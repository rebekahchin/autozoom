# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
######### --------HAVE OBS OPEN ------------- #############
import datetime, time, pyautogui, subprocess
## to wake screen; not unique, any hotkey will do
pyautogui.hotkey('shift') 
## fetch Command Prompt Windows to minimize it
active = pyautogui.getActiveWindowTitle() 
active = pyautogui.getWindowsWithTitle(active)
active[0].minimize()
## fetch button coordinates from ini.txt
with open('ini.txt','r') as coor:
    coors = coor.readlines()
coor.close()
rec_but = [int(coors[0]), int(coors[1])]
join_but = [int(coors[6]), int(coors[7])]
## fetch schedule
flag = 0
if flag == 0:
    ## open and parse schedule.txt file
    with open("schedule.txt", "r") as sch:
        sch_a = sch.readlines()
    sch.close()
    for line in sch_a[0]:
        sch = line.split()
    for line in sch_a:
        sch.append(line.split())      
    ## check curr time, class start time, meeting ID, pwd, class duration
    now = datetime.datetime.now()
    now_d = now.strftime('%A')
    now_h = int(now.strftime('%H'))
    now_m = int(now.strftime('%M'))
    now_day = int(now.strftime('%d'))
    now_mon = int(now.strftime('%m'))
    now_yr = int(now.strftime('%Y'))
    ## compares current time to schedule to determine if there's a class
    ## if yes, fetch end time, id, pwd
    for course in sch:
        if course[2] == now_d and int(course[3])==now_h:
            flag = 1
            m_id = course[8]
            ## To check if we should record
            if course[0] == 'N':
                rec_flag = 0
            else:
                rec_flag = 1
            #to determine if we need to enter a pwd
            if len(course)>9:
                m_pwd = course[9]
                pwd = 1 
            else:
                m_pwd = None
                pwd = 0                
            break
        else:
            flag = 0
if flag == 1:
    ## launch zoom
    subprocess.Popen(str(coors[12]))
    ## launch obs if necessary
    #if rec_flag == 1:
    #   subprocess.Popen(os.getcwd()+'\\obs.bat') 
    end_c = datetime.datetime(now_yr, now_mon, now_day, int(course[5]), int(course[6]))
    end_t = datetime.datetime(now_yr, now_mon, now_day, int(course[5]), 20)
    st_p5 = datetime.datetime(now_yr, now_mon, now_day, int(course[3]), int(course[4])+5)
    ## fetch zoom app window
    ## assume zoom hasn't started yet
    zoom_flag = 0 
    while zoom_flag == 0:
        zoom = pyautogui.getWindowsWithTitle('Zoom')
        if zoom == []:
            zoom_flag = 0
            time.sleep(2)
        else:
            for title in zoom:
                ## if we can find zoom app window
                if title.title == 'Zoom': 
                    zoom_flag = 1
                    zoom = title
                    break
    ## fix size of zoom app window
    zoom.topleft=(int(coors[8]),int(coors[9]))
    zoom.width=int(coors[10])
    zoom.height=int(coors[11])
    ## Start recording in OBS
    if rec_flag == 1:
        time.sleep(5)
        obs = pyautogui.getWindowsWithTitle('OBS')
        obs = obs[0]
        obs.activate()
        obs.topleft=(int(coors[2]),int(coors[3])) #fix size of obs window
        obs.width=int(coors[4])
        obs.height=int(coors[5])
        pyautogui.click(int(coors[4])-35,int(coors[5])-35)#select obs
        pyautogui.click(rec_but[0],rec_but[1])
    ## Join Zoom meeting
    zoom.activate()
    pyautogui.click(int(coors[8])+200,int(coors[9])+20) #select zoom window
    pyautogui.click(join_but[0],join_but[1]) #select "join"
    ## Check if ID window is open
    zoomid_flag = 0 
    while zoomid_flag == 0:
        zoomid = pyautogui.getWindowsWithTitle('Zoom')
        ## ID window not open yet
        if len(zoomid) == 1:
            zoomid_flag = 0
            time.sleep(2)
        ## ID window is open
        else:
            zoomid_flag = 1
            break
    pyautogui.write(m_id)
    pyautogui.write(['\t', '\t','\t','\t','\t','\n'],0.25)
    if pwd==1:
        zoompwd_flag = 0 
        while zoompwd_flag == 0:
            zoompwd = pyautogui.getWindowsWithTitle('Enter meeting passcode')
            if zoompwd == []:
                zoompwd_flag = 0
                time.sleep(2)
            else:
                for title in zoompwd:
                    ## if we can find zoom app window
                    if title.title == 'Enter meeting passcode': 
                        zoompwd_flag = 1
                        break
        pyautogui.click(1136,450)
        pyautogui.write(m_pwd)
        pyautogui.write(['\t','\n'],0.25)
    while datetime.datetime.now() < end_t:
        time.sleep(60)
    ## Assume that the class is still on, past the end time
    while datetime.datetime.now() > end_t and datetime.datetime.now() < end_c: 
        ##find meeting window
        meet = pyautogui.getWindowsWithTitle('Zoom Meeting')
        ## if meeting is over
        if meet == []:
            ## close obs
                if rec_flag == 1:
                    obs.activate()
                    pyautogui.click(rec_but[0],rec_but[1]) 
                    #obs.close()
                ## close zoom app
                zoom.close()
                quit()
        ## assume meeting isn't over
        else:
            time.sleep(30)                
    ## if host hasn't left, we end the recording and leave the meeting
    while datetime.datetime.now() > end_c: 
        meet = pyautogui.getWindowsWithTitle('Zoom Meeting')
        ## if meeting is over, end recording, close zoom app
        if meet == []:
            if rec_flag == 1:
                obs.activate()
                pyautogui.click(rec_but[0],rec_but[1]) 
            zoom.close()
            quit()
        ## if meeting isn't over, force close meeting and obs
        else:
            for tle in meet:
                ##if we can find meeting window
                if tle.title == 'Zoom Meeting': 
                    meet = tle
            meet.close()
            if rec_flag == 1:
                obs.activate()
                pyautogui.click(rec_but[0],rec_but[1]) 
            zoom.close()
            quit()      
quit()
