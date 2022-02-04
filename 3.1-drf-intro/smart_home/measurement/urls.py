from django.urls import path

from measurement.views import MeasurementView, SensorView, SensorDetailView

urlpatterns = [
    path('measurements/', MeasurementView.as_view()),
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view())
]
