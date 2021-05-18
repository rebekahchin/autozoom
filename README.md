# autozoom
Automate and record your Zoom meetings

## Who is this for?
*autozoom* was created to automatically join and record my university classes that were held on Zoom. While my professors did upload the Zoom recordings a few hours after the class ended, I found the audio quality to be lacking. Therefore, this program is most useful if you have Zoom meetings that repeat at a fixed time each week (or every other week) and do not require your participation.\
\
Note: This program works best on computers that have wake timers enabled. \
Go to **Power Options>Edit plan settings>Change advanced power settings>Sleep**. \
If you do not see the option **Allow Wake timers**, then your computer manufacturer does not allow users to enable wake timers. You can attempt to circumvent this by enabling it in the Registory Editor. However, this method did not work for me, and I simply used another computer that allowed users to enable wake timers. 

## How does it work?
*autozoom* relies on OBS Studio to record your computer screen and audio. Therefore, you would not need permission from the Zoom host to record the meeting. After the meeting is over, the recording would be saved on your computer, not the Zoom servers, and would not be further compressed as Zoom cloud recordings are. This program will join any number of meetings based on the information stored in *schedule.txt*.

## Prerequisites
* Windows 10 (due to the usage of batch files and Task Scheduler)
* Zoom
* [OBS Studio](https://obsproject.com/download)
* Python 3.6 and above
* Python packages:
  * datetime
  * time
  * pyautogui
  * subprocess

## Initial Setup
* Install the python packages
  * Open command prompt (**shift+right-click>select "Open powershell here"**) in the directory where *python.exe* is located
  * Run the following commands:
      
        pip install datetime
        pip install time
        pip install pyautogui
        pip install subprocess
      
* Launch Zoom, and log-in 
* Launch OBS
* Run *calibrate.py* with a python compiler
* Run *autozoom.py* at scheduled times with Task Scheduler (*taskschd.msc*)

## Using a batch file to run automate_zoom.py at a scheduled time
### Editing the .bat file
Open *autozoom.bat*. You will then see the following:

    cd "**directory containing the .py script**"
    **directory containing the python program** autozoom.py
    
Replace the asterisks and the text in the asterisks with your own directory locations, save and close the file.\
Note: The directory locations should look like *C:\Users\\...*

### Setting up Task Scheduler
1. Create a task
2. In **General**:
   * Give it a name, e.g. autozoom
   * Select **Run whether user is logged on or not**
   * Select **Run with highest privileges**
   * Select **Configure for: Windows 10**
3. In **Triggers**:
   * Configure the trigger times based on your scheduling needs
4. In **Actions**:
   * Select **Start a program**
   * Navigate to the autozoom folder and select *autozoom.bat*
5. In **Conditions**:
   * Select **Wake computer to run this task**
6. In **Settings**:
   * Select **Allow task to be run on demand**
   * For **If the task is already running, ...:**, select **Stop existing instance**
7. Select **OK** to save the task.
8. Input your Windows password when prompted
 
### (Optional) Turn off password log-in on wake
Navigate to **Settings>Lock screen>Screen saver settings**.\
Then, uncheck **On resume, display log-on screen**
 
### Specifying the meeting ID, password, and start and end time
1. Open *schedule.txt*
2. You will then see the following, which is an example of how the meeting information is formatted:

   > R STATS Wednesday 10 30 12 20 110 123456789 password
 
   Delete this example and replace it with your meeting \
   There are 10 entries seperated by (white)spaces \
   The formatting is as follows:
   * The first entry is either **R** or **N**. **R** for recording, **N** for no recording. Type **R** if you want the meeting to be recorded and **N** if you do not.
   * The second entry is the name of the meeting, and cannot contain spaces
   * The third entry is the day the meeting is held. Do not use abbreviations.
   * The fourth entry is the hour the meeting starts in the 24-hour format
   * The fifth entry is the minute the meeting starts
   * The sixth and seventh entry is the hour and minute the meeting ends, and are in the same format as the fourth and fifth entry.
   * The eigth entry is the length of the meeting in minutes
   * The ninth entry is the meeting ID, with spaces removed
   * The last entry is the meeting password. If your meeting does not have one, leave this entry blank
3. Use a new line for each meetings you'd like scheduled
4. Save the file
    
