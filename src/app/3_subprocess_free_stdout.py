import subprocess

p = subprocess.Popen(["./subprogram"], stdout=None, stderr=None)
p.wait()
print("return to the python workflow")
