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
		List[str]: A list of names loaded from the CSV file.
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


def read_config(config_filepath: str) -> list[Openspace]:
	"""
	Read the room setup configuration from a JSON file and return a list of OpenSpace objects.

	Args:
		config_filepath (str): Path to the JSON configuration file.

	Returns:
		List[OpenSpace]: A list of OpenSpace instances created from the config file.
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
		open_space = Openspace(name=name, number_of_tables=tables, table_capacity=seats, guests_file=guests_file)
		open_spaces.append(open_space)

	return open_spaces
