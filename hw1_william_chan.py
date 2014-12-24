#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
def sortwithloops(input_list):
    x = 0
    while x < len(input_list) - 1:
        temp = input_list[x]
        temp1 = input_list[x + 1]        
        if temp > temp1:
            input_list[x] = temp1
            input_list[x + 1] = temp
            x = 0            
        else:
            x = x + 1                   
    return input_list#return a value

    
#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop
def sortwithoutloops(input_list): 
    input_list.sort()
    return input_list#return a value

    
#3. fill in this function
#   it takes a list for input and a value to search for
#    it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions
def searchwithloops(input_list, value):
    x = 0
    found = False
    while x <= len(input_list) - 1:
        if input_list[x] == value:
            found = True
            return True
        else:            
            x = x + 1
            
    if found == False:
        return False
    

#4. fill in this function
#   it takes a list for input and a value to search for
#    it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input_list, value):
    if value in input_list:
        return True
    else:
        return False 
    

if __name__ == "__main__":    
    L = [5,3,6,3,13,5,6]    

    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
