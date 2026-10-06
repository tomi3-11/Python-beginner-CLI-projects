import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from an empty priority queue')
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return not self._queue

    def size(self):
        return len(self._queue)

    def peek(self):
        if self.is_empty():
            raise IndexError('peek from an empty priority queue')
        return self.queue[0][-1]

# Usage Example
pq = PriorityQueue()

# Add elements with priority
pq.push("low priority task", 1)
pq.push("high priority task", 3)
pq.push("medium priority task", 2)

print("Size:", pq.size()) # Output: Size 3

# Retrieve elements in priority order
print(pq.pop()) # Output: high priority task
print(pq.pop()) # Output: medium priority task
print(pq.pop()) # Output: low priority task

print("Is empty?", pq.is_empty()) # Output: Is empty? True
