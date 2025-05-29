# To search for key-words from one file in multiple other files and save the details in a folder.

import os

# Read unique strings from a file, assuming each string is on a new line.
def read_strings_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

# Search for a string in a file and return the line numbers where it's found.
def search_string_in_file(file_path, search_string):  
    matches = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, start=1):
                if search_string in line:
                    matches.append(line_number)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return matches

# Search for each string in all files within a directory and generate a report.
def search_strings_in_directory(strings_file, search_directory, report_file):
    strings = read_strings_from_file(strings_file)
    results = []
    
    for root, _, files in os.walk(search_directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            for search_string in strings:
                matches = search_string_in_file(file_path, search_string)
                if matches:
                    results.append(f"{search_string}: True \nFound in {file_path} at lines {matches}\n\n")
                else:
                    results.append(f"{search_string}: False\n")
    
    with open(report_file, 'w', encoding='utf-8') as report:
        report.writelines(results)
    
    print(f"Search completed. Report saved to {report_file}")
#Copies all the configurations which need manual checks in a file

def find_and_extract(tough_parameters,directory,output_file):
    try:
        with open(tough_parameters, 'r', encoding='utf-8') as f:
           strings = f.readlines()

        with open(output_file, "w") as outfile:
            for filename in os.listdir(directory):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r') as infile:
                    for line in infile:
                        for string in strings:  
                            if string.strip()in line:
                                outfile.write(line)
        print(f"Related configs saved to {output_file}")

    except Exception as e:
        print(f"Error reading tough_parameters {tough_parameters}: {e}")
    return string
        

# File containing strings to search
strings_file = 'parameters.txt'  
# Directory containing files to search
search_directory = 'Folder_Name'
# Output report
report_file = 'search_report.txt'
#complicated parameters that need manual checks
tough_parameters = "tough_parameters.txt"
#configs stored in a single page of all complicated DB
output_file = "outfile.txt"
# Directory containing files to search
directory = 'Twin Valley'

# Perform search
search_strings_in_directory(strings_file, search_directory, report_file)
find_and_extract(tough_parameters,directory,output_file)



