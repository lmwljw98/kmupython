def tax(price, tax_rate):
    total = price + (price * tax_rate)
    global my_price
    my_price = my_price + 200
    return total

my_price = float(input("Yours : "))

totalPrice = tax(my_price, 0.06)

print(my_price, totalPrice)

