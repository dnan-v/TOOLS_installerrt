import os
import time
os.system("chmod +x install-ubuntu.py")
os.system("sudo apt-get install python3")
time.sleep(2)
os.system("sudo apt-get install python2")
time.sleep(2)
os.system("sudo apt-get install pip")
time.sleep(2)
os.system("pip install faker")
os.system("pip install time")
time.sleep(2)
os.system("pip install logging")
os.system("sudo apt-get install banner")