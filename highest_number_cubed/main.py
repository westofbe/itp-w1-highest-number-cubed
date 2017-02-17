"""This is the entry point of the program."""

def highest_number_cubed(limit):
    previous_number = 1
    
    while True:
        current_number = previous_number + 1
        if current_number ** 3 >= limit:
            return previous_number #when loop ends, set previous number as current to restart loop
        
        previous_number = current_number
        