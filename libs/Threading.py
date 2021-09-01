from threading import Thread
from queue import Queue


class Threading:

    def __init__(self, worker, data, thread_count=5):
        """
        worker: the function you want to run in multi-threading
        data: data to be process, it is a list
        """

        self.threads = []
        self.queue = Queue()

        # put data into queue for thread-safe
        for item in data:
            self.queue.put(item)

        terminator = Terminator()
        for i in range(1, thread_count + 1):
            # don't ever set daemon=true, it will run forever
            thread = Thread(target=worker, args=(i, self.queue, terminator))
            self.threads.append(thread)

    def start(self):
        for thread in self.threads:
            thread.start()

    def join(self):
        for thread in self.threads:
            thread.join()
        print("all threads are closed")


import signal


class Terminator:
    """
    Listen to KeyboardInterrupt
    """

    def __init__(self):
        self.exit_now = False
        signal.signal(signal.SIGINT, self.set_exit_now)
        signal.signal(signal.SIGTERM, self.set_exit_now)

    def set_exit_now(self, *args):
        print("Exit signal received !!")
        self.exit_now = True

    def is_exit_now(self):
        return self.exit_now
