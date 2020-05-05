from django.db import models

class User(models.Model):
    username = models.CharField('用户名', max_length=20, unique=True)
    password = models.CharField('密码', max_length=20)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        db_table = "user"

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='用户名', unique=True, on_delete=models.CASCADE)
    email = models.EmailField('邮箱', blank=True)
    birth = models.DateField('生日', blank=True, null=True)
    phone = models.CharField('手机', max_length=20, null=True)

    def __str__(self):
        return "user{}".format(self.user.username)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        db_table = "user_profile"