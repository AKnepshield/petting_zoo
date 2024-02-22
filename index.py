# import the python datetime module to help us create a timestamp
from datetime import date
from walking import Llama, Donkey, Goat, Horse, Bull, Rat
from slithering import CopperheadSnake, RatSnake, Turtle, Gecko, Scorpion
from swimming import MallardDuck, GoldFish, SnappingTurtle
from flying import Parakeet

llama_del_ray = Llama("Llama Del Ray", "Midday")
print(llama_del_ray)
print(
    f"{llama_del_ray.name} the {llama_del_ray.species} is available to pet during the {llama_del_ray.shift}\n"
)
wonkey = Donkey("Wonkey the donkey", "Afternoon")
print(wonkey)
print(
    f"{wonkey.name} the {wonkey.species} is available to pet during the {wonkey.shift}\n"
)
baaba_fett = Goat("Baaba Fett", "Midday")
print(baaba_fett)
print(
    f"{baaba_fett.name} the {baaba_fett.species} is available to pet during the {baaba_fett.shift}\n"
)
copperhead_snake = CopperheadSnake("Krom")
print(copperhead_snake)
print()
rat_snake = RatSnake("Serpentor")
print(rat_snake)
print()
mallard_duck = MallardDuck("Dewey")
print(mallard_duck)
print()
gold_fish = GoldFish("Wanda")
print(gold_fish)
print()
hidalgo = Horse("Hidalgo", "Morning")
print(hidalgo)
print(
    f"{hidalgo.name} the {hidalgo.species} is available to pet during the {hidalgo.shift}\n"
)
turtle = Turtle("Leo")
print(turtle)
print()
splinter = Rat("Splinter", "Afternoon")
print(splinter)
print(
    f"{splinter.name} the {splinter.species} is available to pet during the {splinter.shift}\n"
)
gecko = Gecko("Spike")
print(gecko)
print()
parakeet = Parakeet("Toxie")
print(parakeet)
print()
snapping_turtle = SnappingTurtle("Slash")
print(snapping_turtle)
print()
scorpion = Scorpion("Scorpius")
print(scorpion)
print()
dwayne = Bull("Dwayne", "Morning")
print(dwayne)
print(
    f"{dwayne.name} the {dwayne.species} is available to pet during the {dwayne.shift}\n"
)


# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def add(self, number):
#         real = self.real + number.real
#         imag = self.imag + number.imag
#         result = Complex(real, imag)
#         return result


# n1 = Complex(5, 6)
# n2 = Complex(-4, 2)
# result = n1.add(n2)
# print("real =", result.real)
# print("imag =", result.imag)
