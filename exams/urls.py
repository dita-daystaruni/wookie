from django.urls import path
from .views import ExamsApiView

urlpatterns = [
    path("", ExamsApiView.as_view(), name="exams"),
]
