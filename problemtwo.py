def display_combinations():
    dice_dict = {}
    # Calculating and Display of total possible combination
    counter = 1
    # counter is to keep track of combinations
    for i in range(1, 7):
        for j in range(1, 7):
            key = "combo_number:" + str(counter)
            # key is the Dictionary's key value, which shows the combinations number
            counter += 1
            value = {"Die_A": i, "Die_B": j, "Sum": i + j}
            # Value stores the DIE_A face number, Die_B face number and the SUM
            dice_dict[key] = value
    return dice_dict