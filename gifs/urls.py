from django.urls import path

from .views import homepage,category,categories,gif,likes

urlpatterns = [
    
    path('', homepage),
    path('category/<str:wrd>', category),
    path('categories', categories),
    path('gif/<int:num>', gif, name = 'gif'),
    path('likes/<int:num>', likes, name = 'likes')
    
]