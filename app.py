import hashlib
import os 

while True:
    print("\n")
    print("=== 🛡️ ULTRA SECURE SYSTEM (with SALT) 🛡️ ===")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        print("--- REGISTER ---")
        u_name = input("Username: ")
        p_word = input("Password: ")
        
        salt = os.urandom(4).hex()
        
        salted_password = p_word + salt
        
        h_pw = hashlib.sha256(salted_password.encode()).hexdigest()
        
        f = open("logs.txt", "a")
        f.write(u_name + "," + salt + "," + h_pw + "\n")
        f.close()
        print("✅ Account Created with Salt protection!")

    
    elif choice == "2":
        print("--- LOGIN ---")
        check_user = input("Username: ")
        check_pass = input("Password: ")
        
        f = open("logs.txt", "r")
        found = False
        
        for line in f:
             data = line.strip().split(",")
            
            stored_user = data[0]
            
            if stored_user == check_user:
                found = True
                stored_salt = data[1] 
                stored_hash = data[2] 
                
                
                check_mix = check_pass + stored_salt
                
            
                check_new_hash = hashlib.sha256(check_mix.encode()).hexdigest()
                
                if check_new_hash == stored_hash:
                    print("✅ ACCESS GRANTED! You are the Boss.")
                else:
                    print("❌ WRONG PASSWORD!")
                break
        
        f.close()
        if not found:
            print("❌ USER NOT FOUND!")

    elif choice == "3":
        print("Bye!")
        break
    else:

        print("Invalid choice")

