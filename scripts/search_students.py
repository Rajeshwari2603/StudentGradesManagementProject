import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("db/grades.db")
cursor = conn.cursor()

def search_menu():
    print("\n🔍 Student Grade Search Menu")
    print("1. Search by Student ID")
    print("2. Search by Name")
    print("3. Filter by Grade (A/B/C/D/F)")
    print("4. Show All Students")
    print("5. Exit")

while True:
    search_menu()
    choice = input("Enter your choice (1–5): ")

    if choice == '1':
        sid = input("Enter Student ID: ")
        cursor.execute("SELECT * FROM students WHERE StudentID = ?", (sid,))
    elif choice == '2':
        name = input("Enter full or partial name: ")
        cursor.execute("SELECT * FROM students WHERE Name LIKE ?", ('%' + name + '%',))
    elif choice == '3':
        grade = input("Enter Grade (A/B/C/D/F): ").upper()
        cursor.execute("SELECT * FROM students WHERE Grade = ?", (grade,))
    elif choice == '4':
        cursor.execute("SELECT * FROM students")
    elif choice == '5':
        print("✅ Exiting. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")
        continue

    results = cursor.fetchall()
    if results:
        print("\n📋 Results:")
        for row in results:
            print(row)
    else:
        print("⚠️ No records found.")

conn.close()
