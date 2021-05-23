from django.urls import path
from .views import IdStampList


urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view()),
    path('', IdStampList.as_view()),
]
