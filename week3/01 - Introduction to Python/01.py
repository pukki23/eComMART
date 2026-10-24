# print ("Hello World!")
# print (9 * "\n")
# print(print ("Hello World!"))

# print("Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec")

# print ("I want \\n to be printed.")
# print("I'm very *happy*")

# print ("Hello\tWorld!")

# print ("""
# Routine:
# \t- Eat
# \t- Study
# \t- Sleep\n\t- Repeat
# """)

# print ("Welcome to", end = ' ')
# print ("Python", end = '!')

# print ("Welcome to", end = ' ')
# print ("Python", end = '!')

# print("Python" , end = '@')

# print("Python " , end = '@')

# print ('_M'*9)

# print("Hello " * 6)

# #TASK 1
# store = "eCoMMart"
# category = "Electronics"

# print("Welcome to " + store + "'s " + category + " section!")

# #TASK 2
# product_name = "Wireless Mouse"
# price = 499.00
# discount = 10
# to_pay = price + (discount / 100)
# seller = "Crafts"
# seller_city = "Abuja"

# print(f"""Product : {product_name}
# Price : ${price:.2f}
# Discount : {discount}%
# You pay : ${to_pay:.2f}
# Sold by : {seller} - {seller_city}
# """)

#Task: Organizing library database
# available = True

# book_1 = {'title': 'Python Basics', 'written_by': 'John Doe', 'status': available}
# book_2 = {'title': 'Python Basics', 'written_by': 'John Doe', 'status': not available}

# for desc, val in book_1.items():
#   print(f'{desc} : {val}')

available = True
issued = not available
returned = not issued

book_1_title = 'Python Basics'
book_1_written_by = 'John Doe'
book_1_is_available = available

book_2_title = 'Data Science 101'
book_2_written_by = 'Jane Smith'
book_2_is_available = returned

print(f"""Book Title : {book_1_title}
Book Author : {book_1_written_by}
Book is Available : {book_1_is_available}\n""")

print(f"""Book Title : {book_2_title}
Book Author : {book_2_written_by}
Book is Available : {book_2_is_available}""")