import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from log_parse import parseLog
from insert_info import insert_data


class Watcher:
    DIRECTORY_TO_WATCH = "/home/nilim/Documents/programmer/test-kafka/log"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Stop script")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)
            values = parseLog(event.src_path)
            print('values', values)
            insert_data(values)


if __name__ == '__main__':
    w = Watcher()
    w.run()