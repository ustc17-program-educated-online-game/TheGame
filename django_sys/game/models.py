from django.db import models

# Create your models here.

class Map(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    creator = models.CharField(max_length=128, default='admin')
    length = models.IntegerField()
    width = models.IntegerField()
    state = models.CharField(max_length=200)

    #关卡起点、终点和宝藏坐标
    startx = models.IntegerField()
    starty = models.IntegerField()
    endx = models.IntegerField()
    endy = models.IntegerField()
    treasurex = models.IntegerField(null=True, blank=True)
    treasurey = models.IntegerField(null=True, blank=True)

    #人物形象和初始时朝向信息
    characterType = models.IntegerField()
    characterState = models.CharField(max_length=2)

    class Meta:
        ordering = ['id']

class PlayerInfo(models.Model):
    name = models.CharField(max_length=128, unique=True)
    passMapNumber = models.IntegerField()
    userLevel = models.IntegerField(default=1)       # 用户级别:1游客，2登录用户

class HistoryInfo(models.Model):
    name = models.CharField(max_length=128, unique=True)
    mapNum = models.IntegerField()
    score = models.IntegerField()
    code = models.TextField()
