# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        was_dropped=True

        if self.size < len(self.finish_time):
            started_at=request.arrived_at
            was_dropped=True
            return Response(was_dropped,started_at)

        if len(self.finish_time)==0:
            started_at=request.arrived_at
            was_dropped=False
            self.finish_time.append(request.time_to_process+request.arrived_at)
            

        elif self.finish_time[0]<=request.arrived_at-request.time_to_process:
            started_at=self.finish_time[-1]+request.arrived_at
            was_dropped=False
            self.finish_time.append(request.time_to_process+request.arrived_at)
            self.finish_time.pop(0)

        else:
            started_at=request.arrived_at
            was_dropped=True


        return Response(was_dropped,started_at)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
