def solution_station_7(equation: str) -> float:
    # Define the known values
    values = {
        'a': 3,
        'b': -1,
        'c': 4,
        'd': 7,
        'e': 0.5
    }
    
    # Evaluate the expression using these values
    return eval(equation, {}, values)

