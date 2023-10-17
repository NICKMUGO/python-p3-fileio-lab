def write_file(file_name, file_content):
    file_name = f"{file_name}.txt"
    with open(file_name, mode="w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_name = f"{file_name}.txt"
    with open(file_name, mode="a") as file:
        file.write(append_content)


def read_file(file_name):
    file_name = f"{file_name}.txt"
    try:
        with open(file_name, mode="r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found"
    
file_name ="test_file"
file_content = "This is a test content."
append_content = "\nAppended content."
write_file(file_name, file_content)
append_file(file_name, append_content)