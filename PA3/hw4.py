#Assignment 4
import sys
import build_data
import hw3

#type "python3 hw4.py operations.txt" into command line to run

# Build an array of all of the demographic objects in the full data file
data_mod = build_data.get_data()

#Checks if the user added a file as a parameter in the command line
if len(sys.argv) == 1:
    raise FileNotFoundError

#Opens the operations file that was sent as a parameter
file1 = open(sys.argv[1], "r")
#Reads each line in the parameter
for line in file1.readlines():
	#Since each word/command is split by a ":" in the operations file, create an array
	#That will store the name of each command as a string
    filters = line.strip().split(":")
    for i in range(0, len(filters)):
		#Loops through each command per line
		#Checks if the command is "display"
        if filters[i] == "display":
		#Prints each demographic object to the screen
            for item in data_mod:
                sys.stdout.write(repr(item))
		#Checks if the command is "filter-state"
        elif filters[i] == "filter-state":
            i += 1
		#The next word in the commandline will be the state abbreviation like "CA"
		#Calls function from hw3
            data_mod = hw3.filter_by_state(data_mod, filters[i])
		#Check for if there are no demographic objects that align with that state
            if len(data_mod) == 0:
                sys.stdout.write("Filter: state == ")
                sys.stdout.write(filters[i])


file1.close()
