"""project_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="main"),
    path('admi1/',views.admi1,name='admi1'),
    path('register/',views.register,name="register"),
    path('uslogin/',views.uslogin,name="uslogin"),

    path('adlogin/',views.adlogin,name="adlogin"),
    path('adminhome/',views.adminhome,name="adminhome"),
    path('adminuser/',views.adminuser,name="adminuser"),
    path('adminproduct/',views.adminproduct,name="adminproduct"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('pupdate/',views.pupdate,name="pupdate"),
    path('pro_delete/',views.pro_delete,name="pro_delete"),

    path('register_user/',views.register_user,name='register_user'),
    path('pro_update_save/',views.pro_update_save,name="pro_update_save"),

    path('user_login/',views.user_login,name="user_login"),
    path('userhome/',views.userhome,name="userhome"),
    path('user_update/',views.user_update,name="user_update"),
    path('save_update/',views.save_update,name="save_update")




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
