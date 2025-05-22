from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.SubmitTestResultView.as_view(), name='submit-test'),
]
