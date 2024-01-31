def newdice():
    list1 = list(range(1, 5))
    list2 = list(range(1, 12))
    comb1 = []
    comb2 = []
    orgnl = [0.0, 0.0, 0.027777777777777776, 0.05555555555555555, 0.08333333333333333, 0.1111111111111111, 0.1388888888888889, 0.16666666666666666, 0.1388888888888889, 0.1111111111111111, 0.08333333333333333, 0.05555555555555555, 0.027777777777777776]

    def total_comb(dice_A,dice_B):
         return len(dice_A)*len(dice_B)
    
    def find_comb_B(ind,temp):
        if len(temp)==6:
            comb2.append(temp)
            return
        if ind<0:
            return
        find_comb_B(ind-1,temp+[list2[ind]])
        find_comb_B(ind-1,temp)


    def find_comb_A(ind,temp):
        if len(temp)==6:
            comb1.append(temp)
            return
        if ind<0:
            return
        find_comb_A(ind,temp+[list1[ind]])
        find_comb_A(ind-1,temp)
        
        
    def distribution(dice_A,dice_B):
        res = [0 for i in range(max(dice_A)+max(dice_B)+1)]
        for i in dice_A:
            for j in dice_B:
                res[i+j] += 1
        return res
        
    def probabilities(dice_A,dice_B):
        if max(dice_A) + max(dice_B) == 12:
            dist = distribution(dice_A,dice_B)
            ln = total_comb(dice_A,dice_B)
            for event in range(max(dice_A)+max(dice_B)+1):
                if dist[event]:
                    if orgnl[event] != dist[event]/ln:
                        return False
                return True

        return False

    find_comb_B(len(list2) - 1, [])
    find_comb_A(len(list1) - 1, [])
    
    
    dice_sets = []

    for dice_A in comb1:
        for dice_B in comb2:
            if probabilities(dice_A, dice_B):
                dice_sets.append((dice_A, dice_B))
                
    return dice_sets