import os
import csv

def structurize():
	# initialize the file structure in case it doesn't exist
	os.mkdir("data", exist_ok=True)
	if not os.path.exists("data"+os.path.sep+"memory.csv"):
		with open("data"+os.path.sep+"memory.csv", "w") as f:
			file = csv.writer(f)
			file.writerow(["id", "cooldown", "proficiency", "subject", "chapter"])
	os.makedirs("data"+os.path.sep+"etc", exist_ok=True) # uncatagorized subject
	ls: list[str] = os.listdir("data")
	for i in ls:
		if os.path.isdir("data"+os.path.sep+i):
			os.mkdir("data"+os.path.sep+i+os.path.sep+"etc", exist_ok=True) # uncatagorized chapter

