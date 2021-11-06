from django.urls import path
from .views import Jaxa, Jaxan, kurslar, Mars, bek, auff

urlpatterns=[
    path('', Jaxa.as_view(),name="home"),
    path('about/', Jaxan.as_view(), name="about"),
    path('kurs/', kurslar.as_view(), name='kurslar'),
    path('abdu/', Mars.as_view(), name='Mars'),
    path('bekjon/', bek.as_view(),name='bek'),
    path('marsjon/',auff.as_view(),name='auff')
]