from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.GiftCodeList.as_view()),
    path('<int:pk>/', views.GiftCodeDetail.as_view()),
    path('usage/', views.GiftCodeUsageList.as_view()),
    path('usage/<int:pk>/', views.GiftCodeUsageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
