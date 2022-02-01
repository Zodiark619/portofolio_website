from django.urls import path
from meong2 import views


urlpatterns=[

    path('',views.django_rest,name='django_rest'),
    path('1/',views.django_rest1,name='django_rest1'),
    path('api/',views.django_rest1_api,name='django_rest1_api')

]