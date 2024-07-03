from random import randint, choice
import math

'''
This module determines the positions to use for each image sample,
based on the input provided in the run() method.

Initially, the code divides the main image field into an n*n grid
of equally sized subdivisions, where n is an integer between 1 and 3.

Next, each of the three samples to be generated is uniquely assigned
to one of these subdivisions selected at random,
preventing any overlapping samples.

Finally, the position of each sample within its respective
subdivision is calculated. This involves applying
a random offset to each sample.

The resulting positions of each sample are then returned
to the invoking module, which generates the samples
using the supplied positions.
'''

FIELD = [0, 0]
SAMPLE_WIDTH = 0
SAMPLE_HEIGHT = 0
SAMPLE_SIZE = 3


def error_check():

    # This ensures that the image is large enough
    # to accommodate all the required samples.

    if SAMPLE_WIDTH * SAMPLE_SIZE > FIELD[0]:
        if SAMPLE_HEIGHT * SAMPLE_SIZE > FIELD[1]:
            raise ValueError(f"Cannot take {SAMPLE_SIZE} non-overlapping"
                             f"samples of dimension"
                             f"{SAMPLE_WIDTH}x{SAMPLE_HEIGHT}"
                             f"in field of size {FIELD[0]}x{FIELD[1]}.")


def calculate_subdivision_array_dimension(sample_length, field_length):

    # This determines whether the image will be divided
    # into one, two, or three subdivisions along a given axis.

    if sample_length > field_length:
        raise ValueError(f"Sample dimension {sample_length} is"
                         f"greater than image dimension {field_length}.")
    quotient = field_length / sample_length
    if quotient >= 3:
        return 3
    if quotient >= 2:
        return 2
    return 1


def calculate_sample_position(
        subdivision_index_x,
        subdivision_index_y,
        subdivision_width,
        subdivision_height
        ):

    # Within each occupied subdivision, the position
    # of the sample to be generated is calculated at random.
    x_displacement = randint(0, subdivision_width - SAMPLE_WIDTH)
    y_displacement = randint(0, subdivision_height - SAMPLE_HEIGHT)
    x = ((subdivision_index_x) * subdivision_width) + x_displacement
    y = ((subdivision_index_y) * subdivision_height) + y_displacement
    return [x, y]


def run(field_x, field_y, sample_width, sample_height, sample_size):
    global FIELD, SAMPLE_WIDTH, SAMPLE_HEIGHT, SAMPLE_SIZE
    FIELD = [field_x, field_y]
    SAMPLE_WIDTH = sample_width
    SAMPLE_HEIGHT = sample_height
    SAMPLE_SIZE = sample_size
    error_check()
    subdivision_array_width = calculate_subdivision_array_dimension(
                            SAMPLE_WIDTH, FIELD[0])
    subdivision_array_height = calculate_subdivision_array_dimension(
                            SAMPLE_HEIGHT, FIELD[1])
    subdivision_width = math.floor(FIELD[0]/subdivision_array_width)
    subdivision_height = math.floor(FIELD[1]/subdivision_array_height)
    # Generating the array of subdivisions
    # into which the image will be divided.
    subdivision_array_x_values = [
        i for i in range(0, subdivision_array_width)]
    subdivision_array_y_values = [
        j for j in range(0, subdivision_array_height)]
    subdivision_array = [
        [k, l] for k in subdivision_array_x_values
        for l in subdivision_array_y_values]
    samples = []
    for n in range(0, SAMPLE_SIZE):
        # Each sample is assigned to a subdivision at random.
        # Its position within its subdivision is then calculated.
        subdivision_indices = choice(subdivision_array)
        subdivision_array.remove(subdivision_indices)
        samples.append(calculate_sample_position(
            subdivision_indices[0],
            subdivision_indices[1],
            subdivision_width,
            subdivision_height))
    return samples
