from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from found.models import Product
import yake
from users.models import *

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

@login_required
def lost_form(request):
    print(request.session)
    if request.method == 'POST':
        #print(request.POST.get('x'))
        form = LostItemForm(request.POST)
        if form.is_valid():
            form.instance.person = request.user
            this_item = form.save()
            this_item.x = request.session.get('x', 0.0)
            this_item.y = request.session.get('y', 0.0)
            this_item.tags = ','.join(extract_keywords(request.POST['description']))
            this_item.save()
            all_products = Product.objects.all()

            finders = []
            temp_item = []
            for product in all_products:
                flag_x = 0
                if ((product.x - float(this_item.x))**2 + (product.y - float(this_item.y))**2)**0.5 <= 0.02:
                    temp_item = set(list(product.tags.split(',')))
                    temp_item2 = set(list(this_item.tags.split(',')))
                    temp_item = temp_item.intersection(temp_item2)
                    print(list(product.tags.split(',')))


                    # for kw in temp_item:
                    #     for kw2 in list(this_item.tags.split(',')):
                    #         if kw == kw2:
                    #             flag_x += 1
                    if len(temp_item) >= 3:
                        finders.append(product)
                        meetup.objects.create(lost_end=this_item.person.id, found_end=product.person.id, product=product, isLost=True)
                        

            #messages.success(request,f'Item is successfully added')
            context = {
                'id': this_item.id,
                'finders': finders
            }

            print(finders)

            return render(request, 'lost/result.html', context)
            #return redirect('l&f-home')
        else:
            form = LostItemForm()
            title = "Register Missing Article"
            return render(request, 'lost/lostform.html', {'form': form, 'title': title})
    else:
        form = LostItemForm()
        title = "Register Missing Article"
        return render(request, 'lost/lostform.html', {'form': form, 'title': title})

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
		#return render(request, 'lostform', context)
		return redirect('lostform')
		# return JsonResponse({"xvar":xv,"yvar":yv})
	else:
		return render(request, 'lost/map.html')