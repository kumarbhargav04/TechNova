class SimplePoiCache:
    def __init__(self, max_size=1000):
        self.cache = {}
        self.max_size = max_size

    def set(self, key, val):
        if len(self.cache) >= self.max_size:
            first = next(iter(self.cache))
            del self.cache[first]
        self.cache[key] = val

    def get(self, key):
        return self.cache.get(key)
