records = {}

while True:
    print("\n--- Student Record System ---")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Display Records")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        records[roll] = {"Name": name, "Marks": marks}

        print("Record Saved")

    elif ch == "2":
        roll = input("Enter Roll No to Search: ")

        if roll in records:
            print("Name :", records[roll]["Name"])
            print("Marks:", records[roll]["Marks"])
        else:
            print("Record Not Found")

    elif ch == "3":
        if records:
            print("\nStudent Details")
            for roll in records:
                print(
                    "Roll:", roll,
                    "| Name:", records[roll]["Name"],
                    "| Marks:", records[roll]["Marks"]
                )
        else:
            print("No Records Available")

    elif ch == "4":
        print("Program Closed")
        break

    else:
        print("Wrong Choice")