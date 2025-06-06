mat_data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

def write_matrix_to_file(data, filename):
    with open(filename, "w") as file_out:
        file_out.write(f"{len(data)} {len(data[0])}\n")
        for row in data:
            file_out.write(" ".join(str(num) for num in row) + "\n")
    print(f"Matrix saved to '{filename}'.")

def read_matrix_from_file(filename):
    loaded_matrix = []
    try:
        with open(filename, "r") as file_in:
            lines = [line.strip() for line in file_in if line.strip()]
            for idx, line in enumerate(lines):
                tokens = line.split()
                if idx == 0:
                    rows, cols = int(tokens[0]), int(tokens[1])
                else:
                    row_values = []
                    for token in tokens:
                        if token == "//":
                            break
                        row_values.append(int(token))
                    if len(row_values) == cols:
                        loaded_matrix.append(row_values)
        print("Matrix loaded from file:")
        for row in loaded_matrix:
            print(row)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

input_filename = "matrix_input.in"
output_filename = "matrix_output.out"

while True:
    print("\nMenu:")
    print("1. Load matrix from file")
    print("2. Save matrix to file")
    print("3. Exit")
    
    try:
        choice = int(input("Select an option (1, 2, or 3): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        read_matrix_from_file(input_filename)
    elif choice == 2:
        write_matrix_to_file(mat_data, output_filename)
    elif choice == 3:
        print("Exiting program.")
        break
    else:
        print("Invalid option. Try again.")
