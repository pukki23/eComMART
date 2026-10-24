# Task 1: eCOMMart — Product Variables
# eCOMMart Product Catalog Entry

# product_name = "Wireless Mouse"
# brand = "TechPro"
# price = 499.00
# is_in_stock = True
# category, seller_city = 'Electronics', 'Lagos'

# print(f"""Product : {product_name}
# Brand : {brand}
# Price : ${price:.2f}
# Available : {is_in_stock}
# Category : {category}
# Seller City : {seller_city}""")

# Task 2: eCOMMart — Price Calculations
# print(type(product_name))
# print(type(price))
# print(type(is_in_stock))

# print(len(product_name))

# price_1 = 499 #(Wireless Mouse)
# price_2 = 350 #(USB Hub)

# total = price_1 + price_2
# difference = price_1 - price_2
# avg_price = total / 2
# bulk_cost = price_1 * 10 #units
# remainder = total % 100
# tax = price_1 * 0.18 #(18% GST)
# per_unit = total // 2

# print(f"""Total : {total}
# Difference : {difference}
# Average Price : {avg_price}
# Bulk Cost : {bulk_cost}
# Remainder : {remainder}
# Tax : {tax}
# Per Unit : {per_unit}""")

# product_price = float(input("Enter the product price? "))
# price_after_discount = product_price - (product_price * 0.20)
# print(price_after_discount)

# product_name = input("Enter the product name: ")
# category = input("Enter the product category: ")
# seller_city = input("Enter the seller city: ")
# product_price = float(input("Enter the product price? "))

# print(f"""Product : {product_name}
# Category : {category}
# Seller City : {seller_city}
# Product Price : ${product_price:.2f}""")

# Task 1: eCOMMart Product Label
# product_sku = '1234456789'
# brand_tagline = "brand's tagline"
# product_description = """ this is the product
#                           full description in a triple quote multi
#                           line sentence"""

# print(f"""Produck SKU : {product_sku}
# Brand Tagline : {brand_tagline}
# Product Description : {product_description}""")

price_1 = 490.55
price_2 = 50.20
price_3 = 7.22
price_4 = 1000.75
price_5 = 68.94

# total_price = 0
# prices = [price_1, price_2, price_3, price_4, price_5]

# for price in prices:
#   total_price += price

subtotal = price_1 + price_2 + price_3 + price_4 + price_5
# subtotal = subtotal + (0.18 * subtotal)

# if subtotal > 500:
#   subtotal = subtotal - 50

# print(f"Total Price is {subtotal:.2f}")

# gst      = subtotal * 0.18
# discount = 50.00 if subtotal > 500 else 0.00
# total    = subtotal + gst - discount

# print(f"Subtotal : ${subtotal:.2f}")
# print(f"GST (18%): ${gst:.2f}")
# print(f"Discount : ${discount:.2f}")
# print(f"Total    : ${total:.2f}")

# Task 3: Order Confirmation with f-String and Triple Quotes
customer_name = "Jane Smith"
order_id = 12345678
item_list = ['item1', 'item2', 'item3']

for item in item_list:
  print(item)

print(f"""{'='*40}
Order Confirmation
{'='*40}
Customer Name : {customer_name}
Order ID : {order_id}
Item List : {', '.join(item_list)}""")