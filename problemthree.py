from fractions import Fraction
def calculate_probability():
    
    results = {}
    
    for die_a in range(1, 7):
        for die_b in range(1, 7):
            total_sum = die_a + die_b
            if total_sum in results:
                results[total_sum] += 1
            else:
                results[total_sum] = 1
    
    total_combinations = 6 * 6
    probabilities = {sum_: Fraction(count, total_combinations)  for sum_, count in results.items()}
    
    return probabilities