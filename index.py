# import the python datetime module to help us create a timestamp
from datetime import date
from walking import Llama, Donkey, Goat, Horse, Bull, Rat
from slithering import CopperheadSnake, RatSnake, Turtle, Gecko, Scorpion
from swimming import MallardDuck, GoldFish, SnappingTurtle
from flying import Parakeet

llama_del_ray = Llama("Llama Del Ray", "Midday", "Llama Chow")
print(llama_del_ray)
# llama_del_ray.feed()
print()
#     f"{llama_del_ray.name} the {llama_del_ray.species} is available to pet during the {llama_del_ray.shift}\n"
# )

wonkey = Donkey("Wonkey the donkey", "Afternoon", "Donkey Chow")
print(wonkey)
# wonkey.feed()
print()
#     f"{wonkey.name} the {wonkey.species} is available to pet during the {wonkey.shift}\n"
# )

baaba_fett = Goat("Baaba Fett", "Midday")
print(baaba_fett)
print()
#     f"{baaba_fett.name} the {baaba_fett.species} is available to pet during the {baaba_fett.shift}\n"
# )

krom = CopperheadSnake("Krom", "Snake Chow")
print(krom)
# krom.feed()
print()

serpentor = RatSnake("Serpentor", "Snake Chow")
print(serpentor)
# serpentor.feed()
print()

dewey = MallardDuck("Dewey", "Duck Chow")
print(dewey)
# dewey.feed()
print()

wanda = GoldFish("Wanda")
print(wanda)
# wanda.feed()
print()

hidalgo = Horse("Hidalgo", "Morning", "Horse Chow")
print(hidalgo)
# hidalgo.feed()
print(
    # f"{hidalgo.name} the {hidalgo.species} is available to pet during the {hidalgo.shift}\n"
)

leo = Turtle("Leo", "Turtle Chow")
print(leo)
# leo.feed()
print()

splinter = Rat("Splinter", "Afternoon", "Rat Chow")
print(splinter)
# splinter.feed()
print(
    # f"{splinter.name} the {splinter.species} is available to pet during the {splinter.shift}\n"
)

spike = Gecko("Spike", "Gecko Chow")
print(spike)
# spike.feed()
print()

toxie = Parakeet("Toxie", "Parakeet Chow")
print(toxie)
# toxie.feed()
print()

slash = SnappingTurtle("Slash", "Snapping Turtle Chow")
print(slash)
# slash.feed()
print()

scorpius = Scorpion("Scorpius", "Scorpion Chow")
print(scorpius)
# scorpius.feed()
print()

dwayne = Bull("Dwayne", "Morning", "Bull Chow")
print(dwayne)
# dwayne.feed()
print(
    # f"{dwayne.name} the {dwayne.species} is available to pet during the {dwayne.shift}\n"
)
