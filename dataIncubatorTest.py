import sys
import numpy as np

i = []
print('Type numbers to add them to array. Type "exit" to leave program.')
stdin_fileno = sys.stdin
 
for line in stdin_fileno: 
    if 'exit' == line.strip():
        print('Found exit. Terminating the program')
        exit(0)
    try:
        n = float(line)
    except ValueError:
        print("Please only type numbers. Type 'exit' to leave the program.")
        continue
    i.append(n)
    a= round(np.average(i),2)
    sd = round(np.std(i),2)
    md = round(np.median(i),2)

    print(a,",",sd,",",md)