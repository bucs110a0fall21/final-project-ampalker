#import your controller
from src import controller
#<<<<<<< HEAD

def main():
	team = {"lead":"Paul Ampadu","backend":"John Paul Alker", "frontend":"Paul Ampadu"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:", team["frontend"])


	g1 = controller.Controller()
	g1.mainloop()

	#Create an instance on your controller object
	#Call your mainloop
	
	###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
main()
#>>>>>>> 7a3fab0d84ea3e3ee8ebdbca0b05e928a277d3cd
