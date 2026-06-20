import subprocess
import os
source = input("file source plz: ")
destination = input("file destination plz: ")
folder = os.path.basename(source)
parent = os.path.dirname(source)
tar_name = f"{folder}.tar"
try:
    subprocess.run(["tar", "-cf", tar_name, "-C", parent, folder], check=True)
    subprocess.run(["rsync", "-ah", "--progress", tar_name, destination], check=True)
    subprocess.run(["tar", "-xvf", tar_name, "-C", destination], check=True)
    subprocess.run(["rm", "-f", tar_name], check=True)
    subprocess.run(["rm", "-f", f"{destination}/{tar_name}"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error during step: {e}")