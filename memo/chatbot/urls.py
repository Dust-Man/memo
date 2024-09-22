# urls.py
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.registerPage,name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('process_audio/', views.process_audio, name='process_audio'),
    path('chat/', views.index, name='index'),
    path('', views.realindex, name='realindex'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)