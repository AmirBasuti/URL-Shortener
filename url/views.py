from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework import generics
from url.models import UrlModel
from url.serilizer import UrlSerializer

class ShowView(View):
    def get(self, request, slug, *args, **kwargs):
        url = get_object_or_404(UrlModel, slug=slug)
        return HttpResponse(f"The URL is: {url.destination}")

class UrlListCreate(generics.ListCreateAPIView):
    queryset = UrlModel.objects.all()
    serializer_class = UrlSerializer