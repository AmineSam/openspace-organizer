# OpenSpace Organizer
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

Your company moved to a new office at CEVI Ghent. Its an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. 

This script runs everyday to re-assign everybody to a new seat.

<img width="700" height="1000" alt="Image" src="https://github.com/user-attachments/assets/5d22cdff-9cfa-42b3-b4f8-c3f86a06963d" />

## 📦 Repo structure

```
├── utils/
│   ├── openspace.py
│   ├── table.py
│   └── file_utils.py
├── .gitignore
├── main.py
├── new_colleagues.csv
├── output.csv
└── README.md
```

## 🛎️ Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

```
   python main.py
```

3. The script reads your input file, and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "output.csv" file in your root directory. 

```python
from utils.file_utils import read_names_from_csv
from utils.openspace import Openspace


def main() -> None:
	"""
	Main function that runs the Open Space Organizer.

	This function:
	1. Reads colleague names from a CSV file.
	2. Creates an OpenSpace with tables and seats.
	3. Randomly assigns people to seats.
	4. Saves the final seating plan to an output file.
	5. Displays the results in the terminal.
	"""
	input_filepath = "new_colleagues.csv"
	output_filename = "output.csv"

	# Step 1: Read all colleague names from the input CSV
	names = read_names_from_csv(input_filepath)

	# Step 2: Create an OpenSpace (6 tables × 4 seats)
	open_space = Openspace(number_of_tables=6, table_capacity=4)

	# Step 3: Randomly assign colleagues to available seats
	open_space.organize(names)

	# Step 4: Save the seating plan to a file
	open_space.store(output_filename)

	# Step 5: Display the assignments in the console
	open_space.display()


if __name__ == "__main__":
	main()
```
## ⏱️ Timeline

This project took two days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/vriveraq/).