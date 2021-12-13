import asyncio
from collections import defaultdict
import math
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
    for i in range(len(L)):
        events[f'{i} + {0}'].set()
    for p in range(int(math.log(len(L), 2))):
        b = 2 ** (p + 1)
        for i in range(0, len(L), b):
            tasks.append(asyncio.create_task(merge(i, i + b // 2, i + b, n, events[f'{i} + {p}'], events[f'{i + b // 2} + {p}'], events[f'{i} + {p + 1}'])))
            n += 1
    await asyncio.gather(*tasks)

L = eval(sys.stdin.read())
new_len = 2
while 2 ** new_len < len(L):
    new_len += 1
to_add = 2 ** new_len - len(L)
extra_num = min(L) - 1

L += [extra_num] * to_add
LL = L.copy()

# I hope noone will see this solution. I'm to tired to tryhard :/
# Don't copypaste this solution. It should be unique (because it is too bad actually)

asyncio.run(joiner())
L = L[to_add:]
print(L)

