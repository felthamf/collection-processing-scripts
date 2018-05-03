import os
import csv
import hashlib
import shutil

#sets the root point to start os.walk
my_folder = r"\\wlgprdfile02\home$\FelthaFl\home\Moving_Test"
destination = r"\\wlgprdfile02\home$\FelthaFl\home\Moving"

#function for creating hash
def create_hash(filepath):
	"""return the hash of a file object"""
	hasher = hashlib.md5()
	BLOCKSIZE = 65536
	with open(filepath, 'rb') as afile:
		buf = afile.read(BLOCKSIZE)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(BLOCKSIZE)
	return (hasher.hexdigest())

#clever way of opening files that then shuts them again. Notice that opening something as "wb" (write binary) removes the second line break from .csv
with open("my_file_log.csv","wb") as data:
	#csv option
	writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

	for root, dirs, files in os.walk(my_folder):
		for file_name in files:
			full_path = os.path.join(root, file_name)
			rel_path = full_path.replace(my_folder,"")
			__, file_ext = os.path.splitext(full_path)
			file_without_ext = file_name.replace(file_ext,"")
			# checksum = create_hash(full_path)
			destination_path = os.path.join(destination,file_name)
			#txt option
			# data.write ("{0}|{1}|{2}|{3}\n".format(full_path,rel_path,name,file_ext))
			#csv option
			#row=[full_path,rel_path,name,file_ext,checksum]
			# writer.writerow(row)
			if not os.path.exists(destination_path):
					shutil.copy2(full_path, destination_path)
			else:
				suffix = 0
				while os.path.exists(destination_path):
					suffix += 1
					destination_path = os.path.join(destination,"{}_{}{}".format(file_without_ext,suffix,file_ext))
				shutil.copy2(full_path, destination_path)
					 

			







