def random_number_generator():
    import random
    min=int(input("Minumum Value?"))
    max=int(input("Maximum value?"))
    random_number=random.randint(min,max)
    print(random_number)
random_number_generator()
