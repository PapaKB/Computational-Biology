import numpy as np

# These labels are for both the columns and rows of blosum50.txt
labels = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
blosum50 = np.array(np.loadtxt('blosum50.txt'))
d = -8


# Function to check if substitution exists and return a value
def check(char1, char2):
    try:
        char1index = labels.index(char1.upper())
    except ValueError:
        return None
    try:
        char2index = labels.index(char2.upper())
    except ValueError:
        return None

    substitution_value = blosum50[char1index][char2index]
    return substitution_value


# Traverses through matrix to construct aligned words starting from the bottom right corner
def traverse_backwards(matrix, string1, string2):
    rows = len(matrix)-1
    columns = len(matrix[0])-1

    aligned1 = ''
    aligned2 = ''

    # Aligned strings are constructed backwards
    while rows >= 0 and columns >= 0:
        (_, direction) = matrix[rows][columns]

        if direction == 'diag':
            aligned1 += string1[rows-1]
            aligned2 += string2[columns-1]
            rows -= 1
            columns -= 1
        elif direction == 'up':
            aligned1 += string1[rows-1]
            aligned2 += '-'
            rows -= 1
        elif direction == 'left':
            aligned1 += '-'
            aligned2 += string2[columns-1]
            columns -= 1
        else:
            break

    aligned1 = aligned1[::-1]
    aligned2 = aligned2[::-1]

    return aligned1, aligned2


# Creates a matrix/ 2d array that is populated with tuples of numbers and directions
# string1 is the vertical string1 in the matrix, string2 is the horizontal string1
def alignment(string1, string2):
    # By setting data type to object every value in the matrix can be a tuple of (number, direction)
    matrix = np.empty((len(string1) + 1, len(string2) + 1), object)

    # The first value in the matrix (0, 0) is 0 and it has no direction as no characters of strings align
    # to this point
    matrix[0, 0] = (0, 'none')

    # Iterates through top row of matrix and adds d to every left column value as there are no
    # substitution values for this row
    for j in range(1, len(string2)+1):
        matrix[0, j] = (matrix[0][j-1][0]+d, 'left')

    # Iterates through first column of matrix and adds d to every above value as there are no
    # substitution values for this column
    for i in range(1, len(string1)+1):
        matrix[i, 0] = (matrix[i-1][0][0]+d, 'up')

    # Populates matrix with the correct number and direction pairs
    for i in range(len(string1)):
        for j in range(len(string2)):
            try:
                diagonal_value = matrix[i][j][0]
                up_value = matrix[i][j+1][0]
                left_value = matrix[i+1][j][0]
                substitution_value = check(string1[i], string2[j])

                new_value_up = up_value + d
                new_value_left = left_value + d

                if substitution_value is not None:
                    new_value_diag = diagonal_value + substitution_value
                else:
                    new_value_diag = new_value_up - 100

                max_value = max(new_value_diag, new_value_up, new_value_left)

                if max_value == new_value_diag:
                    matrix[i+1][j+1] = (new_value_diag, "diag")
                elif max_value == new_value_up:
                    matrix[i+1][j+1] = (new_value_up, "up")
                else:
                    matrix[i+1][j+1] = (new_value_left, "left")

            except TypeError:
                print('Type error should NOT have occurred if order of operations is correct')

    # print(matrix)
    return traverse_backwards(matrix, string1, string2)


def main():
    print(alignment('PAWHEAE', 'HEAGAWGHEE'))
    print(alignment('SALPQPTTPVSSFTSGSMLGRTDTALTNTYSAL', 'PSPTMEAVTSVEASTASHPHSTSSYFATTYYHLY'))


# This will call the main function when code is run
if __name__ == "__main__":
    main()
