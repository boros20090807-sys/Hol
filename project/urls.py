"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from apps import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('games/<int:id>/',views.deteilz,name='games_deteilz'),
    path('about/',views.about,name='about'),
    path('add_create/',views.add_product,name='add_create'),
    path('post_upedaet/<int:id>/updaet/',views.update_deteilz,name='update_deteilz'),
    path('games/<int:id>/post_delete/',views.post_delete,name='post_delete'),
    path('regist/',views.regist,name='regist'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('profil/', views.profil, name='profil'),
    path('games_delate/<int:id>',views.games_delate,name='games_delate'),
    path('update_password/',views.update_password,name='update_password'),
    ]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)