from threading import Thread
from multiprocessing import Process, Queue
from time import time
from numpy import array_split


# Process einfach durch Thread erstetzen, wenn multithreading statt processing gewünscht ist
class Worker(Process):
    def __init__(self, working_list: list[int], queue: Queue):
        super().__init__()
        self.working_list = working_list
        self.queue = queue

    def run(self) -> None:
        for i in range(len(self.working_list)):
            self.working_list[i] *= 2
        self.queue.put(self.working_list)


def main(number_of_threads: int = 4, list_size: int = 100):
    workers = []
    parts = []
    working_list = list(range(list_size))
    for i in array_split(working_list, number_of_threads):
        q = Queue()
        w = Worker(list(i), q)
        workers.append((w, q))

    t1 = time()
    for w in workers:
        w[0].start()

    for w in workers:
        part = w[1].get()
        parts.append(part)
        w[1].close()
        w[0].join()

    t2 = time()
    result = []
    for p in parts:
        result = result + p

    print(result)
    print(f"\n\n{t2 - t1}")


if __name__ == "__main__":
    main(16, 80000000)
