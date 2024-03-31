import os

def read_text_files(directory_path):
    """
    Reads all .txt files in the specified directory and returns their contents as a list of strings.

    :param directory_path: The path to the directory containing .txt files
    :return: A list of strings where each string is the content of a .txt file
    """
    txt_contents = []
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        return txt_contents

    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # Check for .txt extension
        if filename.endswith(".txt"):
            # Construct full file path
            file_path = os.path.join(directory_path, filename)
            # Open and read the contents of the file
            try:
                with open(file_path, 'r') as file:
                    txt_contents.append(file.read())
            except IOError as e:
                print(f"Failed to read file {filename}: {e}")

    return txt_contents
