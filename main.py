import os
import csv
import random

CD_MULTIPLIER = 1.5
CD_MAX = 30

def structurize():
	# initialize the file structure in case it doesn't exist
	os.makedirs("data", exist_ok=True)
	if not os.path.exists("data"+os.path.sep+"memory.csv"):
		with open("data"+os.path.sep+"memory.csv", "w") as f:
			file = csv.writer(f)
			file.writerow(["id", "cooldown", "proficiency", "subject", "chapter", "name"])
	os.makedirs("data"+os.path.sep+"etc", exist_ok=True) # uncatagorized subject
	ls: list[str] = os.listdir("data")
	for i in ls:
		if os.path.isdir("data"+os.path.sep+i):
			os.makedirs("data"+os.path.sep+i+os.path.sep+"etc", exist_ok=True) # uncatagorized chapter

def newcooldown(proficiency: int) -> int:
	# calculate new cooldown based on proficiency
	cooldown = CD_MULTIPLIER**proficiency
	return min(CD_MAX, round(cooldown))

def showitem(file_path: str):
	# display the contents of an item file
	if not os.path.exists(file_path):
		print("Error:\n\tItem file does not exist.")
		return
	if os.path.isfile(file_path):
		os.startfile(file_path)
		return
	ls = os.listdir(file_path)
	ls = [f for f in ls if not f.startswith("answer.")]
	if not ls:
		print("Error:\n\tNo item file found.")
		return
	pick = random.choice(ls)
	os.startfile(file_path+os.path.sep+pick)

def showanswer(file_path: str):
	# display the answer file of an item
	if not os.path.exists(file_path):
		print("Error:\n\Item file does not exist.")
		return
	if os.path.isfile(file_path):
		os.startfile(file_path)
		return
	ls = os.listdir(file_path)
	answers = [f for f in ls if f.startswith("answer.")]
	if not answers:
		print("Error:\n\tNo answer file found.")
		return
	for answer in answers:
		os.startfile(file_path+os.path.sep+answer)

def review(item: list[str]) -> bool:
	# review an item and update its cooldown and proficiency
	file_path = f"data{os.path.sep}{item['subject']}{os.path.sep}{item['chapter']}{os.path.sep}{item['name']}"
	item = {"id": item[0], "cooldown": int(item[1]), "proficiency": int(item[2]), "subject": item[3], "chapter": item[4], "name": item[5]}
	print(f"Reviewing item: {item['name']} (Subject: {item['subject']}, Chapter: {item['chapter']})")
	print(f"Current proficiency: {item['proficiency']}, last seen: {newcooldown(item['proficiency'])} sessions ago")
	print(f"\nfile path: .{os.path.sep}{file_path}\n")
	while True:
		choice = input("[o] open item | [a] show answer | [s] success | [f] fail | [q] quit\n> ").lower()
		if choice not in ["o", "a", "s", "f", "q"]:
			print("Invalid choice, please try again.")
			continue
		if choice == "o":
			showitem(file_path)
			continue
		if choice == "a":
			showanswer(file_path)
			continue
		if choice == "s":
			item['proficiency'] += 1
			item['cooldown'] = newcooldown(item['proficiency'])
			break
		if choice == "f":
			item['proficiency'] = 0
			item['cooldown'] = newcooldown(item['proficiency'])
			break
		if choice == "q":
			print("Exiting review.")
			return False
	rows = []
	with open("data"+os.path.sep+"memory.csv", "r") as f:
		file = csv.reader(f)
		rows.append(next(file))
		for row in file:
			if row[0] == item['id']:
				rows.append([item['id'], str(item['cooldown']), str(item['proficiency']), item['subject'], item['chapter'], item['name']])
			else:
				rows.append(row)
	with open("data"+os.path.sep+"memory.csv", "w") as f:
		file = csv.writer(f)
		file.writerows(rows)
	return True