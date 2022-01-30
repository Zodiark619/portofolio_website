from django.urls import path
from meong1 import views


urlpatterns=[

    path('',views.portfolio,name='portfolio'),
    path('1/',views.portfolio1,name='portfolio1'),

]