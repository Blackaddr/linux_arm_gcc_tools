import glob;
import os;
import shutil;

root_dir = os.getcwd() + "/linux_tools"
filesList = set()

for dir_, _, files in os.walk(root_dir):
    for file_name in files:
        rel_dir = os.path.relpath(dir_, root_dir)
        rel_file = os.path.join(rel_dir, file_name)
        filesList.add(rel_file)

sorted_list = sorted(filesList)
for entry in sorted_list:
    print(entry)

with open('tools_manifest.txt', 'w') as f:
    for entry in sorted_list:
        f.write(entry + "\n")

