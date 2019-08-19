'''
author:mxt
desc:多线程-条件变量
time：2019/08/17
'''
from threading import Condition, Thread


class FooBar:
    def __init__(self, n):
        self.n = n
        self.cd = Condition()
        self.is_produce = False

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            with self.cd:
                while self.is_produce:
                    self.cd.wait()
                    # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.is_produce = True
                self.cd.notify()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.cd:
                while not self.is_produce:
                    self.cd.wait()
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.is_produce = False
                self.cd.notify()
