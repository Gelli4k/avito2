from django.urls import path

from ads.views import AdDetailView, AdLoadImageView, AdListView, AdCreateView

urlpatterns = [
    path('', AdListView.as_view()),
    path('<int:pk>', AdDetailView.as_view()),
    path('create/', AdCreateView.as_view()),
    path('<int:pk>/upload_image', AdLoadImageView.as_view())
]
