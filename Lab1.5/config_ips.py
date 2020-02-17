import glob

template = 'ip address'

file_list = glob.glob('config_files\*')
address_list=[]

for filename in file_list:
    with open(filename) as file:
        for line in file:
            if line.find(template) != -1:
                address_list.append(line.strip())


list1 = list(set(address_list))
list2 = []
for line in list1:
    if line.find(template) == 0:
        if line[11] in "0123456789":
            list2.append(line)

display_list = list2

for line in display_list:
    print(line)