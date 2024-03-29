from threading import Condition, Thread


def One():
    print('one', end='')


def Two():
    print('two', end='')


def Three():
    print('three', end='')


class Foo():

    def __init__(self):
        self.cd = Condition()
        self.NUM = 0

    def first(self,PrintFirst:callable):
        # 这里使用with语法糖,
        #完成了锁的获取acquire
        #锁的释放
        with self.cd:
            while self.NUM != 0:
                self.cd.wait()
            PrintFirst()
            self.NUM += 1
            self.cd.notify_all()

    def second(self,PrintSecond:callable):
        self.cd.acquire()
        while self.NUM != 1:
            self.cd.wait()
        PrintSecond()
        self.NUM += 1
        self.cd.notify_all()
        self.cd.release()

    def third(self,PrintThird:callable):
        self.cd.acquire()
        while self.NUM != 2:
            self.cd.wait()
        PrintThird()
        self.NUM += 1
        self.cd.notify_all()
        self.cd.release()

if __name__ == '__main__':
    foo = Foo()
    callablelist = [foo.first, foo.second, foo.third]
    callablelistargs = [One, Two, Three]
    order = [2, 1, 3]
    A = Thread(target=callablelist[order[0]-1], args=(callablelistargs[order[0]-1],))
    B = Thread(target=callablelist[order[1]-1], args=(callablelistargs[order[1]-1],))
    C = Thread(target=callablelist[order[2]-1], args=(callablelistargs[order[2]-1],))
    A.start()
    B.start()
    C.start()

