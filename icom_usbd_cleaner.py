import os

search_string = "USB-D"
path = "/Volumes/Untitled/IC-7300/Voice" # Set your path here...

filenames_list = [os.path.join(dp, f) for dp, dn, filenames in os.walk(path) for f in filenames if os.path.splitext(f)[1] == '.wav']

for filename in filenames_list:
    print filename, 
    # Open file in binary mode
    with open(filename, 'rb') as file:
        file.seek(-256 * 1, os.SEEK_END)  # Just last 256 bytes
        if search_string in file.read():
            print search_string
            os.remove(filename)
        else:
            print