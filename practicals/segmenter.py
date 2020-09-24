import sys

line = sys.stdin.readline()
while line != '':
        for c in '?!.':
                line = line.replace(c, c + '\n')
        sys.stdout.write(line)
        line = sys.stdin.readline()
