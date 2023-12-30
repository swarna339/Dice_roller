class Dice:
    def __init__(self, Number_of_faces, Number_of_dice):
        self.Number_of_dice = Number_of_dice
        self.Number_of_faces = Number_of_faces
        self.dice_dict = {}
        self.probability_dict = {}

    # to find total outcomes
    def Total_Outcomes(self):
        print(f"Total_outcomes: {pow(self.Number_of_faces, self.Number_of_dice)}")

    def Display_combinations(self):
        # Calculating and Display of total possible combinations
        counter = 1  # counter is to keep track of combinations

        for i in range(1, self.Number_of_faces + 1):
            for j in range(1, self.Number_of_faces + 1):
                key = "combo_number:" + str(counter)
                # key is the Dictionary's key value , which shows the combinations number
                counter = counter + 1
                value = (f"Die_A:{i}", f"Die_B:{j}", f"Sum:{i + j}")
                # Value stores the DIE_A face number , Die_B face number and the SUM
                self.dice_dict[key] = value
        print(self.dice_dict)
        # Display of our Dictionary

    def Display_probability(self):
        # Find the probability of each sum occurring
        sum_values = [value[2] for value in self.dice_dict.values()]
        # finding the sum values from dictionary
        total_combinations = len(self.dice_dict)
        for value in sum_values:
            if value in self.probability_dict:
                self.probability_dict[value] += 1
            else:
                self.probability_dict[value] = 1

        for key in self.probability_dict:
            self.probability_dict[key] = f"{self.probability_dict[key]}/{total_combinations}"

        print(self.probability_dict)


d = Dice(Number_of_faces=6, Number_of_dice=2)
d.Total_Outcomes()
d.Display_combinations()
d.Display_probability()
