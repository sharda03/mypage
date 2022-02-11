from django import shortcuts, views
from django.urls import path
from . import views


urlpatterns=[
    path('',views.start),
    path('/<int:month_id>',views.call_by_number),
    path('/<str:month>',views.index,name='monthly_challenges'),
    
]