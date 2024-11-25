email = input("Enter your e-mail: ")
k, d, j = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@') == 1):
            if (email[-4] == '.') ^ (email[-3] == '.'):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isupper():
                        d = 1
                    elif i.isdigit():
                        continue
                    elif i in ['@', '.', '_']:
                        continue
                    else:
                        j = 1
                if k == 1 or j == 1 or d == 1:
                    print("Make sure there is no space or uppercase letters are used.")
                else:
                    print("Correct email.")
            else:
                print("'.' is missing at the correct position.")
        else:
            print("Missing '@' or it is used more than once.")
    else:
        print("E-mail must start with a character.")
else:
    print("Invalid email. Too short.")
