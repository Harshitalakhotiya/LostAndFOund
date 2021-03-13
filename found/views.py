from django.shortcuts import render

# Create your views h
def home(request):
	
	return render(request, 'found/home.html')
