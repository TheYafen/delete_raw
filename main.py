import os

PATH = os.getcwd()
EXTS = "CR2"
DELETE_NESTED = False

def main():
    files, dirs = get_full_list(PATH)
    uniq_list, ext_list = get_uniq_names(files)
    nested_files = check_nested(dirs)
    if nested_files and DELETE_NESTED:
        print("Found nested files. Deleting...")
        for file in nested_files:
            print(file)
        for dir in dirs:
            path = os.path.join(PATH, dir)
            nested_files, _ = get_full_list(path)
            uniq_list, ext = get_uniq_names(nested_files)
            for file in uniq_list:
                os.remove(os.path.join(PATH, f"{file}.{EXTS}"))
    else:
        print("No nested files found.")
    if EXTS in ext_list:
        print(f"Deleteing files in root...")
        delete_duplicates(PATH, uniq_list, EXTS)

def get_full_list(path):
    full_list = os.listdir(path)
    files = [file for file in full_list if os.path.isfile(os.path.join(path, file))]
    dirs = [dir for dir in full_list if os.path.isdir(os.path.join(path, dir))]
    return files, dirs

def check_nested(dirs):
    if not dirs:
        return False
    for dir in dirs:
        path = os.path.join(PATH, dir)
        nested_files, _ = get_full_list(path)
        return nested_files

def get_uniq_names(full_file_list):
    uniq_names = set()
    extensions = set()
    for full_name in full_file_list:
        u_name, ext = full_name.split('.')
        ## Adding only JPG file names to the uniq_names set,
        ## as I want RAWs to be deleted only if they have a corresponding JPG
        if ext == 'JPG':
            uniq_names.add(u_name)
        extensions.add(ext)
    return uniq_names, extensions

def delete_duplicates(path, uniq_names, extension):
    for file in uniq_names:
        file_path = os.path.join(path, f"{file}.{extension}")
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    main()
