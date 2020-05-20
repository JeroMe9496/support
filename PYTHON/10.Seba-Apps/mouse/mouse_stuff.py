from pynput.mouse import Button, Controller
from time import sleep
import os

mouse = Controller()

print ("Forcing cursor to stay in an invisible box in the center of the screen")
print ("Close console to end process... (if you can)")

while(1):

	# Defining and updating variables for positions
	pos = mouse.position
	posx = pos[0]
	posy = pos[1]

	# Method used to move the mouse 			# Uses the pynput lib
	# This doesn't care where the mouse is, it will increment it based on it's current position
	## mouse.move(10, 10)

	# Whereas this sets its position
	## mouse.position = (50, 50)

	# Rebound mouse inside of box
	if posx < 860:
		mouse.move(10, 0)
	elif posx > 1060 :
		mouse.move(-10, 0)

	if posy < 440:
		mouse.move(0, 10)
	elif posy > 640 :
		mouse.move(0, -10)

	# Sets an interval of seconds between loops 	# Uses the time lib
	## sleep(0.01)
	
	# Printing current mouse position
	## print(mouse.position)

## os.system("pause")