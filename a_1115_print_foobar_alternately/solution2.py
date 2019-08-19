'''
author:mxt
desc:生产者消费者-交替加锁
time：2019/08/17
'''
import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lockfool = threading.Lock()
        self.lockbar = threading.Lock()
        self.lockbar.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.lockfool.acquire()
            printFoo()
            self.lockbar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.lockbar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lockfool.release()

