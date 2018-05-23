from multiprocessing import Queue

q = Queue()
q.put('eat')
q.put('sleep')
q.put('code')
print(q)