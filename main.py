from utils.file_utils import read_names_from_csv
from utils.openspace import Openspace


def main() -> None:
    """
    Main function that runs the Open Space Organizer.

    This function:
    1. Reads colleague names from a CSV file.
    2. Creates an OpenSpace with tables and seats.
    3. Randomly assigns people to seats.
    4. Saves the final seating plan to an output file.
    5. Displays the results in the terminal.
    """
    input_filepath = "new_colleagues.csv"
    output_filename = "output.csv"

    # Step 1: Read all colleague names from the input CSV
    names = read_names_from_csv(input_filepath)

    # Step 2: Create an OpenSpace (6 tables × 4 seats)
    open_space = Openspace(number_of_tables=6, table_capacity=4)

    # Step 3: Randomly assign colleagues to available seats
    open_space.organize(names)

    # Step 4: Save the seating plan to a file
    open_space.store(output_filename)

    # Step 5: Display the assignments in the console
    open_space.display()


if __name__ == "__main__":
    main()
