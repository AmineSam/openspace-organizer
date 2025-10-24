import random
from utils.table import Table


class Openspace:
    """
    A class representing an open space containing multiple tables.

    Attributes:
            name (str): The name of the open space.
            number_of_tables (int): The total number of tables.
            tables (list[Table]): A list of Table objects.
            guests_file (str): Path to the CSV file containing guest names.
    """

    def __init__(
        self,
        name: str = "BeCode",
        number_of_tables: int = 6,
        table_capacity: int = 4,
        guests_file: str = "new_colleagues.csv",
    ) -> None:
        """
        Initialize an Openspace with a given number of tables and seat capacity.

        Args:
                name (str): The name of the open space.
                number_of_tables (int): Number of tables.
                table_capacity (int): Number of seats per table.
                guests_file (str): Path to CSV file containing guest names.
        """
        self.name: str = name
        self.number_of_tables: int = number_of_tables
        self.tables: list[Table] = [
            Table(table_capacity) for _ in range(number_of_tables)
        ]
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

    def display(self) -> None:
        """
        Display the status of all tables and their occupants in a readable format.
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
