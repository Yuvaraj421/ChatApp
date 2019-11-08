from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # Include  by default authorization.
    path('admin/', admin.site.urls),  # admin urls
    path('chat/', include('chat.urls', namespace='chat')),   # Include chat urls
    path('', include('page.urls', namespace='')),            # Include page urls

]
