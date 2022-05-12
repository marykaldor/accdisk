# Open old file in read mode and create new file in write mode
fin = open("/Users/marykaldor/accdisk/fortran/" + "parfile_original.dat", "r")
fout = open("/Users/marykaldor/accdisk/fortran/" + "parfile.dat", "w")

# Setting up list iterations
i = 0
parameters = []

# Give system parameter to change
adjust = input("What would you like to change? ")
parameters.append(adjust)

while i < 27:
    # Check for more parameters. If there are none, end loop.
    if input("Would you like to change anything else? ") == "Yes":
        adjust = input("What would you like to change? ")
        parameters.append(adjust)
        i += 1
    else:
        i = 27

# Setting up range over which to iterate
j = 0
k = len(parameters) - 1

# Go through text and only change given parameter's value
# Everything else just gets rewritten to the new file
while j < k:
    for line in fin:
        if parameters[j] in line:
            x = line.split()
            if parameters[j] == x[1]:
                print("The current value of ", parameters[j], " is ", x[0])
                adjust2 = input("What value would you like to use? ")
                fout.write(line.replace(x[0], adjust2))
                if parameters[j] == parameters[-1]:
                    pass
                else:
                    j += 1
            else:
                fout.write(line)
        else:
            fout.write(line)
    
fin.close()
fout.close()

print("Done")
