# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('', home, name='home'),
#     path('detect_page1', detect_page1, name='detect_page1'),
#     path('detect_page2', detect_page2, name='detect_page2'),
#     path('detect_page3', detect_page3, name='detect_page3'),
#     path('detect_page4', detect_page4, name='detect_page4'),
#     # path('detection', detection, name='detection'),
# ]
from django.urls import path
from .views import  detect_media
from django.conf import settings    
from django.conf.urls.static import static

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    # path('', home, name='home'),
    path('', detect_media, name='detect_media'),
    path('detect_media/', detect_media, name='detect_media'),  # Unified route
]
