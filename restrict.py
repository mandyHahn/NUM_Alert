import winapps
import os
import psutil
import signal

# find_items: given a search path it returns a list of all .exe files in the folder
# search_path - folder to search
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

# kill_unwanted: given a list of executables, kills all of them if they are running
# exe_list - a list of executables to be executed
def kill_unwanted(exe_list):
    for proc in psutil.process_iter():  # psutil.processor_iter() created iterator for the for_each loop to go through
        for i in exe_list:               # for every .exe to kill
            if proc.name() == i:        # if the process name matches the kill .exe
                os.kill(proc.pid, signal.SIGTERM)   # terminate teh program

# setup_apps: to be run at the beginning of the program, creates a dictionary for all the apps and their executable names
# names_list - list of applications
# exe_dict - the dictionary to be filled
def setup_apps(names_list, exe_dict):       # will run on startup of the app
    for i in winapps.list_installed():      # for every installed app
        if not(i.install_location is None or i.install_location == ''):  # make sure the path is not empty
            names_list.append(i.name)                     # add installed app name (formatted) to the list
            exe_dict[i.name] = find_items(str(i.install_location))   # add to hashmap (name->list of .exe)
