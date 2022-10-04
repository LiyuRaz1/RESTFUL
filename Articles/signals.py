from django.db.models.signals import pre_save
#used to save instances. this signal is sent at the begining of a models save() method, unlike post_save method

from django.dispatch import receiver
from .models import Article
from django.utils.text import slugify

@receiver(pre_save, sender=Article)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug 