import os

full_list = os.listdir("test/")

def get_uniq_names(full_file_list):
    uniq_names = set()
    extensions = set()
    for full_name in full_file_list:
       u_name, ext = full_name.split('.')
       uniq_names.add(u_name)
       extensions.add(ext)
    return uniq_names, extensions

a, b = get_uniq_names(full_list)

print(a)
print(b)
