import sys, re

def tokenise(line):
	line = re.sub(r'([\(\)”?:!;])', r' \g<1> ', line)
	line = re.sub(r'([^0-9]),', r'\g<1> ,', line)
	line = re.sub(r',([^0-9])', r', \g<1>', line)
	line = re.sub(r'  +', ' ', line[:-1])

	output = []
	for token in line.split(' '):
		if token == '':
			continue
		if token[-1] == '.':
			token = token[:-1] + ' .'
		output.append(token)

	return ' '.join(output)

line = sys.stdin.readline()
while line != '':
	print(tokenise(line.strip('\n')))
	line = sys.stdin.readline()
