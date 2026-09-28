EXPECTED_BAKE_TIME = 40

def bake_time_remaining(value):
    """Calculate the remaining bake time."""
    return EXPECTED_BAKE_TIME - value

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time."""
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time."""
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + elapsed_bake_time