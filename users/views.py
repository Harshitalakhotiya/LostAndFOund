from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from .models import meetup

class MeetUpObject:
	def __init__(self, id, lost_end, found_end, product):
		self.id = id
		self.lost_end = User.objects.get(id = lost_end)
		self.found_end = User.objects.get(id = found_end)
		self.product = product

def Register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username}! Now you can login')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def Profile(request):
    return render(request, 'users/profile.html')
# Create your views here.

def showNotifications(request):
	user_id = request.user.id
	print(request.user)

	print(meetup.objects.filter(lost_end = user_id))
	print(meetup.objects.filter(found_end = user_id))

	if request.method == "POST":
		print(request.POST)
		#meet_id = request.POST.get("id")
		email=request.POST.get('send_email')
		message=request.POST.get('message')
		if meet_id:
			print(meet_id)
			meetup_instance = meetup.objects.get(id = meet_id)

			lost_id = meetup_instance.lost_end
			found_end = meetup_instance.found_end

		else:
			print("No id found")
	meetup_items = meetup.objects.filter(Q(lost_end = user_id) | Q(found_end = user_id))
	items = []
	for i in meetup_items:
		print(type(i.id))
		items.append(MeetUpObject(i.id, i.lost_end, i.found_end, i.product))
	#print(meetup_items)

	return render(request, 'users/notification.html', {'items': items})