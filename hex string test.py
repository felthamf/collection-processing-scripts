import os
import csv
import binascii


folder = r"Z:\manuscripts\Processing\COPIES  for processing\Flora_PRO_2002_Miria Simpson_A2002-379"

for root, subs, files in os.walk(folder):
	print('Directory: %s' % root)
	print ('Files: %s' % len(files))
	s = set()
	for doc in files:
		print('%s' % doc)
		docpath = os.path.join(root,doc)
		with open(docpath,'r') as data:
			bytes = data.read()
			string = binascii.hexlify(bytes)
			ministring = string[0:1200]
			s.add(ministring)
	print ('Hex signatures in Directory: %s' % len(s))


# with open(r"Z:\manuscripts\Processing\COPIES  for processing\Miria_reporting\set_testing.txt", 'ab') as mydoc:
# 	data.write(s)	

