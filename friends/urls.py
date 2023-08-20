from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.FriendList.as_view()),
    path('<int:pk>/', views.FriendDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
