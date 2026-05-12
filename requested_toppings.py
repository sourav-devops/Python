current_users = ["soshrest", "alkiran", "sgalla", "ragundu", "admin"]
new_users = ["ram", "shyam", "arjun", "nakul", "sgalla", "soshresT"]
        
for user in new_users :
    if user.lower() in current_users:
        print(f"hello {user} user  already registerd, please use another username")
    else:
        print(f"Hello {user} ,thank you for registering")    
