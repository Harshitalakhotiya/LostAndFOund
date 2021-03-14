from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from users.models import meetup
import yake
from lost.models import LostItem

def extract_keywords(description):
	language = "en"
	max_ngram_size = 3
	deduplication_thresold = 0.9
	deduplication_algo = 'seqm'
	windowSize = 1
	numOfKeywords = 20

	custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
	keywords = custom_kw_extractor.extract_keywords(description)
	tags = [kw[0] for kw in keywords]
	for i in keywords:
		print(i)
	
	if len(tags) >= 5:
		return tags[-5:]
	else:
		return tags

def home(request):
	title = "Welcome To Lost and Found"
	return render(request, 'found/home.html', {'title': title})

@login_required
def found_form(request):
	print(request.session)
	if request.method == 'POST':
		#print(request.POST.get('x'))
		form = ProductFoundForm(request.POST)
		if form.is_valid():
			form.instance.person = request.user
			this_item = form.save()
			this_item.x = request.session.get('x', 0.0)
			this_item.y = request.session.get('y', 0.0)
			this_item.tags = ','.join(extract_keywords(request.POST['description']))
			this_item.save()
			all_products = LostItem.objects.all()
			
			finders = []
			temp_item = []
			for product in all_products:
				flag_x = 0
				if ((product.x - float(this_item.x))**2 + (product.y - float(this_item.y))**2)**0.5 <= 0.02:
					temp_item = set(list(product.tags.split(',')))
					temp_item2 = set(list(this_item.tags.split(',')))
					# print(list(product.tags.split(',')))
					print(temp_item)
					temp_item = temp_item.intersection(temp_item2)
					print(temp_item)
					print(temp_item2)
					# for kw in temp_item:
					# 	for kw2 in list(this_item.tags.split(',')):
					# 		if kw == kw2:
					# 			flag_x += 1
					if len(temp_item) >= 3:
						finders.append(product.id)
						meetup.objects.create(lost_end=product.person.id, found_end=this_item.person.id, product=this_item, isLost=True)


			messages.success(request,f'Item is successfully added')
			context = {
				'id': this_item.id,
				'finders': finders
			}

			#request.session['finders'] = ' '.join(finders)
			#return redirect('foundresult')
			return render(request, 'found/result.html', {'finders': finders})
		else:
			form = ProductFoundForm()
			title = "Register Missing Article"
			return render(request, 'found/foundform.html', {'form': form, 'title': title})
	else:
		form = ProductFoundForm()
		title = "Register Missing Article"
		return render(request, 'found/foundform.html', {'form': form, 'title': title})

def find_item(request):
	title = "Find Lost Item"
	return render(request, 'found/find_item.html', {'title': title})

def index(request):
	if request.method == 'POST':
		print('HEREEEE')
		xv = request.POST.get('fname')
		print('xv')
		yv = request.POST.get('lname')
		print('HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
		context = {
			'x'  : xv,
			'y' : yv
		}

		request.session['x'] = xv
		request.session['y'] = yv
		#return render(request, 'foundform', context)
		return redirect('foundform')
		# return JsonResponse({"xvar":xv,"yvar":yv})
	else:
		return render(request, 'found/map.html')

def scheduleMeetUp(request):
	if request.method == 'POST':
		product_id = request.POST['id']
		product = Product.objects.get(id = product_id)

		meetup.objects.create(lost_end=product.person.id, found_end=request.user.id, product=product, isLost=True)
		messages.success(request,f'Lost Object has been Identified!')
		return redirect('l&f-home')
	else:
		print(request.session.get('finders'))
		if request.session.get('finders') is not None:
			str_finders = request.session.get('finders')
			print(str_finders)
			id_finders = list(str_finders.split())
			finders = []
			for i in id_finders:
				finders.append(Product.objects.get(id = i))
			return render(request, 'lost/result.html', {'finders': finders})
		else:
			return redirect('l&f-home')