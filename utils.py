def geometric_progression_value(min_val, max_val, current_iteration):
    # Constants
    total_numbers = 50
    numbers_per_week = 7
    total_weeks = total_numbers // numbers_per_week
    
    # Determine the overall GP ratio for the end values of the weeks
    overall_weekly_gp_ratio = (max_val / min_val) ** (1 / (total_weeks - 1))
    
    # Calculate the weekly final values to ensure they form the general GP
    weekly_final_values = [min_val * (overall_weekly_gp_ratio ** week) for week in range(total_weeks)]
    
    # Corrected: Adjust for accessing the weekly final value within range
    weekly_final_values.append(max_val)  # Ensure the last value matches the max_val
    
    # Determine which week (subsequence) the current iteration belongs to
    week_number = (current_iteration - 1) // numbers_per_week
    
    # Determine the start and end values for the subsequence
    start_val = min_val if week_number == 0 else weekly_final_values[week_number - 1]
    end_val = weekly_final_values[week_number]
    
    # Calculate the GP ratio for this week's progression
    subsequence_gp_ratio = (end_val / start_val) ** (1 / (numbers_per_week - 1))
    
    # Position of the current iteration within its week
    position_in_week = (current_iteration - 1) % numbers_per_week
    
    # Calculate and return the value at the current iteration
    value_at_iteration = start_val * (subsequence_gp_ratio ** position_in_week)
    
    return value_at_iteration
