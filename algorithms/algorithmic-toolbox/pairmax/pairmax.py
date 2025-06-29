
import sys

#ListLength = int(input("Enter list length: "))
#PairsListInput = input("Pairs: \n")
MaxPairList = [2, 2, 13, 1, 1, -8, 3, 2]#PairsListInput.split(" ")

#if len(MaxPairList) != ListLength:
#    print("Wrong list length")
#    exit(1)

for i, j in enumerate(MaxPairList):    # Just showing myself example of enumerate
    print(f"index: {i} element: {j}")    

i_max, v_max = max(enumerate(MaxPairList), key=lambda x:x[1])    # Define max value with max() built-in function. 
                                                                 # Pass enumerated list creating index-value pair objects. 
                                                                 # 'key' paramter of the max() function passed through
                                                                 # lambda function to tell the max() function that estimated value 
                                                                 # has posision '1' in the enumerate object.
                                                                 # posision '0' is for index.
print(i_max, v_max)
i_second_max, v_second_max = max([t for t in enumerate(MaxPairList) if t[0] != i_max], key=lambda x:x[1])
print(i_second_max,v_second_max)

sec_list = [a for a in enumerate(MaxPairList) if a[0] != i_max]    # Here I can see how enumerate creates objects of index-value pairs
print(sec_list)

# Here is a bit longer notation to do the same job
# I explicitly save all numbers with their positons in a temp list excluding first Max numbres
# Search through the temp list for second Max
# In case we need original indecies of both max numbers we have them as well.
def findMaxProduce(pairs):
    print("\n\nEntering function..")
    temp_list = []
    print(f"List of pairs: {pairs}")
    print(f"Enumerated list of pairs: {list(enumerate(pairs))}")
    max_val = max(pairs)
    max_val_index = pairs.index(max_val)
    print(f"First MAX: {max_val},   index: {max_val_index}")
    for p in enumerate(pairs):
        if p[0] != max_val_index:
            temp_list.append(p)
    print(f"Temp list of enum objects: {temp_list}")
    sec_max_val_index, sec_max_val = max(temp_list, key=lambda x:x[1])
    print(f"Second MAX: {sec_max_val},    index: {sec_max_val_index}")
    print(f"Produce of 2 MAX elements: {max_val * sec_max_val}")


findMaxProduce(MaxPairList)

