from queue import Queue


class Request:

    counter: int = 0

    def __init__(self, title: str):
        Request.counter += 1

        self.id = Request.counter
        self.title = title

    def __str__(self) -> str:
        return f"id: {self.id}, title: {self.title}"


# Створити чергу заявок
queue: Queue = Queue()


def generate_request(title: str) -> None:
    request: Request = Request(title)
    queue.put(request)

    print(f"Request initiated: '{request}'")


def process_request() -> None:
    if queue.empty():
        print("No requests found, the queue is empty.")
        return

    request: Request = queue.get()
    print(f"Request processed: '{request}'")


counter: int = 0

while True:
    counter += 1
    generate_request(f"Request #{counter}")

    process_request()
