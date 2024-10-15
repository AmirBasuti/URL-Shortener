from rest_framework import serializers

from url.models import UrlModel


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlModel
        fields = ['slug', 'destination']
        read_only_fields = ['slug']