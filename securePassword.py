secure = (('s', '$'), ('and', '&'), ('a', '@'), ('o', '0'), ('i', '!'))

def securePassword(password):
    for a,b in secure:
        password = password.replace(a,b)
        return password
    
if __name__ == "__main__":
    password = input("Enter password here:")
    password = securePassword(password)
    print("Your password is", password)