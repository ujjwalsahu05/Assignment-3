"""                                             NOTE       
                                        Name : Ujjwal Sahu
                                        Enrollment : 0157AL231216 
                                        Year : 3RD  Section : c
                                        BATCH - 5 (MTF) - 10:30 AM
                                        COLLEGE :  LNCTS - AIML
"""

students = []
scores = []

current_student = None
is_logged_in = False
is_admin = False

# ---------- REGISTRATION & LOGIN ----------

def register():
    print("\n--- Student Registration ---")
    username = input("Enter Username: ")
    for student in students:
        if student['username'] == username:
            print("Username already exists!")
            return
    password = input("Enter Password: ")
    name = input("Enter Full Name: ")
    roll_no = input("Enter Roll No: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    address = input("Enter Address: ")
    dob = input("Enter DOB (DD-MM-YYYY): ")
    gender = input("Enter Gender (M/F): ")
    department = input("Enter Department: ")
    year = input("Enter Year: ")

    student = {
        "username": username,
        "password": password,
        "name": name,
        "roll_no": roll_no,
        "email": email,
        "phone": phone,
        "address": address,
        "dob": dob,
        "gender": gender,
        "department": department,
        "year": year
    }
    students.append(student)
    print("Registration successful!")

def login():
    global current_student, is_logged_in, is_admin
    print("\n--- Login ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Admin login
    if username == "admin" and password == "admin123":
        is_logged_in = True
        is_admin = True
        print("Admin login successful!")
        return

    for student in students:
        if student['username'] == username and student['password'] == password:
            current_student = student
            is_logged_in = True
            is_admin = False
            print(f"Welcome {current_student['name']}! Login successful!")
            return
    print("Invalid credentials!")

def logout():
    global current_student, is_logged_in, is_admin
    if is_logged_in:
        print("Logged out successfully.")
        current_student = None
        is_logged_in = False
        is_admin = False
    else:
        print("No one is logged in.")

# ---------- PROFILE MANAGEMENT ----------

def show_profile():
    if not is_logged_in or is_admin:
        print("Login as a student to view profile.")
        return
    print("\n--- Student Profile ---")
    for key, value in current_student.items():
        print(f"{key.capitalize()}: {value}")

def update_profile():
    if not is_logged_in or is_admin:
        print("Login as a student to update profile.")
        return
    print("\n--- Update Profile ---")
    for key in ['name', 'email', 'phone', 'department', 'year', 'address']:
        new_val = input(f"Update {key} (current: {current_student[key]}): ")
        if new_val.strip():
            current_student[key] = new_val
    print("Profile updated successfully!")

# ---------- QUIZ SECTION ----------

questions = {
    "DSA": [
        ("What is the time complexity of binary search?", ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "O(log n)"),
        ("Which data structure uses FIFO?", ["Stack", "Queue", "Tree", "Graph"], "Queue"),
        ("Which is not a linear data structure?", ["Array", "Queue", "Tree", "Stack"], "Tree"),
        ("What does DFS stand for?", ["Data File Search", "Depth First Search", "Depth Fast Search", "Data First Search"], "Depth First Search"),
        ("Which sorting algorithm is best for large datasets?", ["Bubble", "Insertion", "Quick", "Selection"], "Quick")
    ],
    "DBMS": [
        ("What does SQL stand for?", ["Structured Query Language", "Strong Question Language", "Simple Query Logic", "None"], "Structured Query Language"),
        ("Which key uniquely identifies a record?", ["Primary key", "Foreign key", "Candidate key", "Super key"], "Primary key"),
        ("Which command is used to remove all records?", ["DELETE", "REMOVE", "DROP", "TRUNCATE"], "TRUNCATE"),
        ("Which of the following is a type of join?", ["Inner", "Outer", "Left", "All of these"], "All of these"),
        ("Which of the following is not a DBMS?", ["MySQL", "Oracle", "Python", "MongoDB"], "Python")
    ],
    "PYTHON": [
        ("What is the output of print(2**3)?", ["6", "8", "9", "Error"], "8"),
        ("Which keyword is used for function?", ["def", "fun", "function", "define"], "def"),
        ("Which of these is immutable?", ["List", "Set", "Tuple", "Dictionary"], "Tuple"),
        ("What does PEP stand for?", ["Python Enhancement Proposal", "Python Execution Process", "Program Entry Point", "None"], "Python Enhancement Proposal"),
        ("Which is used for comments?", ["//", "#", "/* */", "--"], "#")
    ]
}

def attempt_quiz():
    if not is_logged_in or is_admin:
        print("Only students can attempt quiz.")
        return
    print("\nCategories: DSA, DBMS, PYTHON")
    category = input("Choose category: ").upper()
    if category not in questions:
        print("Invalid category.")
        return

    quiz_qs = questions[category]
    score = 0
    total = len(quiz_qs)

    for i, (q, opts, ans) in enumerate(quiz_qs, start=1):
        print(f"\nQ{i}. {q}")
        for j, o in enumerate(opts, start=1):
            print(f"  {j}. {o}")
        try:
            choice = int(input("Your answer (1-4): "))
            if opts[choice - 1] == ans:
                score += 1
        except:
            print("Invalid choice, skipping question.")

    print(f"\nYour Score: {score}/{total}")
    scores.append({
        "roll_no": current_student['roll_no'],
        "category": category,
        "marks": f"{score}/{total}"
    })
    print("Your score has been recorded!")

# ---------- ADMIN PANEL ----------

def view_all_scores():
    if not scores:
        print("No score records found.")
        return

    print("\n--- All Quiz Records ---")
    for s in scores:
        print(f"{s['roll_no']} | {s['category']} | {s['marks']}")

# ---------- MAIN MENU ----------

def main():
    while True:
        print("\n===== QUIZ SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        ch = input("Enter your choice: ")

        if ch == '1':
            register()
        elif ch == '2':
            login()
            if is_logged_in:
                if is_admin:
                    while True:
                        print("\n--- Admin Panel ---")
                        print("1. View All Scores\n2. Logout")
                        a = input("Enter choice: ")
                        if a == '1':
                            view_all_scores()
                        elif a == '2':
                            logout()
                            break
                        else:
                            print("Invalid choice.")
                else:
                    while is_logged_in:
                        print("\n--- Student Menu ---")
                        print("1. Attempt Quiz\n2. View Profile\n3. Update Profile\n4. Logout")
                        s = input("Enter choice: ")
                        if s == '1':
                            attempt_quiz()
                        elif s == '2':
                            show_profile()
                        elif s == '3':
                            update_profile()
                        elif s == '4':
                            logout()
                        else:
                            print("Invalid choice.")
        elif ch == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
