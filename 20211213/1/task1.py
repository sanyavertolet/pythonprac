import asyncio
from collections import defaultdict
import sys

async def merge(b0, b1, e1, n, event_left, event_right, event_this):
    if b1 - b0 != 0:
        await event_left.wait()
        await event_right.wait()
    b, e0, i = b0, b1, b0
    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
    await asyncio.sleep(0)
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]
    event_this.set()


async def joiner():
    tasks, n = [], 0
    events = defaultdict(asyncio.Event)
    for i in range(16):
        events[4 * i].set()
    for p in range(4):
        b = 2 ** (p + 1)
        for i in range(0, len(L), b):
            # should build a tree of events: if left and right are done, parent should be marked as done
            tasks.append(asyncio.create_task(merge(i, i + b // 2, i + b, n, events[4 * i + p], events[4 * (i + b // 2) + p], events[4 * i + p + 1])))
            n += 1
    await asyncio.gather(*tasks)

L = eval(sys.stdin.read())
LL = L.copy()

asyncio.run(joiner())
print(L)

