from django.shortcuts import render
from .forms import *

# Create your views h
def home(request):
	
	return render(request, 'found/home.html')

def found_form(request):
	
	form = ProductFoundForm()
		
	return render(request, 'found/foundform.html', {'form': form})
