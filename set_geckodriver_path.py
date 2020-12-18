import os
import sys
import platform

def get_os_version():
    return platform.system()


def add_geckodriver_to_PATH():
    current_path = os.getcwd()
    geckodriver_path = os.path.join(current_path, "geckodriver-v0.28.0-linux64")

    print("PATH before:")
    print(os.environ["PATH"])

    if get_os_version() == "Linux":

        print("Linux detected platform.")

        if geckodriver_path in os.environ["PATH"]:
            print("Geckodriver already in PATH.")
        else:
            os.environ["PATH"] += os.pathsep + geckodriver_path
            print("Geckodriver added in PATH.")

    elif get_os_version() == "Windows":
        print("Windows not yet available.")

    else:
        print("OS not yet available.")

    print("PATH after:")
    print(os.environ["PATH"])


 


 