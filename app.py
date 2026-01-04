import hashlib
import os  # புது ஆளு! (Salt உருவாக்க)

while True:
    print("\n")
    print("=== 🛡️ ULTRA SECURE SYSTEM (with SALT) 🛡️ ===")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Enter choice: ")

    # --- SIGNUP ---
    if choice == "1":
        print("--- REGISTER ---")
        u_name = input("Username: ")
        p_word = input("Password: ")
        
        # STEP 1: புதுசா ஒரு Salt உருவாக்குதல் (4 Bytes = 8 letters)
        # os.urandom: கம்ப்யூட்டர் தானாக உருவாக்கும் ரேண்டம் நம்பர்
        salt = os.urandom(4).hex()
        
        # STEP 2: பாஸ்வேர்ட் கூட உப்பை கலக்குதல் (Mixing)
        # "password" + "salt" = "passwordsalt"
        salted_password = p_word + salt
        
        # STEP 3: கலந்து வச்சதை Hash பண்ணுதல்
        h_pw = hashlib.sha256(salted_password.encode()).hexdigest()
        
        # STEP 4: சேவ் பண்ணும்போது Salt-ஐயும் சேர்த்து வைக்கணும்!
        # Format: username,salt,hash
        f = open("logs.txt", "a")
        f.write(u_name + "," + salt + "," + h_pw + "\n")
        f.close()
        print("✅ Account Created with Salt protection!")

    # --- LOGIN ---
    elif choice == "2":
        print("--- LOGIN ---")
        check_user = input("Username: ")
        check_pass = input("Password: ")
        
        f = open("logs.txt", "r")
        found = False
        
        for line in f:
            # இப்போ data-ல 3 துண்டு இருக்கும்!
            # data[0] = Username
            # data[1] = Salt (அந்த யூசருக்கான தனி உப்பு)
            # data[2] = Hash
            data = line.strip().split(",")
            
            stored_user = data[0]
            
            if stored_user == check_user:
                found = True
                stored_salt = data[1] # டேட்டாபேஸ்ல இருந்து உப்பை எடு
                stored_hash = data[2] # டேட்டாபேஸ்ல இருந்து ஹாஷை எடு
                
                # STEP 5: அதே ஃபார்முலா! (Input Password + Stored Salt)
                check_mix = check_pass + stored_salt
                
                # அதை Hash பண்ணி பார்ப்போம்
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