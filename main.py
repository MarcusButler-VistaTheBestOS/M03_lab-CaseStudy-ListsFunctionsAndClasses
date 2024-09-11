# AUTHOR: Marcus Ed. Butler
# VERSION: 2024-9-10
# REVSION: 0
# DESCRIPTION: 

class Vechicle:
    def __init__(self, type):
        self.type = type


class Automobile(Vechicle):
    def __init__(self, year, make, model, doors, sun_roof):
        super().__init__(type="car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.sun_roof = sun_roof
        

vechiles = ('car', 'truck', 'plane', 'boat')

run = True
# MAIN LOOP
while run:
    # Ask user what type of vechile they are using.
    while True:
        type = input("What is the vechicle type? (car, truck, plane, boat, broomstick'my favorite way to travel' > ")

        if type in vechiles:
            if type == 'car':
                break
        else:
            print("That is not a type of vechicle. Please try again.")

    # Ask user for year.
    while True:
        # Is the year typed correctly.
        try:
            year = int(input("What year was the car manufactered? EX: 1998 > "))
        except ValueError:
            ## Is the year a number.
            print("Try again, The year needs to be a number.")
            continue  

        # Does it contain 4 numbers.
        if len(str(year)) != 4:
            print("Try again, the year needs 4 numbers.")

        else:
            break
            
    # Ask the user for the make
    while True:
        make = input("What is the make? EX: Toyota, Honda >")

        # Did user enter a value?
        if make != '':
            break
        else:
            print("Please type a value.")

    # Ask the user for the model
    while True:
        model = input("What is the model? EX: Fit, Corolla, Rav4 >")
        # Did user enter a value?
        if model != '':
            break
        else:
            print("Please type a value.")

    # Ask the user how many doors are on the vechile.
    while True:
        try:
            doors = int(input("How many doors does the vechile have? EX: 2, 4 >"))
        except ValueError:
            print("Try again, Must be a number.")
        else:
            break

    # Ask the user if the vechile has a sun roof.
    while True:
        sun_roof = input("Does the vechicle have a sun roof?[y,n] >")

        if sun_roof == 'y':
            sun_roof = True
            break
        elif sun_roof == 'n':
            sun_roof = False
            break
        else:
            print("Try again, Answer must be y or n.")
    

    car = Automobile(year, make, model, doors, sun_roof)

    print("Vechicle type:", car.type)
    print("Year:", car.year)
    print("Make:", car.make)
    print("Model:", car.model)
    print("Number of doors:", car.doors)
    print("Sun roof:", car.sun_roof)

    
        
