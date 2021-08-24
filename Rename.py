import os

file_path = 'G:/ImageData/CVC-ClinicDB/CVC-ClinicDB_datasets/78 works/Polyp edge 9/without processed/'
output_path = 'G:/ImageData/CVC-ClinicDB/CVC-ClinicDB_datasets/78 works/Polyp edge 9/rename without processed/'

files = os.listdir(file_path)

# files = files.sort()

index = 1

for file in files:
    old_dir = os.path.join(file_path, '{}.png'.format(index))

    new_dir = os.path.join(output_path, "cvc-clinic{}.png".format(index))
    os.rename(old_dir, new_dir)

    index += 1
