# Android Debloater.
# Python script to remove all bloatware applications from android.

import os
import json
import config
import platform
from tkinter import filedialog


# Function for writing statements to debloater file.
def append_to_file(file_name, content):
    with open(file_name, "a") as out_file:
        out_file.write(content)


current_platform = platform.system()
debloater_configs = config.platform_config.get(current_platform)
debloater_out_file = debloater_configs.get("OutputFile")
debloater_pause_command = debloater_configs.get("PauseCommand")

# Remove debloater file if already exist.
if os.path.exists(debloater_out_file):
    os.remove(debloater_out_file)

# Open the json file containing package name list.
unwanted_package_file_path = filedialog.askopenfilename(
    initialdir=os.getcwd(), title="Select the json file containing unwanted packages"
)

unwanted_packages_content = open(unwanted_package_file_path, "r")
unwanted_packages_dic = json.load(unwanted_packages_content)

debloat_command_list = [
    "adb shell pm uninstall -k --user 0 {}".format(package_name)
    for package_name in unwanted_packages_dic.get("Packages")
]

# Debloater script.
debloater_script = "\n".join(debloat_command_list)

append_to_file(debloater_out_file, debloater_script)
append_to_file(debloater_out_file, debloater_pause_command)

# Execute the script.
os.system(debloater_out_file)

print("Debloater executed successfully.")
