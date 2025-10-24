import random
from utils.table import Table



class Openspace:
	"""
	A class representing an open space containing multiple tables.

	Attributes:
		tables (List[Table]): The list of tables in the open space.
		number_of_tables (int): The total number of tables.
	"""

	def __init__(self, number_of_tables: int, table_capacity: int) -> None:
		"""
		Initialize an Openspace with a given number of tables and their seat capacity.

		Args:
			number_of_tables (int): Number of tables in the open space.
			table_capacity (int): Number of seats per table.
		"""
		self.number_of_tables: int = number_of_tables
		self.tables: list[Table] = [Table(table_capacity) for _ in range(number_of_tables)]

	def organize(self, names: list[str]) -> None:
		"""
		Randomly assign people to available seats across all tables.

		Args:
			names (List[str]): The list of people to assign to seats.
		"""
		random.shuffle(names)
		index = 0
		for table in self.tables:
			while table.has_free_spot() and index < len(names):
				table.assign_seat(names[index])
				index += 1
			if index >= len(names):
				break

	def display(self) -> None:
		"""
		Display the status of all tables and their occupants in a readable format.
		"""
		
		for i, table in enumerate(self.tables, start=1):
			print(f"Table {i}:")
			for j, seat in enumerate(table.seats, start=1):
				status = f"  Seat {j}: {'Free' if seat.free else seat.occupant}"
				print(status)
			print()  # Blank line between tables
		

	def store(self, filename: str) -> None:
		"""
		Store the current seating arrangement in a text file.

		Args:
			filename (str): The name of the file where the arrangement will be saved.
		"""
		with open(filename, "w", encoding="utf-8") as file:
			for i, table in enumerate(self.tables, start=1):
				file.write(f"Table {i}:\n")
				for j, seat in enumerate(table.seats, start=1):
					status = f"  Seat {j}: {'Free' if seat.free else seat.occupant}\n"
					file.write(status)
				file.write("\n")
	def __str__(self) -> str:
		"""
		Return a formatted string summary of the Open Space.

		Returns:
			str: Summary with tables and seat occupancy.
		"""
		result = "OpenSpace Summary:\n"
		for i, table in enumerate(self.tables, start=1):
			result += f"- Table {i}: {table.left_capacity()} seats left\n"
		return result
