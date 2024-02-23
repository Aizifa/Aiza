def unique_elements(l):
    new_list = []
    i = 0
    while i < len(l):
        t_or_f = True
        j = 0
        while j < i:
            if l[i] == l[j]:
                t_or_f = False
            j += 1
        if t_or_f:
            new_list.append(l[i])
        i += 1
    return new_list

l = input()
elements = l.split()
new_list = unique_elements(elements)
print(new_list)



def unique_elements(ilist):
    
    unique_list = []
   
    for item in ilist:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list


ilist = input()
print(unique_elements(ilist))