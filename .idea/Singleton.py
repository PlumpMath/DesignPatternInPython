__author__ = 'huanyu'
def singleton(cls,*args,**kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args,**kw)
        return instances[cls]
    return  _singleton

@singleton
class MySingletonClass(object):
    a = 1
    def __index__(self, x=0):
        self.x = x

one = MySingletonClass()
two = MySingletonClass()

two.a = 3
print id(one)

print id(two)

print one == two
one.x = 5
print one.a

print two.a