class Seat:
    """
    A class representing a single seat in the Open Space.

    Attributes:
            free (bool): Indicates whether the seat is free or occupied.
            occupant (str): The name of the person occupying the seat, or an empty string if free.
    """

    def __init__(self) -> None:
        """Initialize a Seat object as free with no occupant."""
        self.free: bool = True
        self.occupant: str = ""

    def set_occupant(self, name: str) -> bool:
        """
        Assign a person to the seat if it is free.

        Args:
                name (str): The name of the person to assign.

        Returns:
                bool: True if assignment was successful, False otherwise.
        """
        if self.free:
            self.occupant = name
            self.free = False
            return True
        return False

    def remove_occupant(self) -> str:
        """
        Remove the occupant from the seat.

        Returns:
                str: The name of the removed occupant, or an empty string if the seat was already free.
        """
        if not self.free:
            name = self.occupant
            self.occupant = ""
            self.free = True
            return name
        return ""

    def __str__(self) -> str:
        """
        Return a string representation of the seat status.

        Returns:
                str: Description of the seat’s current status.
        """
        return "Seat is free" if self.free else f"Seat occupied by {self.occupant}"


class Table:
    """
    A class representing a table in the Open Space.

    Attributes:
            capacity (int): The total number of seats at the table.
            seats (List[Seat]): A list of Seat objects.
    """

    def __init__(self, capacity: int) -> None:
        """
        Initialize a Table with a given capacity and create empty seats.

        Args:
                capacity (int): The number of seats at the table.
        """
        self.capacity: int = capacity
        self.seats: list[Seat] = [Seat() for _ in range(capacity)]

    def has_free_spot(self) -> bool:
        """
        Check if the table has at least one free seat.

        Returns:
                bool: True if a seat is free, False otherwise.
        """
        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat(self, name: str) -> bool:
        """
        Assign a person to the first available free seat at the table.

        Args:
                name (str): The name of the person to assign.

        Returns:
                bool: True if successfully assigned, False if no seat is available.
        """
        for seat in self.seats:
            if seat.set_occupant(name):
                return True
        return False

    def left_capacity(self) -> int:
        """
        Return the number of available seats left at the table.

        Returns:
                int: The number of free seats remaining.
        """
        count = 0
        for seat in self.seats:
            if seat.free:
                count += 1
        return count

    def __str__(self) -> str:
        """
        Return a string representation of the table status.

        Returns:
                str: Summary of seat availability and occupants.
        """
        occupied = [seat.occupant for seat in self.seats if not seat.free]
        if occupied:
            return f"Table ({len(occupied)}/{self.capacity}) occupied by: {', '.join(occupied)}"
        return f"Table ({len(occupied)}/{self.capacity}) occupied by: No one"
