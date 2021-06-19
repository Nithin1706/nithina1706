
goodies = {} # dictionary to store all goodies and their price
dict_to_sort = {}

# input_file = input("Enter the input filename: ")

with open("input.txt",'r') as file:
    c=0 # to get 1st and 3rd line which have number of employes and topic
    for line in file:
        data = line.rstrip("\n")
        if c==0:
            key,val = data.split(":")
            num_of_emp = int(val.replace(" ",""))
        elif c>3:
            key,val = data.split(":")
            if dict_to_sort.get(int(val.replace(" ","")),None):
                dict_to_sort[ int(val.replace(" ",""))].append(key)
                
            else:
                dict_to_sort[ int(val.replace(" ",""))]=[key]
            goodies[key] = int(val.replace(" ",""))
        c+=1

values = list(goodies.values())
# The minimum difference will be among nearest number so values are needed to be sorted
values.sort()

sorted_goodies = {}
#sort the dictioanry according to sorted 
for x in values:
    for key in dict_to_sort[x]:
        sorted_goodies[key]=x


diff_hash = [values[i+1]-values[i] for i in range(len(values)-1)] #difference between consecutive elements is stored in list to reduce complexity

min_diff = sum(diff_hash[:num_of_emp-1])

start_index = 0

for i in range(1,len(diff_hash)-(num_of_emp-2)):
    temp = min_diff
    temp = temp-diff_hash[i-1]
    temp+= diff_hash[i+(num_of_emp-2)]
    
    if temp<min_diff:
        min_diff=temp
        start_index=i 

res = {}
count = 0
for key,val in sorted_goodies.items():
    
    if count>=start_index+num_of_emp:
        break
    elif count>=start_index:
        res[key]=val
    count+=1



with open("output.txt",'w+') as output:
    output.writelines(f"Number of the employees: {num_of_emp}\n")
    output.writelines("\n")
    output.writelines("Here the goodies that are selected for distribution are:\n")
    for key,val in res.items():
        output.writelines(f"{key}: {val}\n")
    
    output.writelines("\n")
    output.writelines(f"And the difference between the chosen goodie with highest price and the lowest price is {min_diff}")