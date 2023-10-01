from select import select
import os
import subprocess
from contextlib import contextmanager


@contextmanager
def pipe():
    r, w = os.pipe()
    yield r, w
    os.close(r)
    os.close(w)


with pipe() as (r, w):
    cmd = 'echo test'
    with subprocess.Popen(["./subprogram"], stdout=w, stderr=w) as p:
        while p.poll() is None:
            # get read buffer from the output when ready without blocking
            while len(select([r], [], [], 0)[0]) > 0:
                # read 1024 bytes from the buffer
                buf = os.read(r, 1024)
                print(buf.decode('utf-8'), end='')
