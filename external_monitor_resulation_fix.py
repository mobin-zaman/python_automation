import subprocess
import os

# getting cvt output
out = subprocess.Popen(['cvt', '1366', '768'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# getting the first element of the tuple, decode is necessary to remove b'
cvt_output = (out.communicate()[0].decode("utf-8"))

print("cvt output")
print(cvt_output)
print()

# splitting on the basis of '\n' and taking the second item
result = cvt_output.splitlines()[1]

print("resultant string")
print(result)
print()

# cutting the result properly

new_mode = result[9:]

print("New Mode")
print( new_mode)
print()


os.system("sudo xrandr --newmode " + new_mode)
os.system("sudo xrandr --addmode VGA-1 1368x768_60.00")
os.system("xrandr --output VGA-1 --mode 1368x768_60.00 --pos 1376x0 --rotate normal --output eDP-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-3 --off --output HDMI-2 --off --output HDMI-1 --off --output DP-3 --off --output DP-2 --off --output DP-1 --off")
