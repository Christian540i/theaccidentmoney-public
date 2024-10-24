
from django.db import models

class Lead(models.Model):
    # Contact Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    # Multiple-choice questions
    YES_NO = [
        ('', ''),
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    
    
    insured = models.CharField(max_length=3, choices=YES_NO, default='')  # Insured (Yes/No)
    commercial_vehicle = models.CharField(max_length=3, choices=YES_NO, default='')  # Commercial Vehicle (Yes/No)
    fracture = models.CharField(max_length=3, choices=YES_NO, default='')  # Fracture (Yes/No)
    rear_end = models.CharField(max_length=3, choices=YES_NO, default='')  # Rear End (Yes/No)
    passenger = models.CharField(max_length=3, choices=YES_NO, default='')  # Passenger involved (Yes/No)
    pedestrian = models.CharField(max_length=3, choices=YES_NO, default='')  # Pedestrian involved (Yes/No)

    # Timestamp for when the lead was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
