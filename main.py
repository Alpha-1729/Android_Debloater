# Debloater Android

"""
>>>> Script to remove the bloatware from the android.
>>>>
>>>>
>>>>
>>>>
>>>>
"""

import os
import platform
from tkinter import filedialog

debloater_file_info_dic = {
    "Windows": ["debloater.bat", "\npause"],
    "Linux": ["debloater.sh", "\n"]
}

# Function for writing the script to debloater file.
def append_to_file(file_name, content):
    with open(file_name, "a") as out_file:
        out_file.write(content)

debloater_info = debloater_file_info_dic.get(platform.system())
debloater_file = debloater_info[0]
debloater_final_command = debloater_info[1]

package_file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select the package file")

# Remove debloater file if already exist.
if os.path.exists(debloater_file):
    os.remove(debloater_file)

# Read all package name from the package file.
with open(package_file, "r") as bloatware:
    package_name_list = bloatware.readlines()

# Debloater script.
debloat_command_list = ["adb shell pm uninstall -k --user 0 {}".format(package_name) for package_name in package_name_list]
debloat_script = "".join(debloat_command_list)

append_to_file(debloater_file, debloat_script)
append_to_file(debloater_file, debloater_final_command)

os.system(debloater_file)
