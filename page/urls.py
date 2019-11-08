from django.urls import path
from .views import *  # importing form views


# Giving path for signup and home to call the views.
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', home, name='home'),

]
