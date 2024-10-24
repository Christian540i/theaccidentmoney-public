from django.shortcuts import render, redirect
from .forms import LeadForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data
            messages.success(request, 'Lead information saved successfully!')
            return redirect('success')  # Redirect to a success page
    else:
        form = LeadForm()  # Provide an empty form on GET request

    context = {
        'form': form,  # Pass the form to the template
    }

    return render(request, 'home.html', context)

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
