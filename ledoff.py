import time
import os

os.system("sudo bash -c \"echo none > /sys/class/leds/led/trigger\"")
os.system("sudo bash -c \"echo 0 > /sys/class/leds/led0/brightness\"")
os.system("sudo bash -c \"echo 0 > /sys/class/leds/led1/brightness\"")
