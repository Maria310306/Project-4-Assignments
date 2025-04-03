import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

stored_logins = {
    "user@example.com": hash_password("mypassword123"),
    "admin@example.com": hash_password("adminpass456")
}

def login(email, password_to_check):
    if email in stored_logins:
        stored_hash = stored_logins[email]
        entered_hash = hash_password(password_to_check)
        return stored_hash == entered_hash
    else:
        return False

def main():
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    if login(email, password):
        print("Login successful!")
    else:
        print("Login failed!")

if __name__ == '__main__':
    main()
