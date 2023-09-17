import subprocess
import sys
from threading import Thread
from typing import Optional, IO

class capture_output:

    def __init__(self, process, capture_stream: Optional[IO] = None, output_stream: Optional[IO] = None):
        self.capture_logs = []
        self.subprocess = process
        self.capture_stream = capture_stream
        self.output_stream = output_stream
        self.thread = Thread(target=self._run_capture)
        self.thread.start()

    def _run_capture(self):
        if self.capture_stream is not None:
            while self.subprocess.poll() is None:
                line = self.capture_stream.readline().decode('utf-8')
                if line != '':
                    self.output_stream.write(line)
                    self.output_stream.flush()
                    self.capture_logs.append(line)

    def output(self):
        self.thread.join()
        return '\n'.join(self.capture_logs)


p = subprocess.Popen(["./subprogram"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout_capture = capture_output(p, p.stdout, sys.stdout)
stderr_capture = capture_output(p, p.stderr, sys.stderr)
p.wait()

stdout = stdout_capture.output()
stderr = stderr_capture.output()
print("get back control in main flow")
