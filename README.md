# 🏢 OpenSpace Organizer
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## 📖 Description

Your company moved to a new open space office with **6 tables of 4 seats each (24 colleagues total)**.  
To help everyone get to know each other better, the team decided to **rotate seats every day** so that everyone sits with different colleagues.

The **OpenSpace Organizer** automatically:
- Reads your colleague names from a CSV file.
- Randomly assigns each person to a table and seat.
- Displays the arrangement clearly in the terminal.
- Saves the seating plan to an `output.csv` file.

![coworking_img](https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fGRpdmVyc2UlMjB0ZWFtfGVufDB8fDB8fHwy)

---

## 📦 Folder Structure

openspace-organizer/
│
├── main.py
└── utils/
├── init.py
├── file_utils.py
├── openspace.py
└── table.py

yaml
Copy code

- **main.py** → Entry point of the program.  
- **utils/file_utils.py** → Handles CSV file reading and writing.  
- **utils/table.py** → Contains `Seat` and `Table` classes for seat and table logic.  
- **utils/openspace.py** → Contains the `Openspace` class that manages all tables.  

---

## ⚙️ How It Works

1. **People** are read from a `.csv` file (`new_colleagues.csv`).
2. **Seats & Tables** are represented by two classes:
   - `Seat`: manages individual seat status and occupant.
   - `Table`: manages a collection of seats.
3. **OpenSpace** is a class that groups all tables and organizes everyone randomly.
4. The resulting seating plan is displayed and stored for review.

---

## 🚀 Usage

### 1️⃣ Install and Run

```bash
git clone https://github.com/<yourusername>/openspace-organizer.git
cd openspace-organizer
python main.py
2️⃣ Input File Example
new_colleagues.csv

python-repl
Copy code
Alice
Bob
Charlie
Diana
Eve
Frank
...
3️⃣ Output Example
Console display:

yaml
Copy code
===== OPEN SPACE ORGANIZATION =====

Table 1:
  Seat 1: Alice
  Seat 2: Bob
  Seat 3: Charlie
  Seat 4: Diana

Table 2:
  Seat 1: Eve
  Seat 2: Frank
  Seat 3: Grace
  Seat 4: Heidi
...
===================================
Saved file: output.csv

🧩 Code Overview
python
Copy code
def main() -> None:
    """
    Main function that runs the Open Space Organizer.
    """
    input_filepath = "new_colleagues.csv"
    output_filename = "output.csv"

    # Step 1: Read all colleague names
    names = read_names_from_csv(input_filepath)

    # Step 2: Create an OpenSpace
    open_space = Openspace(number_of_tables=6, table_capacity=4)

    # Step 3: Assign colleagues randomly to seats
    open_space.organize(names)

    # Step 4: Save and display results
    open_space.store(output_filename)
    open_space.display()

if __name__ == "__main__":
    main()
🧠 Code Style & Conventions
Every class includes a __str__() method for readable output.

All functions and classes are typed using Python type hints.

Every function and class includes a proper docstring following this structure:

python
Copy code
def example_function(arg: str) -> int:
    """
    Brief description.

    Args:
        arg (str): description.

    Returns:
        int: description.
    """
Indentation uses tabs (Go-style formatting consistency).

🧱 Example Open Space Layout
A simplified visual representation of the 6 tables (4 seats each):

less
Copy code
+-----------+    +-----------+    +-----------+
| Table 1   |    | Table 2   |    | Table 3   |
| [1][2][3][4]   | [1][2][3][4]   | [1][2][3][4]   |
+-----------+    +-----------+    +-----------+

+-----------+    +-----------+    +-----------+
| Table 4   |    | Table 5   |    | Table 6   |
| [1][2][3][4]   | [1][2][3][4]   | [1][2][3][4]   |
+-----------+    +-----------+    +-----------+
⏱️ Timeline
This project was completed in approximately 2 days.

🧑‍💻 Author & Context
This project was created as part of the AI Bootcamp at BeCode.org.

Connect with me on LinkedIn.

🏁 Future Improvements
Add support for Excel (.xlsx) input/output.

Create a CLI menu to reassign seats interactively.

Build a GUI or web interface for daily randomization.

Automate daily runs and email the seating plan automatically.