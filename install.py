import launch
import os

# Construct the path to the requirements.txt file in the video2video folder inside the extensions folder
req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "extensions", "video2video", "requirements.txt")

# Open the requirements.txt file
with open(req_file) as file:
    # Iterate through each line (library) in the requirements.txt file
    for lib in file:
        # Remove any leading/trailing whitespace from the library name
        lib = lib.strip()
        # Check if the library is not already installed
        if not launch.is_installed(lib):
            # Install the library using pip and display a message indicating the purpose of the installation
            launch.run_pip(f"install {lib}", f"video2video requirement: {lib}")
