import winapps
import psutil


namesList = []                                          # ordered list will be used to keep track of all the apps
for i in winapps.list_installed():
    namesList.append(i.name)                     # add all installed app names (formatted) to the list
    print(str(i.install_location) + "\t\t\tname: " + i.name)

# use winapps to get the names
# using the names, get the install path
# in the install path, one folder down, search for all .exe
# store said .exe names in the list
# check for running processes. if a process matches with the list "to turn off", kill the process
# use timer to check the processes (once a min)




while 1:
    for proc in psutil.process_iter():
        x = 5