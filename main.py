#region Program Start

import os

NOTES_FOLDER = "notes"

if not os.path.exists(NOTES_FOLDER):
    os.mkdir(NOTES_FOLDER)

#endregion


#region Create Note

def create_note():

    title = input("Enter Note Title: ").strip().title()

    if not title:
        print("Title cannot be empty!")
        return

    file_path = os.path.join(NOTES_FOLDER, title + ".txt")

    if os.path.exists(file_path):
        print("A note with this title already exists!")
        return

    print("\nWrite Your Note")
    print("Type END on a new line to save.\n")

    lines = []

    while True:

        line = input()

        if line.upper() == "END":
            break

        lines.append(line)

    with open(file_path, "w", encoding="utf-8") as file:

        file.write("\n".join(lines))

    print("Note Created Successfully!")

#endregion


#region View Notes

def view_notes():

    files = os.listdir(NOTES_FOLDER)

    txt_files = []

    for file in files:

        if file.endswith(".txt"):
            txt_files.append(file)

    if not txt_files:
        print("No Notes Found!")
        return []

    print("\n-------- NOTES --------")

    for i, file in enumerate(txt_files, start=1):

        print(f"{i}. {file[:-4]}")

    return txt_files

#endregion


#region Open Note

def open_note():

    notes = view_notes()

    if not notes:
        return

    try:

        note_num = int(input("\nEnter Note Number: "))

        if 1 <= note_num <= len(notes):

            file_path = os.path.join(
                NOTES_FOLDER,
                notes[note_num - 1]
            )

            with open(file_path, "r", encoding="utf-8") as file:

                print("\n---------- NOTE ----------\n")

                print(file.read())

                print("\n--------------------------")

        else:
            print("Invalid Note Number!")

    except ValueError:

        print("Please Enter a Valid Number!")

#endregion

#region Edit Note

def edit_note():

    notes = view_notes()

    if not notes:
        return

    try:

        note_num = int(input("\nEnter Note Number: "))

        if 1 <= note_num <= len(notes):

            file_path = os.path.join(
                NOTES_FOLDER,
                notes[note_num - 1]
            )

            print("\nCurrent Note\n")

            with open(file_path, "r", encoding="utf-8") as file:
                print(file.read())

            print("\nWrite New Note")
            print("Type END on a new line to save.\n")

            lines = []

            while True:

                line = input()

                if line.upper() == "END":
                    break

                lines.append(line)

            with open(file_path, "w", encoding="utf-8") as file:
                file.write("\n".join(lines))

            print("Note Updated Successfully!")

        else:
            print("Invalid Note Number!")

    except ValueError:
        print("Please Enter a Valid Number!")

#endregion


#region Delete Note

def delete_note():

    notes = view_notes()

    if not notes:
        return

    try:

        note_num = int(input("\nEnter Note Number: "))

        if 1 <= note_num <= len(notes):

            file_path = os.path.join(
                NOTES_FOLDER,
                notes[note_num - 1]
            )

            os.remove(file_path)

            print("Note Deleted Successfully!")

        else:
            print("Invalid Note Number!")

    except ValueError:
        print("Please Enter a Valid Number!")

#endregion


#region Search Note

def search_note():

    keyword = input("Enter Note Title: ").strip().lower()

    notes = os.listdir(NOTES_FOLDER)

    found = False

    print("\n-------- SEARCH RESULT --------")

    for note in notes:

        if note.endswith(".txt"):

            if keyword in note.lower():

                print(note[:-4])

                found = True

    if not found:
        print("No Matching Note Found!")

#endregion


#region Rename Note

def rename_note():

    notes = view_notes()

    if not notes:
        return

    try:

        note_num = int(input("\nEnter Note Number: "))

        if 1 <= note_num <= len(notes):

            new_name = input("Enter New Title: ").strip().title()

            if not new_name:
                print("Title cannot be empty!")
                return

            old_path = os.path.join(
                NOTES_FOLDER,
                notes[note_num - 1]
            )

            new_path = os.path.join(
                NOTES_FOLDER,
                new_name + ".txt"
            )

            if os.path.exists(new_path):
                print("A note with this title already exists!")
                return

            os.rename(old_path, new_path)

            print("Note Renamed Successfully!")

        else:
            print("Invalid Note Number!")

    except ValueError:
        print("Please Enter a Valid Number!")

#endregion


#region Statistics

def show_statistics():

    notes = os.listdir(NOTES_FOLDER)

    total = 0

    for note in notes:

        if note.endswith(".txt"):
            total += 1

    print("\n-------- STATISTICS --------")
    print(f"Total Notes : {total}")

#endregion

#region Main Function

def main():

    while True:

        print("\n" + " MARKDOWN NOTE APP ".center(50, "="))
        print("1. Create Note")
        print("2. View Notes")
        print("3. Open Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Search Note")
        print("7. Rename Note")
        print("8. Statistics")
        print("9. Exit")

        choice = input("\nChoose Option: ").strip()

        if choice == "1":
            create_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            open_note()

        elif choice == "4":
            edit_note()

        elif choice == "5":
            delete_note()

        elif choice == "6":
            search_note()

        elif choice == "7":
            rename_note()

        elif choice == "8":
            show_statistics()

        elif choice == "9":
            print("Thanks for Using Markdown Note App!")
            break

        else:
            print("Invalid Choice!")

#endregion


#region Program Entry Point

if __name__ == "__main__":
    main()

#endregion


#region End Of Program