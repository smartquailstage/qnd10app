from django.shortcuts import render
from .models import term

# Create your views here.
def term_list(request):
    terminos = term.objects.all()
    return render(request,
                  'registration/terms.html',
                  {'terminos': terminos,})