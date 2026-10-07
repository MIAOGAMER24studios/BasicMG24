#BasicMG24
print("BasicMG24 by MG24 studios. Version: 1.0. Type '/guide' for help ")


dev = False
inputhing = input("Insert command here: ")
password = 'ilikekids'

if inputhing == "/access":
    input_password = input("Enter the password: ")
    if input_password == password:
        print("Access granted")
        dev = True
    else:
        print("Access denied")


    if input_password == password:
        print("Welcome back, user!")

if inputhing == "/info":
    print("Version 1.0. Made by MG24 studios. Discover more on: https://sites.google.com/view/miaogamer24/home-page")

if inputhing == "/help":
    print("Here are some commands: /access /info /sum /sub /mol /div /raquad /givelink /guide")

if inputhing == "/sum":
    a = input("Number 1:" )
    b = input("Number 2:")
    print(float(a) + float(b))

if inputhing == "/sub":
    a = input("Number 1:" )
    b = input("Number 2:" )
    print(float(a) - float(b))

if inputhing == "/mol":
    a = input("Number 1:" )
    b = input("Number 2:" )
    print(float(a) * float(b))

if inputhing == "/div":
    a = input("Number 1:" )
    b = input("Number 2:" )
    print(float(a) / float(b))

if inputhing == "/raqua":
    a = input("Number: ")
    print(float(a) ** 0.5)

if inputhing == "/givelink":
    print("https://sites.google.com/view/miaogamer24/home-page")

if inputhing == "/feedback":
    print("https://forms.gle/15ihMj26TGCug6Sd8")


if inputhing == "/rick":
    Link_input = input("Insert here your link:" )
    if Link_input == "https://www.youtube.com/watch?v=dQw4w9WgXcQ" or Link_input == "https://www.youtube.com/watch?v=LLFhKaqnWwk" or Link_input == "https://www.youtube.com/watch?v=hvL1339luv0":
        print("Yes, your link is a rickroll")
    else:
        print("Nah, your link isn't a rickroll (theorically)")

if inputhing == "/rickshow":
    print("Here are some rickroll links")
    print("https://www.youtube.com/watch?v=dQw4w9WgXcQ  This is the original ")
    print("https://www.youtube.com/watch?v=LLFhKaqnWwk An animated version")
    print("https://www.youtube.com/watch?v=hvL1339luv0 Cat version")

if inputhing == "/guide":
    print("Here is a list of commands and their explanation:")
    print("/access" " if u are dev")
    print("/info" " Version and other")
    print("/help" " List of commands without explanation")
    print("/sum"  " Sum some numbers")
    print("/sub"  " Subtract some numbers")
    print("/mol"  " Moltiplicate some numbers")
    print("/div"  " Divide some numbers")
    print("/raqua" " Square root (From: radice quadrata in italian)")
    print("/givelink" " Gives the official link for MG24 studios website")
    print("/feedback" " Gives link to a google moduli to report and give me feedback")
    print("/rick" " Checks if your link is a rickroll link. Note: this might not be precise as there might not be all rickroll vids")
    print("/rickshow" " Shows a list of rickroll vids links")
    