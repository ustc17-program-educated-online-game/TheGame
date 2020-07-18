# 需要在python manage.py shell 中运行，初始化系统自带游戏地图，会删除所有原有的地图
from game import models


def initial_database():
    del_list = models.Map.objects.all()
    for i in del_list:
        i.delete()
    map0 = '1111111111111111111113111211111111111111111211111111111111111111111111111111111111111111111111111111'
    models.Map.objects.create(id=1000, name='测试关卡', length=10, width=10, state=map0, startx=4, starty=1, endx=4,
                              endy=4, treasurex=2, treasurey=1, characterType=1, characterState='r')
    map1 = '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    models.Map.objects.create(id=10001, name='第一关', length=10, width=10, state=map1, startx=4, starty=1, endx=4, endy=2,
                              characterType=1, characterState='r')
    map2 = '1111111111111111111111111111111111111111111121111111111111111111111111111111111111111111111111111111'
    models.Map.objects.create(id=10002, name='第二关', length=10, width=10, state=map2, startx=4, starty=1, endx=5, endy=3,
                              characterType=1, characterState='r')
    map3 = '1111111111111111111111111111111111111111111121111112111111111112111111111111111111111111111111111111'
    models.Map.objects.create(id=10003, name='第三关', length=10, width=10, state=map3, startx=4, starty=1, endx=5, endy=7,
                              characterType=1, characterState='r')
    map4 = '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    models.Map.objects.create(id=10004, name='第四关', length=10, width=10, state=map4, startx=4, starty=1, endx=8, endy=8,
                              characterType=1, characterState='r')
    map5 = '1111111111111111111113111211111111111111111211111111111111111111111111111111111111111111111111111111'
    models.Map.objects.create(id=10005, name='第五关', length=10, width=10, state=map5, startx=4, starty=1, endx=4, endy=4,
                              treasurex=2, treasurey=1, characterType=1, characterState='r')
    map6 = '2222222222211111111221222222122122222212211122111221212112222111211222212221122221222211122222222222'
    models.Map.objects.create(id=10006, name='第六关', length=10, width=10, state=map6, startx=8, starty=1, endx=8, endy=8,
                              characterType=1, characterState='u')


#if __name__ == '__main__':
initial_database()
