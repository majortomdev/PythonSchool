import os
import shutil
import send2trash


# print(os.getcwd())
#
# file = open('sillier.txt','w')# creates the file if not exists, gives it write permissions
# file.write("testing the silly text")#writes to it
# file.close()
#
# print(os.listdir())

#####*********************************************************************


#   MOVE a file with shutil

#shutil.move('silly.txt','C:\\Users\\user\\Desktop')


#####*********************************************************************


#  SAFER way to delete files, as can still be recovered
# send2trash.send2trash('sillier.txt')

###*********************


#    way to WALK files

#print(os.walk('C:\\Users\\user\\Desktop\\Python\\topfolder'))

path = 'C:\\Users\\user\\Desktop\\Python\\topfolder'

for i in os.walk('C:\\Users\\user\\Desktop\\Python\\topfolder'):
    print(i[2])
# for folder, subfolder, file in os.walk(path):
#     print(f'In folder: {folder}')
#     print(f'Subfolders are: ')
#     for sub in subfolder:
#         print(f'\t{sub}')
#     print(f'Files are: ')
#     for fi in file:
#         print(f'\t{fi}')
#     print('\t')