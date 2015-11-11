from django.db import models
# Create your models here.
class Host(models.Model):
    hostname = models.CharField(max_length=64)
    ip = models.CharField(max_length=64)
    os = models.CharField(max_length=64,null=True)
    type = models.CharField(max_length=32,null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    class Meta:
        permissions =(
            ('view_host','Can view host'),
        )

    def __unicode__(self):
        return self.hostname
