from django.urls import path
from . import views

urlpatterns = [
    path('itemlost',views.lost_form, name='lostform'),
    path('lostmap',views.index, name='lostmap')
]