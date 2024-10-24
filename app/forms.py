# forms.py

from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',  
            'insured', 'commercial_vehicle', 'fracture', 'rear_end', 'passenger', 'pedestrian'
        ]

        labels = {
            'insured': 'Were you insured?',  # Custom label for 'insured' field
            'commercial_vehicle': 'Was it a commercial vehicle?',  # Custom label for 'commercial_vehicle'
            'fracture': 'Did you sustain a fracture?',  # Custom label for 'fracture'
            'rear_end': 'Was it a rear-end collision?',  # Custom label for 'rear_end'
            'passenger': 'Were you a passenger?',  # Custom label for 'passenger'
            'pedestrian': 'Were you a pedestrian?',  # Custom label for 'pedestrian'
        }

        # Add widgets to turn certain fields into dropdown (select) menus
        widgets = {
              # Choices for Driver Fault

            # Add dropdowns (select) for other new fields as well
            'insured': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')]),  # Dropdown for Insured
            'commercial_vehicle': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')]),  # Dropdown for Commercial Vehicle
            'fracture': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')]),  # Dropdown for Fracture
            'rear_end': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')]),  # Dropdown for Rear End
            'passenger': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')]),  # Dropdown for Passenger involved
            'pedestrian': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')]),  # Dropdown for Pedestrian involved
        }
