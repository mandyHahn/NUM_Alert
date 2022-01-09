Contributors: Uladzislau Kaparykha, Amanda Hahn, Nicholas Waller
Hackathon Team Name: N.U.M

General Purpose:
The general purpose of this program is to keep workers more on task during their work day.
There are 4 categories, "Recurring Alerts", "Timed Alerts", "Restrictions", and "Extras"
"Recurring Alerts" are alerts that happen every given period of time.
"Timed Alerts" are alerts that happen once a day at a given time
"Restrictions" are restrictions you can place on your applications. This will be checked every minute.
"Extras" are extras for the program (currently only a COVID case counter)

Setup:
  - Make sure Chromium driver is updated to the version 97.0 or later. To do so:
    1. Open Google Chrome
    2. Click on the 3 dots in the top-right corner of the screen
    3. In the help subsection, click on the `About Google Chrome`
    4. If the version is not 97.0 onward, click the update button.
<br>
Install following library dependencies via `pip install ___`, where ___ are the libraries mentioned below:
<br>
  - PyQt5
  - selenium
  - psutil
  - winapps
  - win10toast
  To launch the app (assuming you are in the directory containing all the files)
  > py main.py


Using Each Aspect:
Recurring Alerts
 - Alert type: The type of alert. If the type of alert wanted is not on the list, press "custom".
 - Frequency Duration: The amount of time, in minutes, that the notification will appear.
 - Custom Message: The message that will appear on the alert.
 - Notification Duration - How long the notification will stay on screen (see the 2nd limitation/restriction)
 Once the user is happy with all values entered, press "Add Alert"
 If the user wants to delete the alert, click on the alert to delete and then press the "Delete Selected Alert" button.
Timed Alerts
 - Alert type, custom message and notification duration are all the same as above.
 - Time to Occur: The time at which the notification will occur. It only checks the second the minute starts (eg checks at 12:00:00, but won't at 12:00:54)
 Add alert and delete alert are the same as above.
Restrictions
 - Click on the program that you want to be restricted.
 - Click "add to banned"
 - Click on an in the "banned applications" text box and then "unban selected" to unban the item
 - Once all banned applications are ready, check the "focus mode" box to close the applications every minute.
Extras
 - COVID-19 Alerts
   - Click on the "Receive COVID case alerts" radio button
   - "Notify every" - How often the notifications will appear
   - "Country" - The country that you will be checking statistics for. Only the top 30 countries, by case count, are listed.
   - Notification Duration - How long the notification will be on screen.
 The numbers are consistently updated using a webscraper. All information should be accurate and up-to-date.
 All information comes from https://www.worldometers.info/coronavirus/

Limitations/Restrictions:
Windows 10 Exclusive due to how the notifications are processed.
Notification duration is limited not only by the input, but by what the limit is in the user settings.
 - In Windows 10, this can be changed in settings -> Ease of Access -> Show notifications for
If the installation path does not exist, then the program can not be prevented from being closed.
 - An example program is steam, however steam applications can regularly be closed
Depending on the selected programs, unsaved changes will be ignored. The user will not be prompted to save beforehand.
Some programs, in their install path, have extra .exe files, such as UnityCrashHandler.exe.
 - If another unrelated app also uses UnityCrashHandler, it will also be closed.
Upon adding an item to the "banned" list, it will not automatically be closed. "Focus mode" must be turned on.
Restricted programs will only be shut down on a timer of 1 minute to prevent resource hogging. In theory, the program may still be opened.
The amount of "notification time" MAY NOT exceed "time". Meaning, you CAN NOT create 2 alerts that happen every minute that each last 59 seconds without breaking the program.
The COVID cases runs in headless mode, which has been known to be unreliable.
Chrome Version 97.0.4692.71 (the most recent version) is needed.
 - To update, open Google Chrome. Press the 3 buttons in the top right of the screen. Click "help", then "About Google Chrome". The update should automatically start installing if needed.

