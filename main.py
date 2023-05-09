# Tyler Gregory
# 5.08.2023
# Coding Challenge 1

# part 1
p = input()
n = input()
r = input()

p, n, r = int(p), int(n), int(r)

interest = (p * n * r) / 100
print(interest)

# part 2
favorite = ["pizza", "salad", "sushi", "tacos", "pasta"]
print(favorite[2])
favorite.append("lentejas")
print(favorite)

# part 3
for i in range(5):
    print("I am a programmer")

for i in range (9):
    print((i + 1)**2)