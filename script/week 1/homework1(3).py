print("*** welcome to the checkout system ***")

trousers = int(input("How many pairs of trousers have been bought? "))
tshirts = int(input("How many T-shirts have been bought? "))
vests = int(input("How many vests have been bought? "))

total = trousers * 70.5 + tshirts * 20.89 + vests * 100.3

print("You have bought")
print("Trousers:", trousers, "pair(s)")
print("T-shirts:", tshirts, "piece(s)")
print("Vests:", vests, "piece(s)")
print("Total:", total)
