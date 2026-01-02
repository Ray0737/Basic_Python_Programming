#-----------------------------------------------------Final Exam Mock Up-----------------------------------------------------#

#--------------------------------------ATM System--------------------------------------# 

account = {"Ray": ["test1", "0"]}

def login():
    global current_user
    
    username = input("Enter username: ")
    current_user = username
    password = input("Enter password: ")

    if username in account:
        if account[username][0] == password:
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in account:
        print("Username already exists.")
    else:
        account[username] = [password, 0]
        print("Registration successful!")

def withdraw():
    money = account[current_user][1]
    print(f"Current Balance: {money} THB\n")

    print("Bank only have 1000THB, 500THB, and 100THB banknotes")
    withdraw = int(input("Enter the amount of withdraw: "))
    if withdraw % 100 == 0:
        bank1000 = withdraw // 1000
        withdraw = withdraw % 1000
        bank500 = withdraw //500
        withdraw = withdraw % 500
        bank100 = withdraw //100
        print(f"n bank1000 = {bank1000}\nn bank500 = {bank500}\nn bank100 = {bank100}")
    else:
        print("withdraw unable")
        
    new_money = money - withdraw
    account[current_user][1] = new_money
    if input("Return to home (y/n): ") == "y":
        main()
        
def deposit():
    money = account[current_user][1]
    print(f"Current Balance: {money} THB\n")

    deposit = int(input("Enter the amount of deposit: "))
    new_money = money + deposit
    account[current_user][1] = new_money
    print(f"New Balance: {new_money} THB")
    if input("Return to home (y/n): ") == "y":
        main()
    
def main():
    while True:
        money = account[current_user][1]
        print(f"Current Balance: {money} THB\n")
        print("Choose menu (1-Withdraw | 2-Deposit | 3-Exit): ")
        if input("Enter choice (1-3): ") == "1":
            withdraw()
        elif input("Enter choice (1-3): ") == "2":
            deposit()
        elif input("Enter choice (1-3): ") == "3":
            break
        
#--------------------------------------Terminal Triangle--------------------------------------# 

h = int(input("Enter the height of the triangle: "))
for i in range(1, h + 1):
    extspace = h - i
    if i == 1:
        print(" " * extspace + "*")
    elif i == h:
        base_len = 2 * h - 1
        print("*" * base_len)
    else:
        intspace = 2 * i - 3
        print(" " * extspace + "*" + "*" * intspace + "*")