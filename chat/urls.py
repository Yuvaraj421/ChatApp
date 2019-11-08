from django.urls import path, re_path

from .views import index, room                   # importing views from current directory

app_name = 'chat'

# To call the view, we need to map it to a path
urlpatterns = [
    path('', index, name="index"),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),



]

