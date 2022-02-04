from django.urls import path
from data.views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view()),
]
