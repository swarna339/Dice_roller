
Given Problem:
Part-A:
Consider two six-sided faces namely Die A and Die B with faces numbered from 1 to 6. Both the dice are rolled together.
1.	How many total combinations are possible? Show the math along with the code?
2.	Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together.
3.	Calculate the Probability of all Possible Sums occurring among the number of combinations

Part-B:
You have the tools to re-attach the “Spots” back on the Dice.
However, Loki has doomed your dice with the following conditions:
● Die A cannot have more than 4 Spots on a face.
● Die A may have multiple faces with the same number of spots.
● Die B can have as many spots on a face as necessary i.e. even more than 6.
But in order to play your game, the probability of obtaining the Sums must remain the
same!
So if you could only roll P(Sum = 2) = 1/X, the new dice must have the spots reattached
such that those probabilities are not changed.
Input:
● Die_A = [1, 2, 3, 4, 5, 6] & Die B = Die_A = [1, 2, 3, 4, 5, 6]
Output:
● A Transform Function undoom_dice that takes (Die_A, Die_B) as input &
outputs New_Die_A = [?, ?, ?, ?, ?, ?],New_Die_B = [?, ?,
?, ?, ?, ?] where,
● No New_Die A[x] > 4

Solution :
I have solved this using Python Flask web Frame work and diplay the results with Html and Css elements

To Run this :
 Flask should be installed in your system and support the anaconda environment .

 
 Then open this project in your github 

 
  Run command : flask run
 
