import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Execution time: {total_time:.2f} seconds")
        
        return result
    return wrapper

@calculate_time
def create_order(*args, **kwargs):
    customer_name = kwargs.get("name", "Unknown")
    address = kwargs.get("address", "Unknown")
    
    product_count = len(args)
    
    print(f"Customer: {customer_name}")
    print(f"Address: {address}")
    print(f"Total Products: {product_count} -> {args}")
    
    with open("orders.txt", "a") as file:
        file.write(f"Customer: {customer_name} | Address: {address}\n")
        file.write(f"Products: {args}\n")
        file.write("-" * 20 + "\n")
        
    print("Order saved successfully!")

create_order("Phone", "Headphones", "Smartwatch", name="Tara", address="Hamedan")
