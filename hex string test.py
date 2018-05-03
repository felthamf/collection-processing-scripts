import os
import csv
import binascii

# put root directory here
folder = r""
signatures = []

# gets information about each directory and logs it to screen
for root, subs, files in os.walk(folder):
	print('Directory: %s' % root)
	print ('Files: %s' % len(files))
	for doc in files:
		print('%s' % doc)
		docpath = os.path.join(root,doc)
		with open(docpath,'r') as data:
			bytes = data.read()
			string = binascii.hexlify(bytes)
			# take the first 150 bytes of a file. Can alter this
			ministring = string[0:1200]
			# creates a list of all the first 150 bytes of each file in the directory
			signatures.append(ministring)
print len(signatures)
print signatures[1]

# with open(r"Z:\manuscripts\Processing\COPIES  for processing\Miria_reporting\set_testing.txt", 'ab') as mydoc:
# 	data.write(s)	


