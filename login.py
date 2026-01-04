import hashlib

print("--- SECURE LOGIN SYSTEM ---")


check_user = input("Username: ")
check_pass = input("Password: ")

check_hash = hashlib.sha256(check_pass.encode()).hexdigest()

f = open("logs.txt", "r")


found = False


for line in f:
 
    data = line.strip().split(",") 
    
    stored_name = data[0]
    stored_hash = data[1]

    if stored_name == check_user:
        found = True
        if stored_hash == check_hash:
            print("✅ LOGIN SUCCESS! Welcome back, Alpha.")
        else:
            print("❌ WRONG PASSWORD! Access Denied.")
        break 

f.close()

if not found:
    print("❌ USER NOT FOUND! Please Signup first.")