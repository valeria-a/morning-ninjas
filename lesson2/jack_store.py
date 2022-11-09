# Science fiction books: $58
# Comics: $32
# History books: $24
# There are discounts for clients who buy multiple books. The discounts work as follows:
#     10% off science fiction books if a customer buys 3 or more science fiction books. The discount is on science fiction books only.
# 2 +1 on history books
# $20 off if the total price of the purchase exceeds $300

sci_fi_books = int(input("Sci-fi: "))
comics = int(input('comics: '))
history = int(input('history: '))

total_price_no_discounts = sci_fi_books * 58 + comics * 32 + history * 24
total_to_pay = 0
if sci_fi_books >= 3:
    total_to_pay += sci_fi_books * 58 * 0.9
if history > 2:
    # get amount of books you should get for free
    free_books = history // 3
    # total_to_pay = total_to_pay + (history - free_books) * 24
    total_to_pay += (history - free_books) * 24

total_to_pay += comics * 32

if total_price_no_discounts > 300:
    total_to_pay = total_to_pay - 20

print(f"Total before discount: {total_price_no_discounts}")
print(f"Total discount: {total_price_no_discounts-total_to_pay}")
print(f"Total to pay: {total_to_pay}")



