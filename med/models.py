from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import json

class Patient(models.Model):
    center = models.CharField(max_length=100, null=True, blank=True)

    patient_id = models.CharField(max_length=50, unique=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    history = models.TextField()
    scan_type = models.CharField(max_length=10)
    body_part = models.CharField(max_length=100, default='Head')
    ref_by = models.CharField(max_length=100, default='Doctor Unknown')
    # Changed from ImageField to TextField
    scan_image = models.TextField()
    entry_time = models.DateTimeField(auto_now_add=True)
    final_time = models.DateTimeField(null=True, blank=True)
    tat = models.CharField(max_length=20, null=True, blank=True) 
    
    assigned_time = models.DateTimeField(null=True, blank=True) 
    status = models.CharField(max_length=10, default='UNREAD')
    report = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey('UserAccount', on_delete=models.CASCADE, null=True, blank=True)

    assigned_to = models.ForeignKey(
        'UserAccount',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_patients'
    )
    def save(self, *args, **kwargs):
        if not self.patient_id:
            now = datetime.now()
            self.patient_id = f"P{now.strftime('%Y%m%d%H%M%S')}"
        super(Patient, self).save(*args, **kwargs)
    
    # Helper method to get images as list
    def get_images(self):
        try:
            if self.scan_image:
                # Try to parse as JSON array
                parsed = json.loads(self.scan_image)
                if isinstance(parsed, list):
                    return parsed
                # If single string, return as list
                return [parsed] if parsed else []
            return []
        except:
            # Backward compatibility: if single image (old format)
            return [self.scan_image] if self.scan_image else []
    
    # Helper method to set images
    def set_images(self, images_list):
        if isinstance(images_list, list):
            self.scan_image = json.dumps(images_list)
        else:
            # Single image - convert to array
            self.scan_image = json.dumps([images_list])
    
    class Meta:
        db_table = 'patients'


class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reports')
    report_text = models.TextField(blank=True)
    status = models.CharField(max_length=10, default='DRAFT')  # DRAFT or FINAL
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('UserAccount', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Report for {self.patient.name} - {self.status}"


from django.db import models
from django.utils import timezone
USERTYPES = (
    ('RADS', 'RADS'),
    ('IMAGING', 'IMAGING'),
    ('SUPERADMIN', 'Super Admin'),
    ('ADMIN', 'Admin'),
)

class UserAccount(models.Model):
    created_at = models.DateTimeField(default=timezone.now) 
    name = models.CharField(max_length=100)
    userid = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=10, choices=USERTYPES)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    profile_picture = models.TextField(null=True, blank=True)  # Base64 encoded image

    parent_admin = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='sub_users')



    def __str__(self):
        return f"{self.name} ({self.userid})"
        

class SuperAdminCreatedUsers(models.Model):
    name = models.CharField(max_length=200)
    userid = models.CharField(max_length=200)
    usertype = models.CharField(max_length=50)
    contact = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
