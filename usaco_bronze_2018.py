
'''
10 3
11 4
12 5
'''

def pour_milk(amount1, limit2, amount2):
    if amount1 + amount2 <= limit2:
        amount1_new = 0
        amount2_new = amount1 + amount2
    else:
        amount2_new = limit2
        amount1_new = (amount1+amount2)-limit2
    return amount1_new, amount2_new

def mix_milk(c1, m1, c2, m2, c3, m3):
    count = 1
    for x in range(0, 100):
        if count > 3:
            count = 1
        #main run code
        if count == 1:
            m1, m2 = pour_milk(m1, c2, m2)
            count += 1

        elif count == 2:
            m2, m3 = pour_milk(m2, c3, m3)
            count += 1

        elif count == 3:
            m3, m1 = pour_milk(m3, c1, m1)
            count += 1

    return m1, m2, m3



def main():
    # Read input from mixmilk.in
    with open('mixmilk.in', 'r') as infile:
        c1, m1 = map(int, infile.readline().strip().split())
        c2, m2 = map(int, infile.readline().strip().split())
        c3, m3 = map(int, infile.readline().strip().split())
    # Perform the mixing process
    m1, m2, m3 = mix_milk(c1, m1, c2, m2, c3, m3)
    # Write output to mixmilk.out
    with open('mixmilk.out', 'w') as outfile:
        outfile.write(f'{m1}\n{m2}\n{m3}\n')
    print("mixmilk.out successfully written")
# Execute the main function
if __name__ == '__main__':
    main()