import struct
import sys

data = sys.stdin.buffer.read()
try:
    markers = [*struct.unpack('=4s', data[0:4]), *struct.unpack('=4s', data[8:12]), *struct.unpack('=3s', data[12:15]), *struct.unpack("=4s", data[36:40])]
except struct.error:
    print('NO')
else: 
    if markers == [b'RIFF', b'WAVE', b'fmt', b'data']:
        try:
            info = [*struct.unpack('=i', data[4:8]), *struct.unpack('=hhi', data[20:28]), *struct.unpack('=h', data[34:36]), *struct.unpack('=i', data[40:44])]
        except struct.error:
            print('NO')
        else:
            print('Size={}, Type={}, Channels={}, Rate={}, Bits={}, Data size={}'.format(*info))
    else:
        print('NO')

