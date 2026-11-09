# print("Hi. welcome!")

# name = input("Enter your name:").strip().upper()
# last_name = input("Enter your last name:").strip().upper()
# age = int(input("Enter your age:"))
# phone_number = input("Enter your phone number:")

# if phone_number.startswith("09"):
#     print(f"---User Information---")
#     print(f"Name:{name}{last_name}")
#     print(f"Age:{age}")
#     print(f"Phone number must start with 09.")
# else:
#     print("Error")





# ---------------tamrin2---------------


# products = ["Laptop","Mouse","Keyboard","Monitor","Mouse"]

# print(len(products))
# print("Laptop" in products)
# print(products.count("Mouse"))
# print(products.index("Keyboard"))
# print(tuple(products))
# print(set(products))


# ......***...........tamrin3.........***.........


# student = {
#     "name": "  tara rezaie majzoob  ", 
#     "age": "18",
#     "score": "19",
#     "city": "hamedan"
# }


# student["name"] = student["name"].strip()
# student["age"] = int(student["age"])
# student["score"] = float(student["score"])


# student["name"] = student["name"].upper()
# student["city"] = student["city"].upper()


# print(type(student["name"]))
# print(type(student["age"]))
# print(type(student["score"]))


# is_passed = student["score"] >= 15

# print(f"NAME: {student['name']}")
# print(f"AGE: {student['age']}")
# print(f"SCORE: {student['score']}")
# print(f"CITY: {student['city']}")
# print(f"PASSED: {is_passed}")



# ....................tamrin4....................


# text = " Python is a good code "


# clean_text = text.strip().lower()
# print(f"متن پاکسازی: {clean_text}")


# words = clean_text.split()
# print(f"تعداد کلمات: {len(words)}")

# print(f"شروع با python: {clean_text.startswith('python')}")
# print(f"پایان با programming: {clean_text.endswith('programming')}")

# replaced_text = clean_text.replace("code", "Python")
# print(f"جایگزینی: {replaced_text}")



# ......***...........tamrin5.........***.........


# customers = {
#     "1001": "Tara Rezaie",
#     "1002": "Taraneh Rezaie",
#     "1003": "Arman Rezaie",
#     "1004": "Arsan Rezaie"
# }

# print(f"1. Total customers: {len(customers)}")

# search_id = input("2. Enter customer ID (e.g., 1002): ")

# if search_id in customers:
#     customer_name = customers[search_id]
#     print(f"4. Customer Name: {customer_name}")
#     print(f"5. Name in Uppercase: {customer_name.upper()}")
# else:
#     print("Customer not found!")

# unique_names = set(customers.values())
# print(f"6. Unique names: {unique_names}")

# ids_list = list(customers.keys())
# print(f"7. List of IDs: {ids_list}")






