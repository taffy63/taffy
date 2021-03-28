
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Member, Profile


@receiver(post_save, sender=Member)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print("___________Profile Create Auth Auto________",Profile.objects.all())
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Member)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
