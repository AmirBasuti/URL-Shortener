from django.db import models

import hashlib

def generate_unique_slug(destination):
    hash_object = hashlib.md5(destination.encode())
    slug = hash_object.hexdigest()[:6]
    return slug

class UrlModel(models.Model):
    slug = models.SlugField(max_length=6, unique=True, blank=True)
    destination = models.URLField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self.destination)
        super().save(*args, **kwargs)