import argparse
from utils.file_utils import (
	read_config,
	read_names_from_csv,
	append_name_to_csv,
)
from utils.openspace import Openspace


def main() -> None:
	"""
	Main function that runs the Open Space Organizer.

	Modes:
	1) Default:
	   - Reads OpenSpace configurations from a JSON file.
	   - For each configured OpenSpace:
	     - Loads the colleague names from the corresponding CSV file.
	     - Creates and organizes seating arrangements.
	   - Stores all seating plans into a single output file.
	   - Displays the results in the terminal.

	2) CLI Add Mode:
	   - Use: python main.py --add_colleague "Name" --openspace "OpenSpace Juniors"
	   - Adds the colleague to the given OpenSpace (CSV persistence),
	     rebalances tables without lonely seats, updates config.json,
	     then stores and displays all OpenSpaces (updated and others).
	"""
	parser = argparse.ArgumentParser(description="Open Space Organizer CLI")
	parser.add_argument("--add_colleague", type=str, help="Name of the new colleague to add")
	parser.add_argument("--openspace", type=str, help="Name of the OpenSpace (as in config.json) to add the colleague into")
	args = parser.parse_args()

	config_filepath = "config.json"
	output_filename = "output.csv"

	# Step 1: Read all open space configurations
	open_spaces = read_config(config_filepath)

	# CLI Mode: Add colleague to a specific OpenSpace
	if args.add_colleague and args.openspace:
		target_os_name = args.openspace.strip().lower()
		new_name = args.add_colleague.strip()
		print(f"CLI Mode: Adding '{new_name}' to '{args.openspace}'...\n")

		# Find the matching OpenSpace
		target_space: Openspace | None = None
		for os_obj in open_spaces:
			if os_obj.name.strip().lower() == target_os_name:
				target_space = os_obj
				break

		if target_space is None:
			print(f"OpenSpace '{args.openspace}' not found in config.json.")
			return

		# Append new colleague to the right CSV
		append_name_to_csv(target_space.guests_file, new_name)
		print(f"Added '{new_name}' to {target_space.guests_file}")

		# Rebalance that OpenSpace
		target_space.add_colleague(new_name, config_filepath)
		print(f"Rebalanced {target_space.name} successfully.\n")

	# Whether CLI or Default mode → write full output (for all OpenSpaces)
	with open(output_filename, "w", encoding="utf-8") as outfile:
		for open_space in open_spaces:
			# Only reorganize if we did NOT already rebalance this one
			if not (args.add_colleague and args.openspace and open_space.name.strip().lower() == args.openspace.strip().lower()):
				names = read_names_from_csv(open_space.guests_file)
				open_space.organize(names)
			open_space.store(outfile)

	# Display all OpenSpaces in the console
	for open_space in open_spaces:
		print(f"\n=== {open_space.name.upper()} ===")
		open_space.display()

	print(f"\nSeating plan saved to {output_filename}")


if __name__ == "__main__":
	main()
