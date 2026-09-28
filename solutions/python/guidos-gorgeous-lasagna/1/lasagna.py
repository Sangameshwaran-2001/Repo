import time
EXPECTED_BAKE_TIME = 40
def bake_time_remaining(value):
    return EXPECTED_BAKE_TIME-value
def preparation_time_in_minutes(number_of_layers):
    return (number_of_layers*2)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + elapsed_bake_time
total_bake_timing= bake_time_remaining(10)

