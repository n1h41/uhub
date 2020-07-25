from django.shortcuts import render
from .forms import contact_us_form
from django.http import HttpResponse

# Create your views here.

def contact(request):
    form = contact_us_form()
    if request.method == 'POST':
        form = contact_us_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks')
    return render(request, 'contact.html', {'form': form})