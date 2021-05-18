# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 04:37:23 2020

@author: Rebekah
"""
import keyboard, pyautogui, time, subprocess, os
active = pyautogui.getActiveWindowTitle()
active = pyautogui.getWindowsWithTitle(active)
active[0].minimize()
zoom_flag = 0 #assume zoom hasn't started yet
while zoom_flag == 0:
    zoom = pyautogui.getWindowsWithTitle('Zoom')
    if zoom == []:
        zoom_flag = 0
        time.sleep(5)
    else:
        for title in zoom:
            if title.title == 'Zoom': #if we can find zoom window
            #check for zoom
                zoom_flag = 1
                zoom2 = title
                break
            else: #if we can't find zoom window
                zoom_flag = 0
                time.sleep(5)
zoom = zoom2
#make sure obs and zoom are not maximised
re = pyautogui.confirm(text='Would you like to record your meetings?', title='Auto-Zoom: Initialisation', buttons=['Yes', 'No'])
if re == 'Yes':
    pyautogui.alert(text='Launch OBS and Zoom. Then, press OK', title='Auto-Zoom: Initialisation', button='OK')
    pyautogui.alert(text='Adjust the size of the OBS and Zoom windows so they do not overlap. Then, press OK', title='Auto-Zoom: Initialisation', button='OK')
    zoom = pyautogui.getWindowsWithTitle('Zoom')
    for title in zoom:
        zoom2 = title
    zoom = zoom2
    ## get size of zoom window
    z_tl = zoom.topleft 
    z_wd = zoom.width
    z_ht = zoom.height
    obs = pyautogui.getWindowsWithTitle('OBS')
    obs = obs[0]
    ## get size of obs window
    o_tl = obs.topleft 
    o_wd = obs.width
    o_ht = obs.height
    ## get coordinates of rec button
    while True:
        pyautogui.alert(text='Move your mouse pointer over "Start Recording" in OBS. Then, press "R"', title='Find "Start Recording" button', button='OK')
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('R'):  
                x, y = pyautogui.position()
                rec_button = [x,y]
                break   
    pyautogui.moveTo(rec_button)
    ## get coordinates of zoom join button
    while True:
        pyautogui.alert(text='Move your mouse pointer over "Join" in Zoom. Then, press "J"', title='Find "Join" button', button='OK')
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('J'):  
                x, y = pyautogui.position()
                join_button = [x,y]
                break  
    pyautogui.moveTo(join_button)
else:
    ## use default size of zoom window
    zoom = pyautogui.getWindowsWithTitle('Zoom')
    for title in zoom:
        zoom2 = title
    zoom = zoom2
    z_tl = zoom.topleft 
    z_wd = zoom.width
    z_ht = zoom.height
    ## get coordinates of join button
    while True:
        pyautogui.alert(text='Move your mouse pointer over "Join" in Zoom. Then, press "J"', title='Find "Join" button', button='OK')
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('J'):  
                x, y = pyautogui.position()
                join_button = [x,y]
                break 
    pyautogui.moveTo(join_button)
pyautogui.alert(text='Go to Settings, then General in Zoom.\nUncheck "Ask me to confirm when I leave a meeting".', title='Zoom Settings', button='OK')
zoom_dir = pyautogui.prompt(text='Input the directory that the Zoom.exe file is in. \nIt should look like this:C:\\\\Users\\\\Name\\\\AppData\\\\Roaming\\\\Zoom\\\\bin', title='Auto-Zoom: Initialisation', default='')
s = os.getcwd() + '\ini.txt'
f = open(s,"w+")
if re == 'Yes':
    f.write(str(rec_button[0])+ "\n")
    f.write(str(rec_button[1])+ "\n")
    f.write(str(o_tl[0])+ "\n")
    f.write(str(o_tl[1])+ "\n")
    f.write(str(o_wd)+ "\n")
    f.write(str(o_ht)+ "\n")
else:
    f.write('0'+"\n"+'0'+"\n"+'0'+"\n"+'0'+"\n"+'0'+"\n"+'0'+"\n")
f.write(str(join_button[0])+ "\n")
f.write(str(join_button[1])+ "\n")
f.write(str(z_tl[0])+ "\n")
f.write(str(z_tl[1])+ "\n")
f.write(str(z_wd)+ "\n")
f.write(str(z_ht)+ "\n")
f.write(str(zoom_dir)+'\\\\Zoom.exe')
f.close()

