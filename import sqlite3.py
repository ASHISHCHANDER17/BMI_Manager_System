import sqlite3
from datetime import datetime

# --- Database Management Functions ---

def create_connection():
    """Creates a connection to the SQLite database."""
    try:
        # This will create the file 'bmi_database.db' automatically
        conn = sqlite3.connect('bmi_database.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(conn):
    """Creates the table to store BMI records if it doesn't exist."""
    try:
        cursor = conn.cursor()
        # SQL query to create the table
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS bmi_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50),
            weight REAL,
            height REAL,
            bmi REAL,
            category VARCHAR(20),
            date_recorded DATETIME
        );
        """
        cursor.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def save_record(conn, name, weight, height, bmi, category):
    """Inserts a new BMI record into the database."""
    try:
        cursor = conn.cursor()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        sql_insert = """
        INSERT INTO bmi_records (name, weight, height, bmi, category, date_recorded)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        
        cursor.execute(sql_insert, (name, weight, height, bmi, category, current_time))
        conn.commit()
        print(f"\n✅ Record for {name} saved successfully!")
    except sqlite3.Error as e:
        print(f"Error saving record: {e}")

def view_history(conn):
    """Fetches and displays all saved records."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bmi_records ORDER BY date_recorded DESC")
    rows = cursor.fetchall()

    print("\n" + "="*70)
    print(f"{'ID':<5} | {'Name':<15} | {'BMI':<6} | {'Category':<15} | {'Date':<20}")
    print("="*70)

    if not rows:
        print("No records found in database.")
    else:
        for row in rows:
            # row structure: (id, name, weight, height, bmi, category, date)
            print(f"{row[0]:<5} | {row[1]:<15} | {row[4]:<6} | {row[5]:<15} | {row[6]:<20}")
    print("="*70 + "\n")

# --- Logic Functions ---

def get_bmi_category(bmi):
    """Returns the category based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmi_logic():
    """Handles the user input and calculation logic."""
    print("\n--- NEW BMI CALCULATION ---")
    name = input("Enter Name: ")
    
    try:
        weight = float(input("Enter Weight (kg): "))
        height_cm = float(input("Enter Height (cm): "))
        
        # BMI Formula: Weight (kg) / Height (m)^2
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)
        
        category = get_bmi_category(bmi)
        
        print(f"\n---> Your BMI is: {bmi}")
        print(f"---> Category: {category}")
        
        return name, weight, height_cm, bmi, category
        
    except ValueError:
        print("\n❌ Invalid input! Please enter numbers for weight and height.")
        return None

# --- Main Application ---

def main():
    # 1. Setup Database
    conn = create_connection()
    if conn is not None:
        create_table(conn)
    else:
        print("Failed to initialize database. Exiting.")
        return

    # 2. Main Menu Loop
    while True:
        print("\n=== BMI MANAGER SYSTEM ===")
        print("1. Calculate BMI & Save")
        print("2. View History")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            result = calculate_bmi_logic()
            if result:
                save = input("Do you want to save this record? (y/n): ").lower()
                if save == 'y':
                    save_record(conn, *result) # Unpack the tuple result
        
        elif choice == '2':
            view_history(conn)
            
        elif choice == '3':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

    conn.close()

if __name__ == '__main__':
    main()