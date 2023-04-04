from django.urls import path
from app1.views import *
app_name='page1'
urlpatterns=[
    path('page1/',page1,name='page1')
]