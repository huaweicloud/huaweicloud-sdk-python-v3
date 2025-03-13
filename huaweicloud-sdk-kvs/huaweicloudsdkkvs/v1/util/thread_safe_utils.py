import threading


class AtomicBool:
    def __init__(self, value=False):
        self._value = value
        self._lock = threading.Lock()

    def set(self, value):
        with self._lock:
            self._value = value

    def get(self):
        with self._lock:
            return self._value


class AtomicInteger:
    def __init__(self, value=0):
        self._value = value
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self._value += 1
            return self._value

    def decrement(self):
        with self._lock:
            self._value -= 1
            return self._value

    def get(self):
        with self._lock:
            return self._value

    def set(self, num):
        with self._lock:
            self._value = num
            return self._value


class ThreadSafeList:
    def __init__(self):
        self._list = []
        self._lock = threading.Lock()

    def append(self, item):
        with self._lock:
            self._list.append(item)

    def remove(self, item):
        with self._lock:
            self._list.remove(item)

    def clear(self):
        with self._lock:
            self._list = []

    def size(self):
        with self._lock:
            return len(self._list)

    def __str__(self):
        with self._lock:
            return str(self._list)


class ThreadSafeDict:
    def __init__(self):
        self._dict = {}
        self._lock = threading.Lock()

    def get(self, key):
        with self._lock:
            return self._dict.get(key)

    def set(self, key, value):
        with self._lock:
            self._dict[key] = value

    def delete(self, key):
        with self._lock:
            if key in self._dict:
                del self._dict[key]

    def size(self):
        with self._lock:
            return len(self._dict)

    def clear(self):
        with self._lock:
            self._dict = {}

    def keys(self):
        with self._lock:
            return self._dict.keys()

    def include_endpoint(self, endpoint):
        with self._lock:
            for _, value in self._dict.items():
                if value.endpoint.name == endpoint.name and value.endpoint.weight == endpoint.weight:
                    return True
            return False
