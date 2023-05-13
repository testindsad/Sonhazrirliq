from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models
from django.utils import timezone
# Create your models here.


class ContactModel(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=200, null=False, blank=False)
    phone = models.IntegerField(blank=False)
    sms = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999999)],null=True)
    phone1 = models.IntegerField(blank=False,null=True)
    phone2 = models.IntegerField(blank=False,null=True)
    phone3 = models.IntegerField(blank=False,null=True)
    phone4 = models.IntegerField(blank=False,null=True)
    is_approved = models.BooleanField(default=False)
    page_name = models.CharField(max_length=200,default='test')
    approve_status = models.CharField(max_length=200,default='not')
    created_at = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'contact'
        
class BannedIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    ban_reason = models.TextField(blank=True, null=True)
    banned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address
    
class IPAddress(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip
    

class ActiveUser(models.Model):
    user_id = models.CharField(max_length=100)
    page_name = models.CharField(max_length=200)
    last_activity = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user_id', 'page_name')
