"""
URL configuration for kaungmyat_pj project.

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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kaung/',include("kaungmyat_app.urls")),
    path('Min/' , include("kaungmyat_app.urls")),
    path('Myat/' , include("kaungmyat_app.urls")),
    path('Alex/', include("kaungmyat_app.urls")),
    path('John/', include("kaungmyat_app.urls")),
    path('Kyaw/', include("kaungmyat_app.urls"))

]
