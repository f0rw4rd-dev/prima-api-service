from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.PlayerItemList.as_view()),
    path('<int:pk>/', views.PlayerItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
