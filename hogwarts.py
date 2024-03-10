def main():
    students = [
        {"Name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
        {"Name": "Draco", "House": "Slytherin", "Patronus": None},
        {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
        {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russell Terrier"},
    ]
    for student in students:
        print(student.get("Patronus"))


if __name__ == "__main__":
    main()
