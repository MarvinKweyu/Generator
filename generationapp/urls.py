from django.urls import path
from .views import IdStampList


urlpatterns = [
    path('', IdStampList.as_view()),
]
