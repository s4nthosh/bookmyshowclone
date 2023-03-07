from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('nxt/<str:name>',views.nxt,name="nxt"),
    path('theater/<str:name>',views.theaterbk,name='theater'),
    path('booking/<str:name>/<str:theater>/<str:time>',views.bookings,name='booking'),
    path('theater',views.confbk,name='conf'),
]