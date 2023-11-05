# printer/printer.py

from collections import deque


class Document:
    def __init__(self, pages=None):
        self.pages = deque(pages) if pages is not None else deque()

    def append(self, page):
        self.pages.append(page)

    def print(self):
        if not self.pages:
            return None
        return self.pages.popleft()

    def __len__(self):
        return len(self.pages)


class Printer:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, document):
        self.queue.append(document)

    def cancel(self):
        if not self.queue:
            return None
        return self.queue.popleft()

    def __len__(self):
        return len(self.queue)

    def pages(self):
        return sum(len(doc) for doc in self.queue)

    def print(self):
        if not self.queue:
            return None
        first_doc = self.queue[0]
        page = first_doc.print()
        if len(first_doc) == 0:
            self.queue.popleft()
        return page