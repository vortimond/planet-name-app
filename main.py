import random

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
attempts = 0
random_planet = random.choice(planets)
random_number = planets.index(random_planet)
print("\nI have selected a planet from eight possible options:")
print("Planets:")
print(planets)
while True:
    user_planet = input("\nTell me which one ['q' to quit]: ")
    user_planet = user_planet.capitalize()
    attempts += 1
    if user_planet in planets:
        user_number = planets.index(user_planet)
        if random_number == user_number:
            print("Correct!")
            print(f"The selected planet was: {random_planet}")
            print(f"You nedded {attempts} attempts.")
            break
        elif random_number > user_number:
            print("The planet is farther away from the Sun.")
        else:
            print("The planet is closer to the Sun.")
    elif user_planet == "Q":
        break
    else:
        print(f"'{user_planet}' is not a planet.")
