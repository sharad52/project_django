from django.urls import path
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
	path('login/',views.CustomLogin.as_view(),name='login'), #this as_view() is very important in class based view
	path('signup/',views.SignupView.as_view(),name='signup'),
]