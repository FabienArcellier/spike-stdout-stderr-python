import subprocess
import sys

p = subprocess.Popen(["./subprogram"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout_content = []
while True:
    line = p.stdout.readline().decode("utf-8")
    stdout_content.append(line)
    sys.stdout.write(line)
    if line == '' and p.poll() != None:
        break

stdout_content = ''.join(stdout_content)
print("return to the python workflow")
