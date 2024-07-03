from random import randint, choice
import math

FIELD = [1000,1000]
SAMPLE_WIDTH = 100
SAMPLE_HEIGHT = 20
SAMPLE_SIZE = 3

def error_check():
    if SAMPLE_WIDTH * SAMPLE_SIZE > FIELD[0]:
        if SAMPLE_HEIGHT * SAMPLE_SIZE > FIELD[1]:
            raise ValueError(f"Cannot take {SAMPLE_SIZE} non-overlapping samples of dimension {SAMPLE_WIDTH}x{SAMPLE_HEIGHT} in field of size {FIELD[0]}x{FIELD[1]}.")

def calculate_slot_array_dimension(sample_length, field_length):
    if sample_length > field_length:
        raise ValueError(f"Sample dimension ({sample_length}) greater than image dimension ({field_length}).")
    quotient = field_length / sample_length
    if quotient >= 3:
        return 3
    if quotient >= 2:
        return 2
    return 1

def calculate_sample_position(
        slot_index_x, 
        slot_index_y,
        slot_width,
        slot_height   
    ):
    print(f"Making sample in slot: {slot_index_x},{slot_index_y}")
    x_displacement = randint(0, slot_width - SAMPLE_WIDTH)
    y_displacement = randint(0, slot_height - SAMPLE_HEIGHT)
    x = ((slot_index_x) * slot_width) + x_displacement
    y = ((slot_index_y) * slot_height) + y_displacement
    print(f"Made sample at: {x},{y}")
    return [x,y]

def has_overlap(box1, box2):
    return all(
        high1 >= low2 and high2 >= low1
        for low1, high1, low2, high2 in zip(*box1, *box2)
    )

def run(field_x, field_y, sample_width, sample_height, sample_size):
    global FIELD, SAMPLE_WIDTH, SAMPLE_HEIGHT, SAMPLE_SIZE
    FIELD = [field_x, field_y]
    SAMPLE_WIDTH = sample_width
    SAMPLE_HEIGHT = sample_height
    SAMPLE_SIZE = sample_size
    error_check()
    slot_array_width = calculate_slot_array_dimension(SAMPLE_WIDTH,FIELD[0])
    slot_array_height =  calculate_slot_array_dimension(SAMPLE_HEIGHT,FIELD[1])
    print(f"slot array size: {slot_array_width}x{slot_array_height}")
    slot_width = math.floor(FIELD[0]/slot_array_width)
    slot_height = math.floor(FIELD[1]/slot_array_height)
    print(f"Slot size: {slot_width}x{slot_height}")
    slot_array_x_values = [i for i in range(0,slot_array_width)]
    slot_array_y_values = [j for j in range(0,slot_array_height)]
    slot_array = [[k, l] for k in slot_array_x_values for l in slot_array_y_values]
    samples = []
    for n in range(0, SAMPLE_SIZE):
        slot_indices = choice(slot_array)
        slot_array.remove(slot_indices)
        samples.append(calculate_sample_position(slot_indices[0],slot_indices[1],slot_width,slot_height))
    return samples  


