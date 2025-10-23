import csv
from typing import List


def read_names_from_csv(filepath: str) -> List[str]:
	"""
	Read colleague names from a CSV file and return them as a list.

	Args:
		filepath (str): Path to the CSV file containing the colleague names.

	Returns:
		List[str]: A list of names loaded from the CSV file.
	"""
	names: List[str] = []
	with open(filepath, mode="r", encoding="utf-8") as file:
		reader = csv.reader(file)
		for row in reader:
			if len(row) > 0 and row[0].strip() != "":
				names.append(row[0].strip())
	return names
