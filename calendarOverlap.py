import argparse  # arguments parsing
import os  # get name of file

""" calendarOverlap.py : Check if activities are overlapping in a calendar and if a bouquet of activities will induce overlapping. """

__author__ = "Matvei Pavlov"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "surname.lastname@etu.univ-grenoble-alpes.fr"

dayValue = {}
confValues = {}
inputFile = ""

def args():
	"""Arguments parsing 

	Returns:
		list: every arguments
	"""
	parser = argparse.ArgumentParser(description='Check if a set of weekly activities would overlap if put together.')
	parser.add_argument('-n', '--newactivity', help='Add an activity to the list.', required=False, action='store', nargs=4)
	parser.add_argument('-r', '--remove', help='Remove an activity from the list.', required=False, action='store', nargs=1)
	parser.add_argument('-i', '--input', help='Use as input another config file (default is .calConfig)', required=False, action='store', nargs='?', default=".calConfig")
	parser.add_argument('-s', '--show', help='Show the config data and current overlapping activities', required=False, action='store_true')
	parser.add_argument('-c', '--checkOverlap', help='Check if the activities given as arguments overlap with each other', required=False, action='store', nargs='+')
	return parser.parse_args()

def addDay(name):
	"""Add a day to the dayValue dictionnary and link it to a value if it is not yet in the dictionnary

	Args:
		name (str): Day to be added
	"""
	if name not in dayValue :
		if not dayValue : # if dictionnary is empty
			dayValue[name] = 0
		else: # value is biggestValue+10 000
			last_key = list(dayValue)[-1]
			nextValue = int(dayValue[last_key])+10000
			dayValue[name] = nextValue

def hourToTime(hourFormat):
	"""Converts a HH:MM format to an integer

	Args:
		hourFormat (Hour)): Hour in the format of HH:MM. /!\ 0 must be precised, XX:00 or 00:XX

	Returns:
		int: HH*60+MM
	"""
	values = hourFormat.split(':')
	return int(values[0])*60 + int(values[1])

def loadConfig():
	"""Read the config file and put values in global variables
	"""
	with open(inputFile, 'r') as file :
		for line in file :
			current = line.rstrip().split('|')
			day = current[1].lower()
			addDay(day)
			minValue = hourToTime(current[2])+dayValue[day]
			maxValue = hourToTime(current[3])+dayValue[day]
			confValues[current[0]]=[minValue, maxValue]

def addActivity(arguments):
	"""Add a new Activity to the config file

	Args:
		arguments (list): list containing [<name>, <day>, <startHour>, <endHour>]
	"""
	if arguments[0] in confValues:
		print("Error : Activity already exists. Please delete it using\n   python {} -d {}".format(os.path.basename(__file__),arguments[0]))
		exit(1)
	if hourToTime(arguments[2]) > hourToTime(arguments[3]):
		print("Error : Activity ends before it starts")
		exit(1)
	toAdd = "{}|{}|{}|{}\n".format(arguments[0],arguments[1],arguments[2],arguments[3])
	with open(inputFile, "a") as file :
		file.write(toAdd)

def removeActivity(activity):
	"""Remove activity from the config file

	Args:
		activity (str): name of the activity to remove. /!\ Case sensitive !
	"""
	lines = []
	with open(inputFile, 'r') as file :
		for line in file:
			lines.append(line.rstrip().split('|'))
	with open(inputFile, 'w') as file :
		for line in lines :
			if line[0] != activity:
				file.write("{}|{}|{}|{}\n".format(line[0], line[1], line[2], line[3]))


def overlapsFormat(name1, name2):
	"""Makes a sorted tuple (in list) with two strings

	Args:
		name1 (str): first string
		name2 (str): second string

	Returns:
		list: sorted tuple of the args
	"""
	if name1>name2 :
		tup= [name1, name2]
	else : 
		tup=[name2, name1]
	return tup

def checkOverlaps():
	"""Calculate the overlapping activities from the config file

	Returns:
		list: Every tuple of overlapping activities
	"""
	# This is optimizable, because I check key1 - key2 and key2 - key1
	overlaps = []
	for key, value in confValues.items() :
		for key2, value2, in confValues.items():
			# check if they are not overlapping : 
			if key != key2 :
				if value[0] >= value2[1] or value[1]<=value2[0]:
					overlap=False
				else :
					overlap=True
					tup = overlapsFormat(key, key2)
					if tup not in overlaps:
						overlaps.append(tup)
	return overlaps

def showValues():
	"""Proints the content of the config file and the overlapping activities
	"""
	print("Content of the config File ({}) :".format(inputFile))
	with open(inputFile, 'r') as file:
		for line in file :
			current = line.rstrip().split('|')
			print("| - {} : {}, {}, {}".format(current[0], current[1], current[2], current[3]))
	overlaps = checkOverlaps()
	print("Overlapping Activities : ")
	for tup in overlaps : 
		print("| - {} ; {}".format(tup[0], tup[1]))

def areThereOverlaps(arguments):
	"""Check if the arguments contain two overlapping activities, and print them if they does

	Args:
		arguments (list): a list of arguments to be checked
	"""
	if len(arguments) != 1 :
		# well, that's not very effective, huh
		overlaps = checkOverlaps()
		overlapingTuples = []
		for activity in arguments :
			for activity2 in arguments :
				if activity != activity2:
					tup = overlapsFormat(activity, activity2)
					if tup in overlaps :
						if tup not in overlapingTuples:
							overlapingTuples.append(tup)
		print(overlapingTuples)

args = args()
inputFile = args.input
if not os.path.exists(inputFile):
	f = open(inputFile, "w+")
	f.close()

if args.newactivity :
	loadConfig()
	addActivity(args.newactivity)
if args.show :
	loadConfig()
	showValues()
if args.remove :
	removeActivity(args.delete[0])
if args.checkOverlap :
	loadConfig()
	areThereOverlaps(args.checkOverlap)