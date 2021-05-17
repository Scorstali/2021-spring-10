F = input() 
M = input()
S = input()

if F == "scissors" and M == "paper" and S == "paper":
	print ("F")
elif F == "paper" and M == "rock" and S == "rock":
	print ("F")
elif F == "rock" and M == "scissors" and S == "scissors":
	print ("F")
elif M == "scissors" and F == "paper" and S == "paper":
	print ("M")
elif M == "paper" and F == "rock" and S == "rock":
	print ("M")
elif M == "rock" and F == "scissors" and S == "scissors":
	print ("M")
elif S == "scissors" and M == "paper" and F == "paper":
	print ("S")
elif S == "paper" and M == "rock" and F == "rock":
	print ("S")
elif S == "rock" and M == "scissors" and F == "scissors":
	print ("S")
else:
	print ("?")
