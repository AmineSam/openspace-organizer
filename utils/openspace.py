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
		Display all 6 tables (4 seats each) in a visual rectangular layout.
		The table name appears centered inside the rectangle,
		and seats are evenly spaced around it.
		"""

		print("OPEN SPACE SEATING ARRANGEMENT\n")

		for i, table in enumerate(self.tables, start=1):

			# Ensure layout only runs for 4 seats
			if len(table.seats) != 4:
				continue

			# Extract occupant names (or 'Free')
			s = [seat.occupant if not seat.free else "Free" for seat in table.seats]

			# Layout:
			#   [Seat1]          [Seat2]
			#         +-------------+
			#         |   Table i   |
			#         +-------------+
			#   [Seat3]          [Seat4]

			top_row = f"  [{s[0]:^8}]          [{s[1]:^8}]"
			table_box = f"        +-------------+\n        |  Table {i:^3}  |\n        +-------------+"
			bottom_row = f"  [{s[2]:^8}]          [{s[3]:^8}]"

			print(top_row)
			print(table_box)
			print(bottom_row)
			print("\n" + " " * 2 + "-" * 44 + "\n")
	

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
