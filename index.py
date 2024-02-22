# import the python datetime module to help us create a timestamp
from datetime import date
from walking import Llama, Donkey, Goat, Horse, Bull, Rat
from slithering import CopperheadSnake, RatSnake, Turtle, Gecko, Scorpion
from swimming import MallardDuck, GoldFish, SnappingTurtle
from flying import Parakeet

llama = Llama("Llama Del Ray")
print(llama)
donkey = Donkey("Wonkey the donkey")
print(donkey)
goat = Goat("Baaba Fett")
print(goat)
copperhead_snake = CopperheadSnake("Krom")
print(copperhead_snake)
rat_snake = RatSnake("Serpentor")
print(rat_snake)
mallard_duck = MallardDuck("Dewey")
print(mallard_duck)
gold_fish = GoldFish("Wanda")
print(gold_fish)
horse = Horse("Hidalgo")
print(horse)
turtle = Turtle("Leo")
print(turtle)
rat = Rat("Splinter")
print(rat)
gecko = Gecko("Spike")
print(gecko)
parakeet = Parakeet("Toxie")
print(parakeet)
snapping_turtle = SnappingTurtle("Slash")
print(snapping_turtle)
scorpion = Scorpion("Scorpius")
print(scorpion)
bull = Bull("Dwayne")
print(bull)


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
