from threading import Thread


class MyThread(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        while True:
            print(self.name)


t = MyThread("t")
t.start()
a = MyThread("a")
a.start()
