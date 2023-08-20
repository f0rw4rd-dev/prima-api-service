from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.PlayerCosmeticList.as_view()),
    path('<int:pk>/', views.PlayerCosmeticDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
