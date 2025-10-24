import math
import random
from utils.table import Table
from utils.file_utils import read_names_from_csv, update_config


class Openspace:
	"""
	A class representing an open space containing multiple tables.

	Attributes:
		name (str): The name of the open space (matches key in config.json).
		number_of_tables (int): The total number of tables.
		tables (list[Table]): A list of Table objects.
		guests_file (str): Path to the CSV file containing guest names.
		table_capacity (int): Max seats per table (4, 6, or 8).
	"""

	def __init__(
		self,
		name: str = "OpenSpace BeCode",
		number_of_tables: int = 6,
		table_capacity: int = 4,
		guests_file: str = "new_colleagues.csv",
	) -> None:
		"""
		Initialize an Openspace with a given number of tables and seat capacity.

		Args:
			name (str): The name of the open space.
			number_of_tables (int): Number of tables.
			table_capacity (int): Max number of seats per table (4, 6, or 8).
			guests_file (str): Path to CSV file containing guest names.
		"""
		self.name: str = name
		self.number_of_tables: int = number_of_tables
		self.table_capacity: int = table_capacity
		self.tables: list[Table] = [Table(table_capacity) for _ in range(number_of_tables)]
		self.guests_file: str = guests_file

	def organize(self, names: list[str]) -> None:
		"""
		Randomly assign people to available seats across all tables.

		Args:
			names (list[str]): List of people to assign to seats.
		"""
		random.shuffle(names)
		index = 0
		for table in self.tables:
			while table.has_free_spot() and index < len(names):
				table.assign_seat(names[index])
				index += 1
			if index >= len(names):
				break

	def _min_allowed_for_capacity(self) -> int:
		"""
		Minimum allowed people per table given the table_capacity constraints:
			- capacity 4 -> min 2
			- capacity 6 -> min 4
			- capacity 8 -> min 6
		Returns:
			int: minimum allowed number of seated people per table.
		"""
		if self.table_capacity == 4:
			return 2
		if self.table_capacity == 6:
			return 4
		if self.table_capacity == 8:
			return 6
		# Fallback: if a different capacity is used, enforce at least 2.
		return max(2, self.table_capacity - 2)

	def _compute_distribution(self, total_people: int) -> list[int]:
		"""
		Compute an even distribution of people across tables, avoiding lonely tables and
		respecting per-table capacity ranges.

		We start from the minimum number of tables required by capacity and adjust so that
		the smallest table size is >= min_allowed (except when total_people is very small).

		Args:
			total_people (int): total number of colleagues.

		Returns:
			list[int]: list with the number of people per table (length = number of tables).
		"""
		C = self.table_capacity
		m = self._min_allowed_for_capacity()

		if total_people == 0:
			return []

		# Start from minimal number of tables to not exceed max capacity
		tables = max(1, math.ceil(total_people / C))

		# If resulting base size is less than min allowed (i.e. people would end up alone),
		# reduce the table count to increase per-table size, as long as tables > 1.
		while tables > 1:
			base = total_people // tables
			# If the minimum table size would be < m, merge tables (reduce table count)
			if base < m:
				tables -= 1
			else:
				break

		# Now create the (base/base+1) distribution across `tables`
		base = total_people // tables
		extra = total_people % tables
		sizes = [(base + 1 if i < extra else base) for i in range(tables)]

		# Edge case: if total_people < m and tables == 1, allow a single small table
		# (can't avoid "alone" if there's literally 1 person).
		return sizes

	def _rebuild_tables_and_assign(self, names: list[str]) -> None:
		"""
		Recreate tables according to the computed distribution and assign shuffled names.
		"""
		sizes = self._compute_distribution(len(names))
		self.tables = [Table(self.table_capacity) for _ in sizes]
		self.number_of_tables = len(self.tables)

		random.shuffle(names)
		idx = 0
		for i, needed in enumerate(sizes):
			for _ in range(needed):
				if idx < len(names):
					self.tables[i].assign_seat(names[idx])
					idx += 1

	def add_colleague(self, name: str, config_filepath: str) -> None:
		"""
		Add a new colleague to this OpenSpace (CSV already updated by caller),
		then rebalance tables evenly (no lonely tables), and update the config file.

		Args:
			name (str): New colleague name (used only for logging).
			config_filepath (str): Path to config.json to update the OpenSpace layout.
		"""
		# Reload all names from CSV (already appended in CLI)
		names = read_names_from_csv(self.guests_file)

		# Rebalance: decide number of tables and per-table sizes, then rebuild
		self._rebuild_tables_and_assign(names)

		# Update config.json with the new table count and existing capacity + guest file
		update_config(
			config_filepath=config_filepath,
			openspace_name=self.name,
			tables=self.number_of_tables,
			seats=self.table_capacity,
			guests_file=self.guests_file,
		)

	def display(self) -> None:
		"""
		Display the status of all tables and their occupants in a readable format.
		(Visual layout can be enhanced separately if needed.)
		"""
		for i, table in enumerate(self.tables, start=1):
			print(f"Table {i}:")
			for j, seat in enumerate(table.seats, start=1):
				status = f"  Seat {j}: {'Free' if seat.free else seat.occupant}"
				print(status)
			print()
		print("===================================\n")

	def store(self, file) -> None:
		"""
		Write the current seating arrangement into an open file handle.

		Args:
			file: An open file object where the arrangement will be written.
		"""
		file.write(f"===== {self.name.upper()} =====\n\n")
		for i, table in enumerate(self.tables, start=1):
			file.write(f"Table {i}:\n")
			for j, seat in enumerate(table.seats, start=1):
				status = f"  Seat {j}: {'Free' if seat.free else seat.occupant}\n"
				file.write(status)
			file.write("\n")
		file.write("===================================\n\n")

	def __str__(self) -> str:
		"""
		Return a formatted string summary of the Open Space.

		Returns:
			str: Summary with tables and remaining seat counts.
		"""
		result = f"OpenSpace Summary for {self.name}:\n"
		for i, table in enumerate(self.tables, start=1):
			result += f"- Table {i}: {table.left_capacity()} seats left\n"
		return result
