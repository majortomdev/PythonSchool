#import zipfile

# my_zip = zipfile.ZipFile('file_compressed.zip', 'w')
#
# my_zip.write("my_text_A.txt")
# my_zip.write("my_text_B.txt")
#
# my_zip.close()
# the zip file is now created with these 2 files in itr

####*********    now to OPEN it   **************************


# open_zip = zipfile.ZipFile('file_compressed.zip', 'r')
#
# open_zip.extractall() #...now theyv been extracted to the folder
# or if i want to extract less i specify ->  open_zip.extract('my_file_A.txt')





####*************   ANOTHER way to zip files    *********************

import shutil

# source_folder = 'C:\\Users\\user\\Desktop\\Python\\topfolder'
#
# destination_file = 'all_compressed'
#
# shutil.make_archive(destination_file, 'zip', source_folder)

#*********** now a zip file has been created with all the folder contents    *********



##****** can now CREATE a folder to hold the EXTRACTED contents   ************

shutil.unpack_archive('all_compressed.zip', 'extraction_finished', 'zip')

##****** SHUTIL is more practical, useful than zipfile   **********************