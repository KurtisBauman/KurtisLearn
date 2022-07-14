my_numbers = [4, 9, 10, 25]
animals = ["rabbit", "duck", "duck","worker"]
animals.sort()
my_numbers.reverse()
animals.extend(my_numbers)
animals.append("Dom")
animals.insert(1, "ant")
animals.remove("worker")
animals.pop()
print(animals)
print(animals.index("ant"))
print(animals.count("duck"))
animals2 = animals.copy()
print(animals2)

