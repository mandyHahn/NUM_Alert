import winapps
import os
import psutil
import signal


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


def kill_unwanted(exe_list):
    for proc in psutil.process_iter():  # psutil.processor_iter() created iterator for the for_each loop to go through
        for i in exe_list:               # for every .exe to kill
            if proc.name() == i:        # if the process name matches the kill .exe
                os.kill(proc.pid, signal.SIGTERM)   # terminate teh program


def setup_apps(names_list, exe_dict):       # will run on startup of the app
    for i in winapps.list_installed():      # for every installed app
        if not(i.install_location is None or i.install_location == ''):  # make sure the path is not empty
            names_list.append(i.name)                     # add installed app name (formatted) to the list
            exe_dict[i.name] = find_items(str(i.install_location))   # add to hashmap (name->list of .exe)


# use winapps to get the names
# using the names, get the install_path
# in the install_path, one folder down, search for all .exe
# store said .exe names in the list
# check for running processes.
# if a process matches with the list "to turn off", kill the process

# use timer to check the processes (once a min)
