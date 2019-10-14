# DEPRECATED
This repository is not being updated anymore as the new LoL launcher already has a "Keep me signed in" option.

<former description>
 
# League of Legends Auto Logger

Auto logging for League of Legends client written in python3.  
You must have your username set and make sure "Remember Me" is checked.

![example of use](https://i.imgur.com/ZOIwkzK.gif)
----------

## HowTo
*You need to have python 3 installed in your system.* [*'How to' for Windows*](https://docs.python.org/3/using/windows.html).

Once you've done that:  
 **1.** Open a cmd and execute: `pip3 install pynput`  
 **2.** Now edit **lolauth.py** following instructions there.  
 *--- Next steps are not necessary but they make it easier to launch everything from just a shortcut.  
 Otherwise, you would have to open a cmd every time and type `python lolauth.py` which kinda sucks.---*  
 **3.** Place both **lolauth.py** and **lolauth.bat** wherever you want in your system but make sure they are in the same folder.  
 **4.** Make a shortcut of **lolauth.bat**. If you ever move the files, make sure to repeat this and next steps.  
 **5.** Right click the shortcut > *Properties*. Add **"C:\Windows\System32\cmd.exe /C "** *(without quotes)* to **Target**'s field.  
 **6.** Rename the shortcut to whatever you want but make it end in **.exe**.   
 **7.** You can now drop it to your taskbar or your desktop and execute it by clicking.  
 **8.** ***Get out of silver!***  

----------

## Content of files  
**lolauth.py:**  
> Opens the LoL launcher, types your password and signs in.  

**lolauth.bat:**  
> Executes lolauth.py
