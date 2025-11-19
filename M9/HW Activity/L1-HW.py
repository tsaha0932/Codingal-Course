def update_student_intro(filename, student_name, favorite_subject):
    import os
    if os.path.exists(filename):
        file = open(filename, "r")
        data = file.readlines()
        file.close()
    else:
        data = []

    new_data = []
    skip = False

    for line in data:
        if line.startswith("Name: " + student_name):
            skip = True
            continue
        if skip and line.strip() == "":
            skip = False
            continue
        if not skip:
            new_data.append(line)

    intro = f"Name: {student_name}\nFavorite Subject: {favorite_subject}\n\n"
    new_data.append(intro)

    file = open(filename, "w")
    file.writelines(new_data)
    file.close()

    print(f"Updated record for {student_name} successfully!")


# Example usage
update_student_intro("students.txt", "Roy", "Mathematics")
update_student_intro("students.txt", "Priya", "Science")
update_student_intro("students.txt", "Rahul", "English")
