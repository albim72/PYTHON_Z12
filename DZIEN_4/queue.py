from queue import Queue

q = Queue(maxsize=5)

print(q.qsize())
q.put(564)
q.put(234)
q.put(765)
q.put(345)
q.put(345)

print(q.qsize())

print(f"full: {q.full()}")
print(q.get())
print(q.get())
print(q.get())
print(q.get())
#(q.get())

print(f"kolejka pusta: {q.empty()}")
