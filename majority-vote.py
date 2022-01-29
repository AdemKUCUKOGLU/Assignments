liste = ["A", "A", "A", "B", "C", "A"]
def majority_vote(lst):
    return max(lst,key=lst.count)
    
#print(majority_vote(liste))

def majority_vote_2(lst):
    count = 0
    dict = {}
    vote = set(lst)
    for i in vote:
        for j in lst:
            if i == j:
                count+=1
        if count > len(lst)/2:
            return i
        else:
            count = 0

    return "no majority found"

print(majority_vote_2(liste))