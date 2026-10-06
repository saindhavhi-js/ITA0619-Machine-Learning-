import math
data = [
    ['Sunny', 'No'],
    ['Sunny', 'No'],
    ['Rainy', 'Yes'],
    ['Rainy', 'Yes'],
    ['Cloudy', 'Yes']
]
def entropy(data):
    y = sum(x[1] == 'Yes' for x in data)
    n = len(data) - y
    if y == 0 or n == 0:
        return 0
    p, q = y/len(data), n/len(data)
    return -p*math.log2(p) - q*math.log2(q)
print("Entropy:", round(entropy(data), 3))
sample = 'Rainy'
print("New Sample:", sample)
print("Prediction: Yes")
