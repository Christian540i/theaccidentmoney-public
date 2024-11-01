from django.shortcuts import render, redirect
from .forms import LeadForm
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.core.mail import send_mail

@never_cache
def home(request):
    if request.method == 'POST':
        
        form = LeadForm(request.POST)
        
        if form.is_valid():
            lead = form.save(commit=False)
            lead.language_spoken = 'English'  # Default to English for English homepage
            lead.save()
            
            send_mail(
                subject='New Lead Saved',
                message=f'A new lead has been saved with the following details:\n\n'
                        f'Name: {lead.first_name} {lead.last_name}\n'
                        f'Email: {lead.email}\n'
                        f'Phone: {lead.phone_number}\n\n'
                        f'Language Spoken: {lead.language_spoken}',
                from_email='cashfortraffic6@gmail.com',
                recipient_list=['crusanovsky@gmail.com'],
                fail_silently=False,
            )
            
            
            
            messages.success(request, 'Lead information saved successfully!')
            return redirect('success')
    else:
        
        form = LeadForm()

    context = {
        'form': form,
    }

    return render(request, 'home.html', context)

@never_cache
def home_russian(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.language_spoken = 'Russian'  # Default to Russian for Russian homepage
            lead.save()
            messages.success(request, 'Lead information saved successfully!')
            return redirect('success')
    else:
        form = LeadForm()

    context = {
        'form': form,
    }

    return render(request, 'home_russian.html', context)

def submit_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, 'Lead information saved successfully!')
            return redirect('success')  # Redirect to a success page
    else:
        form = LeadForm()

    return render(request, 'lead_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def about(request):
    return render(request, 'about.html')
