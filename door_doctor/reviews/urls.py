from django.urls import path
from . import views
from .views import approve_review

app_name = 'reviews'

urlpatterns = [
    path('submit/', views.submit_review, name='submit_review'),
    path('thanks/', views.thank_you, name='review_thanks'),
    path('', views.review_list, name='review_list'),
    path('approve/<token>', views.approve_review, name='approve_review'),
]
