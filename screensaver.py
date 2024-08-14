import subprocess as sp

out = sp.check_output(['stty', 'size'])
out = out.decode().rstrip().split()
rows = int(out[0])
cols = int(out[1])
print(rows, cols)
