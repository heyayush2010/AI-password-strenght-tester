x = ["123456 = weak", "password = weak", "123456789 = weak", "12345678 = weak","password123 = weak", "1234567 = weak", "1234567890 = weak", "123123 = weak", "12345 = weak", "123456789 = weak", "1234 = weak", "123456 = weak", "123456789 = weak", "querty = weak", "abc123 = weak", "111111 = weak", "12345678 = weak", "password1 = weak", "123 = weak", "123456789 = weak", "123", "starwars = weak", "starwars123 = weak", "querty123 = weak", "something = weak", "something123 = weak", "something1234 = weak", "something12345 = weak", "hello = weak","hello1234 = weak", "hello12345 = weak", "hello123456 = weak", "hello1234567 = weak", "hello12345678 = weak", "random password = weak", "randompassword = weak", "randompassword123 = weak", "randompassword1234 = weak", "randompassword12345 = weak",]
y = [
    "J#7vK9!eLpX2",
    "z@R5bF%3qJ8s",
    "M7t!oE&9VbQ1",
    "W^gP4kz9$L0c",
    "Q!zK2yX@3pR5m",
    "Vj7A$YzP9+L3n",
    "H#bG0j9&Z6eX",
    "R7aT$hK8bL1D2",
    "F#3cJ!oXwV8p",
    "B2j@7pX5*LQ6v"
]
x_train = x 
y_train = y 
input_password = input("Enter password: ")
if input_password in [pw.split(' = ')[0] for pw in x]:  
    print("Weak password")
else: 
    print("Strong password") 
    
