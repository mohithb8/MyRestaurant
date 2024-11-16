from django.urls import path
from dinner import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
  path('',views.home,name='homepage'),
  path('menu/',views.menu,name='menu'),
  path('additems',views.fun1,name='item'),
] 
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)