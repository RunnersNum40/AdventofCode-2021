import numpy as np
from scipy.stats import mode

file_name = "input.txt"
with open(file_name, "r") as file:
    # Convert to a 2d array 
    data = np.array([list(map(int, line.strip())) for line in file])

def decimal(arr, carry=0):
    # Take a binary number in list form and reduce to an integer
    l = len(arr)
    if l==1:
        return carry+arr[0]
    else:
        return carry+arr[0]*2**(l-1)+decimal(arr[1:], carry)

# Part 1
def part1(data):
    # Take the mode of each column
    gamma = np.array(mode(data)[0][0])
    # Reverse each item 0->1, 1->0
    epsilon = 1-gamma

    # Convert to decimal
    gamma = decimal(gamma, 0)
    epsilon = decimal(epsilon, 0)

    return gamma*epsilon

# Part 2
def part2(data):
    # Find the most common bits in each column
    most_common = np.array(mode(data)[0][0])

    # Copy data to two new arrays
    o2, co2, = map(np.copy, (data, data))

    for n in range(data.shape[1]):
        print(n, mode(list(o2[:,n])+[1])[0][0])
        o2 = o2[o2[:,n]==mode(list(o2[:,n])+[1])[0][0]] if o2.shape[0]>1 else o2
        co2 = co2[co2[:,n]!=mode(list(co2[:,n])+[1])[0][0]] if co2.shape[0]>1 else co2
        print("O2:", o2.shape[0], o2)

    print(o2, co2)
    o2, co2 = map(decimal, (o2[0], co2[0]))
    print(o2, co2)
    return o2*co2


#Running
print("Part 1:", part1(data)) # 4001724
print("Part 2:", part2(data)) # 587895