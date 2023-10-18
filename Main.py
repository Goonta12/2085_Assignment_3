from mode1 import Mode1Navigator
from island import Island

a = Island("A", 400, 100)
b = Island("B", 300, 150)
c = Island("C", 100, 5)
d = Island("D", 350, 90)
e = Island("E", 300, 100)
        # Create deepcopies of the islands
islands = [
    Island(a.name, a.money, a.marines),
    Island(b.name, b.money, b.marines),
    Island(c.name, c.money, c.marines),
    Island(d.name, d.money, d.marines),
    Island(e.name, e.money, e.marines),
    ]

nav = Mode1Navigator(islands, 200)

for i in nav.Islands:
    print(i)

print(nav.select_islands())

