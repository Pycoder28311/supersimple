from django.urls import path
from . import views

urlpatterns = [
    path('new',views.home, name='home'),
    #path('login/',views.loginuser, name='login'),
    #path('logout/',views.logoutuser, name='logout')
]