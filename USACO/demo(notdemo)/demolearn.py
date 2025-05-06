# Open the file in read mode
f = open("demoin.in")
# Read all lines from the file into a list
numbers = f.readlines()
f.close()

# Access the first line, strip any leading/trailing spaces, and split it into a list
line = numbers[0].strip().split()

# Convert the first three elements to integers
M = int(line[0])
N = int(line[1])
K = int(line[2])
# Print the values to verify
print("M:", M)
print("N:", N)
print("K:", K)


with open("demoin.in", 'r') as numbers2:
    numbers2.readline()
    signal = []
#--------------------------------- Adds signal to list
    for x in range(M):
        number = numbers2.readline().strip()
        signal.append(number)
#--------------------------------- Adds new signal to anouther list
    signal_out = []
    line_out = ""
    #-
    for line in signal:
        for char in line:
            #-
            if len(line_out) >= 8: #will be replaced with - len(line_out) >= size*2
                signal_out.append(line_out) #will be replaced with - for x in range(0, size): signal_out.append(line_out)
                signal_out.append(line_out)
                line_out = ""
            #-
            if char == 'X': #xxx. xxxxxx..
                line_out += 'XX' #Will be replaced with - for x in range(0, size): line_out += 'X'
            elif char == '.':
                line_out += '..'
    if line_out:
        signal_out.append(line_out)
        signal_out.append(line_out)
#---------------------------------- End of code
print(signal)
print(signal_out)
with open("demoout.out", "w") as outfile:
    for line in signal_out:
        outfile.write(line+'\n')
        
'''
XXXXXX..
XXXXXX..
XX....XX
XX....XX
XXXXXX..
XXXXXX..
XX....XX
XX....XX
XXXXXX..
XXXXXX..

'''

