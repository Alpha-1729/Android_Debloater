# Debloater Android

"""
>>>> Script to remove the unwanted application from the android.
>>>> Steps:
         Add the package name of the unwanted apps into the txt file.
         Then run the python file using the Run.bat file.
         In linux please run the Program.py file.
         After running the script:
            Batch file for windows and bash file for linux will be created in the current folder.
            Just run the run the script after enabling the USB debugging in the android.
>>>>
>>>>
>>>>
>>>>
>>>>
"""
import os

debloater_windows_loc = "debloater_windows.bat"
debloater_linux_loc = "debloater_linux.sh"

# Remove debloater file for windows.
if os.path.exists(debloater_windows_loc):
    os.remove(debloater_windows_loc)

# Remove debloater file for linux.
if os.path.exists(debloater_linux_loc):
    os.remove(debloater_linux_loc)
    

# Function for writing the script to debloater file.
def append_to_file(file_name, content):
    with open(file_name, "a") as out:
        out.write(content)

# Read all package name from the txt file.  
with open("unwanted_package_name.txt", "r") as bloatware:
    package_name_list = bloatware.readlines()

# Adding the command to uninstall the bloatware to debloater_file.
for package_name in package_name_list:
    uninstall_command = "adb shell pm uninstall -k --user 0 {}".format(package_name)
    append_to_file(debloater_windows_loc, uninstall_command)
    append_to_file(debloater_linux_loc, uninstall_command)


append_to_file(debloater_windows_loc, "\npause")






