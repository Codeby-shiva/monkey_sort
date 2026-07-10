import random


def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    
    return True
        
def monkey_sort(arr):
    Round = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        print(arr)
        Round += 1

    print("Round : ",Round)
    
