## Love calculator

print("MY Love Calculator")

yourname = input("Enter your name?: \n")
yourpartnername = input("Enter your partnername?: \n")

together = yourname + yourpartnername
lower = together.lower()

t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")

true = t+r+u+e

l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")

love = l + o + v + e

lovestory = str(true) + str(love)
love = int(lovestory)

if (love < 10) or (love > 90):
    print(f"Your love score is (love}")
elif (love >= 40) and (love <=50):
    print(f"Your score is {love}")
else:
    print(f"your score is {love}")

