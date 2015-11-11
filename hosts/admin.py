from django.contrib import admin
from models import Host
from guardian.admin import GuardedModelAdmin
# Register your models here.
class HostAdmin(GuardedModelAdmin):
    list_display = ('hostname', 'ip', 'created_at')

admin.site.register(Host, HostAdmin)