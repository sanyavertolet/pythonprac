import sys

bts = sys.stdin.buffer.read()
n, bts = bts[0:1], bts[1:]

#batch_size = len(bts) // n[0] if len(bts) % n[0] == 0 else len(bts) // n[0] + 1
batch_size = len(bts) // n[0]

ordered_bts = b''.join(sorted([bts[i * len(bts) // n[0]:(i + 1) * len(bts) // n[0]] for i in range(n[0])]))

sys.stdout.buffer.write(n + ordered_bts)
