from pynput.keyboard import Key, Controller
import time
import subprocess

# Password
pass = "1 Lik3 Che3Se"

# For example: \Riot Games\League of Legends\LeagueClient.exe
subprocess.Popen(['\Riot Games\League of Legends\LeagueClient.exe'])

# Wait untill client is fully launched so 
# we can star typing the password field.
# This value can (should) be modified to fit
# your personal timing.
time.sleep(5.5)  

keyboard = Controller()

# Type password
for a in pass:
	keyboard.press(a)
	keyboard.release(a)

time.sleep(0.5)

# Press enter
keyboard.press(Key.enter)
keyboard.release(Key.enter)
