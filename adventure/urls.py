from django.urls import path

from adventure import views

urlpatterns = [
    path("create-vehicle/", views.CreateVehicleAPIView.as_view()),
    path("start/", views.StartJourneyAPIView.as_view()),
    path("end/", views.StopJourneyAPIView.as_view()),
]
