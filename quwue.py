from queue import Queue
import time
import random

request_queue = Queue()

request_id_counter = 1

def generate_request():
    global request_id_counter
    request = {
        "id": request_id_counter,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    request_queue.put(request)
    print(f"Request added to queue: #{request['id']} - {request['timestamp']}")
    request_id_counter += 1

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Application processing: #{request['id']} - {request['timestamp']}")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Application processed #{request['id']}\n")
    else:
        print("The queue is empty. There are no requests to process.\n")

def main():
    print("Service center. Simulating work with applications.\nPress Ctrl+C to exitу.")
    try:
        while True:
            generate_request()
            time.sleep(random.uniform(1, 2))
            process_request()
            time.sleep(random.uniform(1, 2))
            process_request()
            time.sleep(random.uniform(1, 2))
            generate_request()
            time.sleep(random.uniform(1, 2))
            process_request()
            time.sleep(random.uniform(1, 2))
    except KeyboardInterrupt:
        print("\n User termination of the program.")

if __name__ == "__main__":
    main()