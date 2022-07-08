from django.urls import path
from . import views


app_name = 'urls'

urlpatterns = [
    path('', views.url_create, name='create'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('<slug:slug>/', views.redirect_outside, name='redirect')
]
