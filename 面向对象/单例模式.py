
class MusicPlayer(object):
    #记录第一个被创建对象的引用
    instance = None

    #记录是否执行过初始化动作
    init_flag =False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance=super().__new__(cls)

        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag:
            return
        print('初始化播放器')
        MusicPlayer.init_flag = True

c=MusicPlayer()
print(c)
c1=MusicPlayer()
print(c1)