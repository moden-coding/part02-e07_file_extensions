#!/usr/bin/env python3
import re

def file_extensions(filename):
    empty_file_type = []
    dict_files = {}
    with open(filename, "r") as f:
        for line in f:
            if "." not in line:
                empty_file_type.append(line[:-1])
            else:
                mo = re.search(r"(.*)\.(.*)$",line[:-1])
                file_type = mo.groups()[1]
                file_name = mo.groups()[0]
                if file_type in dict_files:
                    dict_files[file_type].append(f"{file_name}.{file_type}")
                else:
                    dict_files[file_type] = [f"{file_name}.{file_type}"]
            
    
    return (empty_file_type, dict_files)

def main():
    results = file_extensions("src/filenames.txt")
    print(f"{len(results[0])} files with no extension")
    for key, value in results[1].items():
        print(f"{key} {len(value)}")
    
    

if __name__ == "__main__":
    main()
