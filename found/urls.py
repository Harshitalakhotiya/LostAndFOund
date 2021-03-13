from django.urls import path
from . import views
from .views import home


urlpatterns = [
    path('',views.home, name='l&f-home'),
    path('itemfound',views.found_form, name='foundform'),
    path('foundmap',views.index, name='foundmap'),
    path('find_item', views.find_item, name = 'lost')
]