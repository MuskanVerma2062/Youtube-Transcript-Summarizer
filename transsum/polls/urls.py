from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create_summary/', createSummary, name="note" )
]