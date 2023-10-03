"""
URL configuration for ormproject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SchoolView),
    path('home/',views.RetrieveView),
    path('pass/',views.StudentPassView),

    path('list/',views.StudentView),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/',views.LogoutView),
    path('signin/',views.SigninView),
    path('delete/<int:id>',views.DeleteView),
    path('update/<int:id>',views.UpdateView),
    path('insert/',views.InsertView),
    path('specific/',views.SpecificColumn),
   
]
