from collections import deque


def processes(start, end, processes):

    queue = deque([(start, [])])
    while len(queue):
        dest, path = queue.popleft()
        if dest == end:
            return path
        queue.extend( (p[2], path + [p[0]]) for p in processes if p[1] == dest)
    return []

test_processes = [
    ['gather', 'field', 'wheat'],
    ['bake', 'flour', 'bread'],
    ['mill', 'wheat', 'flour']
]
print processes('field', 'bread', test_processes)
print processes('field', 'ferrari', test_processes) # should return []
print processes('field', 'field', test_processes) # should return []
