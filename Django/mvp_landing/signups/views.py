from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext

from django.contrib import messages

from .forms import SignUpForm

def home(request):
    
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank you for joining.')
    
    return render_to_response("signup.html", 
                              locals(), 
                              context_instance = RequestContext(request))
