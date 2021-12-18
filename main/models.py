from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, username, address, password=None):
        user = self.model(username=username, address=address)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, address, password=None):
        user = self.create_user(
            username=username, address=address
        )
        user.set_password(password)
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    address = models.CharField(max_length=50, null=True , unique=True)
    username = models.CharField(max_length=50, null=True)


    USERNAME_FIELD = 'address'
    REQUIRED_FIELDS = ['username']
    
    objects = UserAccountManager()

    def __str__(self):
        return self.address

    # @property
    def get_num_users(self):
        return User.objects.all().count()


class Player_detail(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    score = models.IntegerField()
    coin_total = models.FloatField()
    box_total = models.IntegerField()
    level = models.ForeignKey("Level", related_name="player_detail", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.address


class Level(models.Model):
    num = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.num}"

    @property
    def get_comments(self):
        return self.comments.all().order_by("-timestamp")


