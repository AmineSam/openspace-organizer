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

	# Step 2: Open the output file once for all OpenSpaces
	with open(output_filename, "w", encoding="utf-8") as outfile:

		# Step 3: Loop through each configured OpenSpace
		for open_space in open_spaces:
			names = read_names_from_csv(open_space.guests_file)
			open_space.organize(names)

			# Store the results using the new centralized method
			open_space.store(outfile)

	# Step 4: Display the results in the console
	for open_space in open_spaces:
		print(f"\n=== {open_space.name.upper()} ===")
		open_space.display()


if __name__ == "__main__":
	main()
