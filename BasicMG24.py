#BasicMG24
print("BasicMG24 by MG24 studios. Version: 1.0. Type '/guide' for help ")
dev = False
password = '1234'

while True:
    inputhing = input("Insert command here: ")

    if inputhing == "/access":
        input_password = input("Enter the password: ")
        if input_password == password:
            print("Access granted")
            dev = True
            print("Welcome back, user!")
        else:
            print("Access denied")
            

    elif inputhing == "/info":
        print("Version 1.0. Made by MG24 studios. Discover more on: https://sites.google.com/view/miaogamer24/home-page")

    elif inputhing == "/help":
        print("Here are some commands: /access /info /sum /sub /mol /div /raqua /givelink /guide /feedback /rick /rickshow /passchange /whodev")

    elif inputhing == "/sum":
        a = input("Number 1:" )
        b = input("Number 2:")
        print(float(a) + float(b))

    elif inputhing == "/sub":
        a = input("Number 1:" )
        b = input("Number 2:" )
        print(float(a) - float(b))

    elif inputhing == "/mol":
        a = input("Number 1:" )
        b = input("Number 2:" )
        print(float(a) * float(b))

    elif inputhing == "/div":
        a = input("Number 1:" )
        b = input("Number 2:" )
        print(float(a) / float(b))

    elif inputhing == "/raqua":
        a = input("Number: ")
        print(float(a) ** 0.5)

    elif inputhing == "/givelink":
        print("https://sites.google.com/view/miaogamer24/home-page")

    elif inputhing == "/feedback":
        print("https://forms.gle/15ihMj26TGCug6Sd8")

    elif inputhing == "/rick":
        Link_input = input("Insert here your link:" )
        if Link_input in [
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "https://www.youtube.com/watch?v=LLFhKaqnWwk",
            "https://www.youtube.com/watch?v=hvL1339luv0"
        ]:
            print("Yes, your link is a rickroll")
        else:
            print("Nah, your link isn't a rickroll (theorically)")

    elif inputhing == "/rickshow":
        print("Here are some rickroll links")
        print("https://www.youtube.com/watch?v=dQw4w9WgXcQ  This is the original ")
        print("https://www.youtube.com/watch?v=LLFhKaqnWwk An animated version")
        print("https://www.youtube.com/watch?v=hvL1339luv0 Cat version")

    elif inputhing == "/passchange":
        if dev:
            password = input("New password:" )
        else:
            print("Only administrators can do this")


    elif inputhing == "/whodev":
        print("MG24 studios is a developing studios created by MIAOGAMER24. It's still growing and it's only member it's me.")

    elif inputhing == "/guide":
        print("Here is a list of commands and their explanation:")
        print("/access - if u are dev")
        print("/info - Version and other")
        print("/help - List of commands without explanation")
        print("/sum - Sum some numbers")
        print("/sub - Subtract some numbers")
        print("/mol - Moltiplicate some numbers")
        print("/div - Divide some numbers")
        print("/raqua - Square root (From: radice quadrata in italian)")
        print("/givelink - Gives the official link for MG24 studios website")
        print("/feedback - Gives link to a google moduli to report and give me feedback")
        print("/rick - Checks if your link is a rickroll link")
        print("/rickshow - Shows a list of rickroll vids links")
        print("/passchange - Changes admin password ")
        print("/whodev - Tells u more info about me ")


    elif inputhing == "/exit":
        print("Closing BasicMG24...")
        break

    else:
        print("Unknown command. Type /help or /guide")

