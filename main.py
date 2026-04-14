class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

def main():
    # Initial list
    classmates = [
        Classmate("Kristine", "Amethyst", "Math"),
        Classmate("Jean", "Amethyst", "Science"),
        Classmate("Hariette", "Amethyst", "English"),
        Classmate("Jubilee", "Amethyst", "Math"),
        Classmate("Vivian", "Amethyst", "History")
    ]

    while True:
        print("\n--- Grade 10 Classmates System ---")
        print("1. Add Classmate")
        print("2. Show List")
        print("3. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter Name: ")
            section = input("Enter Section: ")
            subject = input("Enter Favorite Subject: ")
            classmates.append(Classmate(name, section, subject))
            print("Successfully added!")

        elif choice == '2':
            print("\n📋 Classmate List:")
            # Loop to display all introductions
            for student in classmates:
                print(student.introduce())
        
        elif choice == '3':
            break

if __name__ == "__main__":
    main()