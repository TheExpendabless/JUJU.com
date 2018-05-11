# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Community(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    link = models.CharField(unique=True, max_length=255)
    district = models.CharField(max_length=255)
    bizcircle = models.CharField(max_length=255)
    taglist = models.CharField(db_column='tagList', max_length=255)  # Field name made lowercase.
    onsale = models.CharField(max_length=255)
    onrent = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    housetype = models.CharField(max_length=255, blank=True, null=True)
    cost = models.CharField(max_length=255, blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    building_num = models.CharField(max_length=255, blank=True, null=True)
    house_num = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    validdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'community'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hisprice(models.Model):
    houseid = models.CharField(db_column='houseID', primary_key=True, max_length=255)  # Field name made lowercase.
    totalprice = models.CharField(db_column='totalPrice', max_length=255)  # Field name made lowercase.
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hisprice'
        unique_together = (('houseid', 'totalprice'),)

class newsFlash(models.Model):
    id = models.CharField(primary_key=True,max_length=255)
    link =models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    source=models.CharField(max_length=255)
    datetime=models.CharField(max_length=255)
    img=models.CharField(max_length=255,null=True)
    img_name=models.CharField(max_length=255)


class Houseinfo(models.Model):
    houseid = models.CharField(db_column='houseID', primary_key=True, max_length=255)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    community = models.CharField(max_length=255)
    years = models.CharField(max_length=255)
    housetype = models.CharField(max_length=255)
    square = models.CharField(max_length=255)
    direction = models.CharField(max_length=255)
    floor = models.CharField(max_length=255)
    taxtype = models.CharField(max_length=255)
    totalprice = models.CharField(db_column='totalPrice', max_length=255)  # Field name made lowercase.
    unitprice = models.CharField(db_column='unitPrice', max_length=255)  # Field name made lowercase.
    followinfo = models.CharField(db_column='followInfo', max_length=255)  # Field name made lowercase.
    decoration = models.CharField(max_length=255)
    validdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'houseinfo'


class Rentinfo(models.Model):
    houseid = models.CharField(db_column='houseID', primary_key=True, max_length=255)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    zone = models.CharField(max_length=255)
    meters = models.CharField(max_length=255)
    other = models.CharField(max_length=255)
    subway = models.CharField(max_length=255)
    decoration = models.CharField(max_length=255)
    heating = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    pricepre = models.CharField(max_length=255)
    updatedate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rentinfo'


class Sellinfo(models.Model):
    houseid = models.CharField(db_column='houseID', primary_key=True, max_length=255)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    community = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    years = models.CharField(max_length=255)
    housetype = models.CharField(max_length=255)
    square = models.CharField(max_length=255)
    direction = models.CharField(max_length=255)
    floor = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    totalprice = models.CharField(db_column='totalPrice', max_length=255)  # Field name made lowercase.
    unitprice = models.CharField(db_column='unitPrice', max_length=255)  # Field name made lowercase.
    dealdate = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255)
    updatedate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sellinfo'

class User(models.Model):
     username = models.CharField(max_length=50)
     password = models.CharField(max_length=50)
     email = models.EmailField(max_length=50)

class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=11, verbose_name=u"手机号码", null= True, blank= True, default='')
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

class UserCollect(models.Model):

    # 此处应设置外键与级联删除等，但是目前还未实现
    # 未设置主键，自动生成了id作为主键，无实际含义
    user = models.CharField(max_length=150,verbose_name=u"用户")
    community_id = models.BigIntegerField(default=0,verbose_name=u"小区ID")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"收藏时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

