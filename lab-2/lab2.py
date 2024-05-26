import re

text = input("describe your purchases: ")
# text = "I bought three Samsung smartphones 150 $ each, four kilos of fresh banana for 1,2 dollar a kilogram and one Hamburger with 4,5 dollar."

product_pattern = r'(\b(?:one|two|three|four|five|six|seven|eight|nine|ten|\d+)\s(?:[a-zA-Z_-]+\s?)+)\s(?:(\d+(?:,|.\d+)?)\s(?:\$|dollar|dollars)s?(?: each| kilogram|s)?)?'

word_to_number = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10 }

stop_words = {'fresh', 'with', 'for', 'only', 'dollars', 'new', 'dollar', 'cheap', 'each', 'of', 'kilo', 'kilos'}

products = re.findall(product_pattern, text)

product_list = []
for match in products:
    quantity_text = re.findall(r'\b(?:one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b', match[0])[0]
    quantity = word_to_number.get(quantity_text.lower(), quantity_text)
    product = ' '.join(word for word in match[0].split()[1:] if word.lower() not in stop_words)
    unit_price_str = match[1].replace(',', '.') if match[1] else "0.0"
    unit_price = float(unit_price_str)
    total_price = quantity * unit_price
    product_list.append((product, quantity, unit_price, total_price))

# print(product_list)

print("Generated Bill:")
print("{:<30} {:<10} {:<15} {:<10}".format("Product", "Quantity", "Unit Price", "Total Price"))
for product in product_list:
    print("{:<30} {:<10} {:<15} {:<10}".format(product[0], product[1], product[2], product[3]))
