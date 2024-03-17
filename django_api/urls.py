"""
URL configuration for django_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import django_eventstream
from .routes.sse_route import SSE
from .modules.persistent import Persistent

persist = Persistent()
sseinit = SSE(persist)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sse/init/<str:userID>', sseinit.initialize_sse_con, name='stream'),
    path('sendmessage/<str:userID>/<str:to>/<str:message>/', sseinit.send_message),
    path(r'events/', include(django_eventstream.urls))
]
