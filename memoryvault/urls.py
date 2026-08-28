from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('accounts/',include('accounts.urls')),
    path('memory/',include('memories.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
