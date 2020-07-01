from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver



class MyUserManager(BaseUserManager):
	def create_user(self, email, name, password=None):
		my_user = self.model(email=self.normalize_email(email), name=name)
		my_user.set_password(password)
		my_user.save()
		print('my user manager')
		return my_user


class MyUser(AbstractBaseUser):
	email = models.EmailField(max_length=150, unique=True)
	name = models.CharField(max_length=100, blank=True)
	joined_on = models.DateField(auto_now_add=True)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']



class BlogPost(models.Model):
	member = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def update_blogpost_signal(sender, instance, created, **kwargs):
	if created:
		BlogPost.objects.create(member=instance)
	instance.blogpost.save()















