from utils.file_utils import read_config, read_names_from_csv



def main() -> None:
	"""
	Main function that runs the Open Space Organizer.

	This function:
	1. Reads OpenSpace configurations from a JSON file.
	2. For each configured OpenSpace:
		- Loads the colleague names from the corresponding CSV file.
		- Creates and organizes seating arrangements.
	3. Stores all seating plans into a single output file.
	4. Displays all the results in the terminal.
	"""
	config_filepath = "config.json"
	output_filename = "output.csv"

	# Step 1: Read all open space configurations
	open_spaces = read_config(config_filepath)

	# Step 2: Open output file once to store all results together
	with open(output_filename, "w", encoding="utf-8") as outfile:
		
		# Step 3: Loop through each OpenSpace from config
		for open_space in open_spaces:
			# Read the list of names for this open space
			names = read_names_from_csv(open_space.guests_file)

			# Organize seating arrangement
			open_space.organize(names)

			# Store each open space's data in the output file
			outfile.write(f"===== {open_space.name.upper()} =====\n\n")
			for i, table in enumerate(open_space.tables, start=1):
				outfile.write(f"Table {i}:\n")
				for j, seat in enumerate(table.seats, start=1):
					status = f"  Seat {j}: {'Free' if seat.free else seat.occupant}\n"
					outfile.write(status)
				outfile.write("\n")
			outfile.write("===================================\n\n")

	# Step 4: Display the results in the console
	for open_space in open_spaces:
		print(f"\n=== {open_space.name.upper()} ===")
		open_space.display()


if __name__ == "__main__":
	main()
