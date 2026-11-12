def check_access(**kwargs):

    for key,value in kwargs.items():
        print(f"{key}: {value}")
    
    is_admin = kwargs.get("admin", False)
    
    if is_admin == True:
        print("OK")
    else:
        print("IS NOT OK")

check_access(name="Tara", email="qtara@gmail.com", admin=True)
print("----------------")
check_access(name="Taraneh", email="qtaraneh@gmail.com", admin=False)
print("----------------")
check_access(name="Arman", email="qarman@gmail.com")