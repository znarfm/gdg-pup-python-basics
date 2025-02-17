import os

# Get the script's current directory
curr_dir = os.path.dirname(os.path.abspath(__file__))


def open_sample():
    file_path = os.path.join(curr_dir, "sample.txt")

    # Open a file for reading.
    try:
        with open(file_path, "r") as file:
            # Read the contents of the file.
            lines = file.read()
            # Display the contents of the file.
            print(f"Contents of the file:\n{lines}")
    except FileNotFoundError as e:
        print(e)


# Optionally, create a new file and write some content to it.
def create_new():
    file_path = os.path.join(curr_dir, "newfile.txt")
    try:
        with open(file_path, "w") as file:
            file.write("This is a new file, like New Year New Me XD")
    except FileExistsError:
        print("File already exists. Reading it now instead.")
    read_new()


def read_new():
    file_path = os.path.join(curr_dir, "newfile.txt")

    with open(file_path, "r") as file:
        lines = file.read()
        print(f"New file created with content:\n{lines}")


def main():
    open_sample()
    print()
    create_new()


if __name__ == "__main__":
    main()
