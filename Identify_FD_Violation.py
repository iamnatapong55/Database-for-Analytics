# Midterm Part4 Question#4c

with open('Midterm_Part4B.txt', 'r') as file:
    content = file.readlines()           # read all lines
    cName = {}                           # set dictionary
    key = []                             # set list
    for row in content:
        line = row.split(',')
        if line[4] == 'None':            # None value in CName column
            continue
        elif line[4] not in key:
            cName[line[4]] = line[-2]    # Assign dictionary
            key.append(line[4])          # Add in list
        elif line[4] in key and line[-2] != cName[line[4]]:   # Check condition
            print('This line has violated the functional dependency of the CName -> Credits\n', line)


