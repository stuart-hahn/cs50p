import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    fieldnames = ["name", "home"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow({"name": name, "home": home})
