import winapps
import os
import psutil
import signal
import sched, time

namesList = []  # ordered list will be used to keep track of all the apps. will be populated via InstalledApp.name
toKill = []     # combobox selected items will go into this list

exeDict = {}    # hashmap of name->list of executables
exeList = []    # after toShutdown list was given, merge all lists matching items in toShutdown

s = sched.scheduler(time.time, time.sleep)

def find_items(search_path):
    result = []
    search_path = search_path.replace("\"", "")    # path might contain double quotes, bad
    try:
        itemsList = os.listdir(search_path)         # some paths have cursed chars, can't follow said path
    except FileNotFoundError:
        return []                                   # if that happens, return empty list

    for currItem in itemsList:                      # all files in the destination were found, must check for .exe
        if '.exe' in currItem:                      # assume .exe file was found
            result.append(currItem)                 # add said item to the list to be returned
    return result


def kill_unwanted(sc):
    for proc in psutil.process_iter():  # psutil.processor_iter() created iterator for the for_each loop to go through
                                        # contains every current runing process with it's name and PID
        for i in exeList:               # for every .exe to kill
            if proc.name() == i:        # if the process name matches the kill .exe
                os.kill(proc.pid, signal.SIGTERM)   # terminate teh program
    s.enter(60, 1, kill_unwanted, (sc,))



for i in winapps.list_installed():
    if not(i.install_location is None or i.install_location == ''):
        namesList.append(i.name)                     # add all installed app names (formatted) to the list
        print(i.name)
        exeDict[i.name] = find_items(str(i.install_location))   # add to hashmap name->list of .exe

for i in toKill:                # not mandatory, but performance improvement
    exeList += exeDict[i]       # given toKill list, merge matching dict entries, O-notation is smaller

s.enter(60, 1, kill_unwanted, (s, ))
s.run()
# use winapps to get the names
# using the names, get the install path
# in the install path, one folder down, search for all .exe
# store said .exe names in the list
# check for running processes.
# if a process matches with the list "to turn off", kill the process

# use timer to check the processes (once a min)

