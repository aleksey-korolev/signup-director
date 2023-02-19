from django.urls import path
from . import views

urlpatterns = [
    path('participants', views.ParticipantsView.as_view()),
    path('participants/<int:pk>', views.SingleParticipantView.as_view()),
]