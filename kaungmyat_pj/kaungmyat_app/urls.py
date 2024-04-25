from django.urls import path
from kaungmyat_app import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('Min/',views.k,name="k"),
    path('Myat/',views.s,name="s"),
    path('Alex/',views.n,name="n"),
    path('John/',views.m,name="m"),
    path('Kyaw/',views.o,name="o")

]

