info = ["7868190130M7522","5303914400F9211","9273338290F4010"]

count = 0
def find():
    global count
    for x in info:
        if x[11] >= '6':
            count = count + 1
find()
print(count)