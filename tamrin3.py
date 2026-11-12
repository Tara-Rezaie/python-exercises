import time

def calculate_time(func):
    
    def wrapper():
        start_time = time.time()  
        func()  
        end_time = time.time()  
        
        total_time = end_time - start_time
        print(f"Execution time: {total_time}")

    return wrapper

def test_function():
    time.sleep(2)  
    print("Task Finished")
