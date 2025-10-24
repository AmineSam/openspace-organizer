import os
import csv
import json
from utils.openspace import Openspace


def read_names_from_csv(filepath: str) -> list[str]:
	"""
	Read colleague names from a CSV file and return them as a list.

	Args:
		filepath (str): Path to the CSV file containing the colleague names.

	Returns:
		list[str]: A list of names loaded from the CSV file.
	"""
	names: list[str] = []

	if not os.path.exists(filepath):
		raise FileNotFoundError(f"The file '{filepath}' does not exist.")

	with open(filepath, mode="r", encoding="utf-8") as file:
		reader = csv.reader(file)
		for row in reader:
			if len(row) > 0 and row[0].strip() != "":
				names.append(row[0].strip())
	return names


def append_name_to_csv(filepath: str, name: str) -> None:
	"""
	Append a new colleague name to the CSV file for persistence.

	Args:
		filepath (str): Path to the CSV file.
		name (str): New colleague name.
	"""
	# Create file if it doesn't exist
	create_header = False
	if not os.path.exists(filepath):
		# If you want headers, set create_header=True and write one.
		open(filepath, "a", encoding="utf-8").close()

	with open(filepath, mode="a", encoding="utf-8", newline="") as file:
		writer = csv.writer(file)
		writer.writerow([name])


def read_config(config_filepath: str) -> list[Openspace]:
	"""
	Read the room setup configuration from a JSON file and return a list of OpenSpace objects.

	Args:
		config_filepath (str): Path to the JSON configuration file.

	Returns:
		list[Openspace]: A list of OpenSpace instances created from the config file.
	"""
	if not os.path.exists(config_filepath):
		raise FileNotFoundError(f"The file '{config_filepath}' does not exist.")

	with open(config_filepath, mode="r", encoding="utf-8") as file:
		config_data = json.load(file)

	open_spaces: list[Openspace] = []

	for name, data in config_data.items():
		tables = data.get("Tables", 0)
		seats = data.get("Seats", 0)
		guests_file = data.get("Guests", "")
		open_space = Openspace(
			name=name,
			number_of_tables=tables,
			table_capacity=seats,
			guests_file=guests_file,
		)
		open_spaces.append(open_space)

	return open_spaces


def update_config(config_filepath: str, openspace_name: str, tables: int, seats: int, guests_file: str) -> None:
	"""
	Update the config.json for a specific OpenSpace entry.

	Args:
		config_filepath (str): Path to config.json.
		openspace_name (str): The key name in config.json (e.g., "OpenSpace Juniors").
		tables (int): Updated number of tables.
		seats (int): Max seats per table (capacity).
		guests_file (str): Path to the corresponding CSV file.
	"""
	if not os.path.exists(config_filepath):
		raise FileNotFoundError(f"The file '{config_filepath}' does not exist.")

	with open(config_filepath, mode="r", encoding="utf-8") as file:
		data = json.load(file)

	if openspace_name not in data:
		# Create if not existing
		data[openspace_name] = {}

	data[openspace_name]["Tables"] = int(tables)
	data[openspace_name]["Seats"] = int(seats)
	data[openspace_name]["Guests"] = guests_file

	with open(config_filepath, mode="w", encoding="utf-8") as file:
		json.dump(data, file, indent=2)
