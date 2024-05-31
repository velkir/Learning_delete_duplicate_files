import hashlib
import os

def file_hash(filename):
  # Create a hash object
  hash_object = hashlib.sha256()
  # Read the file in binary mode and update hash object
  with open(filename, 'rb') as f:
      while True:
          data = f.read(65536)  # Read in 64k chunks
          if not data:
              break
          hash_object.update(data)
  # Get the hexadecimal representation of the hash
  return hash_object.hexdigest()
# Calculate the hash of a file

#Loop through list of files. Delete duplicates
def remove_duplicates(path):
  files = os.listdir(path)
  hashes = {}
  
  for file in files:
    file_path = path+file
    file_hash_value = file_hash(file_path)
    if file_hash_value not in hashes.values():
      hashes[file] = file_hash_value
    else:
      os.remove(file_path)

path = "files-duplicate/"
remove_duplicates(path)