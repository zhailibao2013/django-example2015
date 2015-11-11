from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Host
from django.template import RequestContext
from guardian.shortcuts import get_objects_for_user
from guardian.decorators import permission_required_or_403
from django.contrib.auth.decorators import login_required
from forms import AddHostForm
# Create your views here.
@login_required
def dashboard(request):
    hosts = get_objects_for_user(request.user,'hosts.view_host')
    return render_to_response("dashboard.html",{'hosts':hosts},context_instance=RequestContext(request))
@login_required
@permission_required_or_403("hosts.change_host", (Host, 'id', "host_id"))
def edit(request,host_id):
    host = get_object_or_404(Host, pk=int(host_id))
    if request.method == 'POST':
        form = AddHostForm(request.POST, instance=host)
        print 'before valid'
        if form.is_valid():
            print 'before save'
            host = form.save()
            url = reverse("host_detail", kwargs={'host_id': host.pk})
            return HttpResponseRedirect(url)
    #host = Host.objects.get(id=host_id)
    else:
        form = AddHostForm(instance=host)
    return render_to_response("edit.html", {'form': form, 'host_id': host_id}, context_instance=RequestContext(request))

@login_required
@permission_required_or_403("hosts.add_host",)
def add(request):
    if request.method == 'POST':
        form = AddHostForm(request.POST)
        if form.is_valid():
            host = form.save()
            url = reverse("host_detail",kwargs={'host_id': host.pk})
            return HttpResponseRedirect(url)
    else:
        form = AddHostForm()
    return render_to_response("add.html", {'form': form}, context_instance=RequestContext(request))

@login_required
@permission_required_or_403("hosts.view_host", (Host, 'id', "host_id"))
def detail(request,host_id):
    host = Host.objects.get(id=host_id)
    return render_to_response("detail.html",{'host':host},context_instance=RequestContext(request))

@login_required
@permission_required_or_403("hosts.delete_host", (Host, 'id', "host_id"))
def delete(request,host_id):
    host = Host.objects.get(id=host_id)
    host.delete()
    return HttpResponseRedirect(reverse("host_index"))
