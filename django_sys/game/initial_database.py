from game import models


def initial_database():
    del_list = models.Map.objects.all()
    for i in del_list:
        i.delete()
    map1 = '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    models.Map.objects.create(id=1, name='第一关', length=10, width=10, state=map1, startx=4, starty=1, endx=4, endy=2,
                              characterType=1, characterState='r')
    map2 = '1111111111111111111111111111111111111111111121111111111111111111111111111111111111111111111111111111'
    models.Map.objects.create(id=2, name='第二关', length=10, width=10, state=map2, startx=4, starty=1, endx=5, endy=3,
                              characterType=1, characterState='r')
    map3 = '1111111111111111111111111111111111111111111121111112111111111112111111111111111111111111111111111111'
    models.Map.objects.create(id=3, name='第三关', length=10, width=10, state=map3, startx=4, starty=1, endx=5, endy=7,
                              characterType=1, characterState='r')
    map4 = '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    models.Map.objects.create(id=4, name='第四关', length=10, width=10, state=map4, startx=4, starty=1, endx=8, endy=8,
                              characterType=1, characterState='r')
    map5 = '1111111111111111111113111211111111111111111211111111111111111111111111111111111111111111111111111111'
    models.Map.objects.create(id=1000, name='第五关', length=10, width=10, state=map5, startx=4, starty=1, endx=4, endy=4,
                              treasurex=2, treasurey=1, characterType=1, characterState='r')


#if __name__ == '__main__':
initial_database()
