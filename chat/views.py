
# Create your views here.
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def index(request):
    """
           This method is used to display the index page.
           :param request:
           :returns:  provide service to request the index page.
       """
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    """
           This method is used chat room page for text communication purpose.
           :param request:
           :returns:  provide service to request the room page.
       """
    return render(request, 'chat/room.html', {
        # Explicitly mark a string as safe for HTML output purposes
        # The returned object can be used everywhere a string or unicode object.
        'room_name_json': mark_safe(json.dumps(room_name))
    })
