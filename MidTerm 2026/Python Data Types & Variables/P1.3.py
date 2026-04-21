#3. Program to take user input and display its data type
# Note: In Python, input() always takes data as string (str) by default

user_input = input("Enter Something: ")
try:
    val = int(user_input)
    print("Value Is Integer")
except:
    try:
        val = float(user_input)
        print("Value Is Float")
    except:
        if user_input.lower() in ["true", "false"]:
            print("Data Type: Boolean")
        else:
            print("Data Type: String")
    