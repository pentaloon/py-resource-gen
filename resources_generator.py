#!/usr/bin/python
import sys, os, base64

def main(argv):
	n = 80
	outputfile = 'resources.py'
	resource = 'class Pixmaps(object):\n'
	for arg in argv:
		try:
			with open(arg, 'rb') as f:
				blob = f.read()
				encoded = str(base64.b64encode(blob))
		except:
			print('failed to read input file')
		chunks = [('    ' + encoded[i:i+n] + ' \\\n') for i in range(0, len(encoded), n)]
		
		name = os.path.splitext(arg)[0]
		resource += '    # ' + arg + '\n    ' + name + ' = \\\n' + ''.join(chunks)
	try:
		with open(outputfile, 'w') as f:
			f.write(resource)
	except:
		print('failed to write output file')
if __name__ == "__main__":
   main(sys.argv[1:])
