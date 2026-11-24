
scores = list(map(int, input("Enter scores: ").split()))

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum =", total)
print("Average =", average)

