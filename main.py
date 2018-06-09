import os
import subprocess

script_dir = os.path.dirname(__file__)
name_of_source_folder='Source'
name_of_result_folder='Result'


if not os.path.exists(os.path.join(script_dir,name_of_result_folder)):
            os.makedirs(os.path.join(script_dir,name_of_result_folder))

for d, dirs, files in os.walk(os.path.join(script_dir,name_of_source_folder)): #Просматриваем каталог
    for file in files:
        subprocess.call([os.path.join(script_dir,'convert.exe'), os.path.join(d, file), '-resize', '200', os.path.join(name_of_result_folder, file)])