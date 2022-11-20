ages = [5, 12, 17, 18, 24, 32]

adults = list(filter(lambda x: False if x < 18 else True, ages))

print(adults)
