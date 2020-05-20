from graphics import *

def main():

	win = GraphWin("Things of stuff", 500, 500)
	
	# Drawing a point
	p = Point(100, 50)
	p.draw(win)
	
	# Drawing a rectangle
	rect = Rectangle(Point(20, 10), Point(30, 30))
	rect.draw(win)
	
	# Waiting for mouse click to close
	win.getMouse()
	win.close()
		
main()