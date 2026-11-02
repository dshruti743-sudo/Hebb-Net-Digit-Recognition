import numpy as np

# --------------------------------
# TRAINING PATTERNS (DIGITS 0 TO 9)
# --------------------------------

patterns = np.array([

    # 0
    [
        1, 1, 1,
        1,-1, 1,
        1,-1, 1,
        1,-1, 1,
        1, 1, 1
    ],

    # 1
    [
       -1, 1,-1,
        1, 1,-1,
       -1, 1,-1,
       -1, 1,-1,
        1, 1, 1
    ],

    # 2
    [
        1, 1, 1,
       -1,-1, 1,
        1, 1, 1,
        1,-1,-1,
        1, 1, 1
    ],

    # 3
    [
        1, 1, 1,
       -1,-1, 1,
        1, 1, 1,
       -1,-1, 1,
        1, 1, 1
    ],

    # 4
    [
        1,-1, 1,
        1,-1, 1,
        1, 1, 1,
       -1,-1, 1,
       -1,-1, 1
    ],

    # 5
    [
        1, 1, 1,
        1,-1,-1,
        1, 1, 1,
       -1,-1, 1,
        1, 1, 1
    ],

    # 6
    [
        1, 1, 1,
        1,-1,-1,
        1, 1, 1,
        1,-1, 1,
        1, 1, 1
    ],

    # 7
    [
        1, 1, 1,
       -1,-1, 1,
       -1, 1,-1,
        1,-1,-1,
        1,-1,-1
    ],

    # 8
    [
        1, 1, 1,
        1,-1, 1,
        1, 1, 1,
        1,-1, 1,
        1, 1, 1
    ],

    # 9
    [
        1, 1, 1,
        1,-1, 1,
        1, 1, 1,
       -1,-1, 1,
        1, 1, 1
    ]

])

print("Training Patterns:")
print(patterns)

print("\nTraining Pattern Shape:", patterns.shape)


# --------------------------------
# TARGET MATRIX
# --------------------------------

targets = -np.ones((10, 10))

for i in range(10):
    targets[i][i] = 1

print("\nTarget Matrix:")
print(targets)


# --------------------------------
# HEBBIAN LEARNING
# --------------------------------

weights = np.zeros((15, 10))

for i in range(10):
    weights += np.outer(patterns[i], targets[i])

print("\nWeight Matrix:")
print(weights)

print("\nWeight Matrix Shape:", weights.shape)


# --------------------------------
# INPUT PATTERN FUNCTION
# --------------------------------

def get_pattern(message):

    print(message)
    print("Enter 5 rows with 3 values each.")
    print("Use only 1 and -1.")

    test = []

    for i in range(5):

        while True:

            try:
                row = list(map(int, input(f"Enter Row {i+1}: ").split()))

                if len(row) == 3 and all(x in [1, -1] for x in row):
                    test.extend(row)
                    break

                else:
                    print("Invalid input! Enter exactly 3 values (1 or -1).")

            except ValueError:
                print("Invalid input! Enter only integers 1 and -1.")

    return np.array(test)


# --------------------------------
# DIGIT RECOGNITION FUNCTION
# --------------------------------

def recognize_digit(test):

    output = np.dot(test, weights)

    print("\nOutput:")
    print(output)

    recognized_digit = np.argmax(output)

    print("Recognized Digit =", recognized_digit)


# --------------------------------
# NORMAL TEST
# --------------------------------

test = get_pattern("\nNORMAL TEST PATTERN")

recognize_digit(test)


# --------------------------------
# ONE PIXEL ERROR TEST
# --------------------------------

test_error = get_pattern("\nONE PIXEL ERROR TEST")

recognize_digit(test_error)

print("\nProgram Completed Successfully!")
