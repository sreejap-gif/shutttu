from django.urls import path
from mine import views

urlpatterns = [
    # path('story/', views.story, name='story'),
    # path('story/', views.story, name='story'),


    path('', views.home, name='home'),
    path('story/', views.story, name='story'),
    path('gallery/', views.gallery, name='gallery'),
    path('reasons/', views.reasons, name='reasons'),
    path('surprise/', views.surprise, name='surprise'),
    path('finale/', views.finale, name='finale'),
]



