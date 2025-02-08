"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('receipes/', views.receipes,name='receipes'),
    path('update_receipe/<id>', views.update_receipe, name='update_receipe'),
    path('delete_receipe/<id>', views.delete_receipe, name='delete_receipe'),
    path('home/', views.home,name='home'),
     path('order/<int:id>/', views.food_order, name='food_order'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)