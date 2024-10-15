from django.urls import path
from url.views import ShowView, UrlListCreate

urlpatterns = [
    path('<slug:slug>/', ShowView.as_view(), name='redirect'),
    path('api/urls/', UrlListCreate.as_view(), name='url-list-create'),
]