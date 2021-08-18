from django.urls import path

from .views import homepage,category,categories,gif

urlpatterns = [
    
    path('', homepage),
    path('category/<str:wrd>', category),
    path('categories', categories),
    path('gif/<int:num>', gif),
  
    
]