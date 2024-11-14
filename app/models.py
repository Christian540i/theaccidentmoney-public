
from django.db import models

class Lead(models.Model):
    # Contact Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    language_spoken = models.CharField(max_length=20, blank=True, null=True)

    # Multiple-choice questions (Yes/No)
    YES_NO = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    insured = models.CharField(max_length=3, choices=YES_NO, default='No', blank=True, null=True)  # Insured (Yes/No)
    commercial_vehicle = models.CharField(max_length=3, choices=YES_NO, default='No', blank=True, null=True)  # Commercial Vehicle (Yes/No)
    injured = models.CharField(max_length=3, choices=YES_NO, default='No', blank=True, null=True)  # Fracture (Yes/No)
    rear_end = models.CharField(max_length=3, choices=YES_NO, default='No', blank=True, null=True)  # Rear End (Yes/No)
    passenger = models.CharField(max_length=3, choices=YES_NO, default='No', blank=True, null=True)  # Passenger involved (Yes/No)
    pedestrian = models.CharField(max_length=3, choices=YES_NO, default='No', blank=True, null=True)  # Pedestrian involved (Yes/No)

    
   

    # Timestamp for when the lead was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.created_at}"
    



