#BasicMG24
print("BasicMG24 by MG24 studios. Version: 1.1. Type '/guide' or '/help' for help ")

#some imports
import shutil
from pathlib import Path
import random
import sys
import os
import panda3d
from datetime import datetime
import time


PACKAGES = {
    "/install1": [
        "BasicMG24_cover.png"
    ],
    "/install2": [
        "play1_obstacle_1.png",
        "play1_obstacle_2.png",
        "play1_obstacle_3.png",
        "play1_player.png"
    ]
}


dev = False
password = ''
secret_wip = False
wip = False



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
        print("Version 1.1. Made by MG24 studios. Discover more on: https://sites.google.com/view/miaogamer24/home-page")

    elif inputhing == "/help":
        print("Here are some commands: /access /info /sum /sub /mol /div /raqua /esp /givelink /guide /feedback /rick /rickshow /passchange /whodev /diceroll /cdiceroll /devlogthis /devlogall /play1 /install1 /install2 /r100 /rnum /rpers /time /date / /wip")

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
    
    elif inputhing == "/esp":
        a = input("Number 1:" )
        b = input("Number 2:" )
        print(float(a) ** float(b))

    
    elif inputhing == "/givelink":
        print("https://sites.google.com/view/miaogamer24/home-page")

    elif inputhing == "/feedback":
        print("https://forms.gle/15ihMj26TGCug6Sd8")

    elif inputhing == "/rick":
        Link_input = input("Insert here your link:" )
        if Link_input in [
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "https://www.youtube.com/watch?v=LLFhKaqnWwk",
            "https://www.youtube.com/watch?v=hvL1339luv0",
            "https://music.youtube.com/watch?v=dQw4w9WgXcQ"
        ]:
            print("Yes, your link is a rickroll")
        else:
            print("Nah, your link isn't a rickroll (theorically)")

    elif inputhing == "/rickshow":
        print("""Here are some rickroll links
        https://www.youtube.com/watch?v=dQw4w9WgXcQ  This is the original 
        https://www.youtube.com/watch?v=LLFhKaqnWwk An animated version
        https://www.youtube.com/watch?v=hvL1339luv0 Cat version
        https://music.youtube.com/watch?v=dQw4w9WgXcQ Yt music
        """)

    elif inputhing == "/passchange":
        if dev:
            password = input("New password:" )
        else:
            print("Only administrators can do this")


    elif inputhing == "/whodev":
        print("MG24 studios is a developing studios created by MIAOGAMER24. It's still growing and it's only member it's me.")

    elif inputhing == "/diceroll":
        roll = random.randint(1, 6)
        print("Result:",  roll)

    elif inputhing == "/cdiceroll":

        def diceroll():
            Element_a = input("Insert element a: ")
            Element_b = input("Insert element b: ")
            roll = random.randint(1, 2)
            if roll == 1:
                return Element_a
            else:
                return Element_b

        print("Result:", diceroll())

    elif inputhing == "/devlogthis":
        print("""
        Devlog BasicMG24:
        1.1: (29/10/26)
        1.0: Release (7/10/26)
        More on: https://mg24studios.fandom.com/wiki/BasicMG24
        """)

    elif inputhing == "/devlogall":
        product = input("Insert exact product name (to show products list insert /showlist):" )
        if product == "/showlist":
            product_list = ["BasicMG24", "Parkourer"]
            print(product_list)
        elif product == "BasicMG24":
            print("""
            Devlog BasicMG24:
            1.1: (29/10/26)
            1.0: Release (7/10/26)
            More on: https://mg24studios.fandom.com/wiki/BasicMG24
            """)
        elif product == "Parkourer":
            print("""
            Devlog parkourer:
            Parkourer was never released, and it won't be.
            More on: https://mg24studios.fandom.com/wiki/Parkourer
            """)
        else:
            print("Product name is wrong, or the product isn't avaiable anymore.")

    elif inputhing == "/play1":
        import pygame
        pygame.init()

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        def find_file(filename):
            for root, dirs, files in os.walk(BASE_DIR):
                if filename in files:
                    return os.path.join(root, filename)
            raise FileNotFoundError(f"File not found: {filename}")

        player_image = pygame.image.load(find_file("play1_player.png"))
        player_image = pygame.transform.scale(player_image, (20, 40))

        obstacle_images = [
            pygame.transform.scale(
                pygame.image.load(find_file(f"play1_obstacle_{i}.png")),
                (30, 50)
            )
            for i in range(1, 4)
        ]

        # --- WINDOW ---
        WIDTH = 1400
        HEIGHT = 500
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Stick Runner")

        clock = pygame.time.Clock()

        # --- PLAYER ---
        player_x = 50
        player_y = HEIGHT - 60
        player_width = 20
        player_height = 40
        player_vel_y = 0
        gravity = 1
        is_crouching = False

        # --- OBSTACLES ---
        obstacles = []
        obstacle_speed = 6

        # --- SCORE ---
        score = 0
        font = pygame.font.SysFont(None, 36)

        def spawn_obstacle():
            obstacle = {
                "rect": pygame.Rect(
                    WIDTH,
                    HEIGHT - 50,
                    30,
                    50
                ),
                "image": random.choice(obstacle_images)
            }

            obstacles.append(obstacle)

        # --- GAME LOOP ---
        running = True

        while running:
            screen.fill((255, 255, 255))

            # --- INPUT ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()

            # Jump
            if (keys[pygame.K_w] or keys[pygame.K_SPACE] or keys[pygame.K_UP]) and player_y == HEIGHT - player_height:
                player_vel_y = -15

            # Crouch
            is_crouching = keys[pygame.K_s]

            # Move left/right
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
                player_x = max(0, player_x - 5)

            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
                player_x = min(WIDTH - player_width, player_x + 5)

            # --- GRAVITY ---
            player_y += player_vel_y
            player_vel_y += gravity

            if player_y >= HEIGHT - player_height:
                player_y = HEIGHT - player_height
                player_vel_y = 0

            # --- CROUCH ---
            draw_height = player_height // 2 if is_crouching else player_height

            player_rect = pygame.Rect(
                player_x,
                player_y,
                player_width,
                draw_height
            )

            # --- SPAWN OBSTACLES ---
            if random.random() < 0.02:
                spawn_obstacle()

            # --- MOVE OBSTACLES ---
            for obs in obstacles:
                obs["rect"].x -= obstacle_speed

            obstacles = [
                o for o in obstacles
                if o["rect"].x > -50
            ]

            # --- DRAW PLAYER ---
            screen.blit(
                player_image,
                (player_rect.x, player_rect.y)
            )

            # --- DRAW OBSTACLES ---
            for obs in obstacles:
                screen.blit(
                    obs["image"],
                    obs["rect"]
                )

            # Ground
            pygame.draw.line(
                screen,
                (0, 0, 0),
                (0, HEIGHT - 1),
                (WIDTH, HEIGHT - 1),
                2
            )

            # Score
            score += 1
            score_text = font.render(
                f"Score: {score}",
                True,
                (0, 0, 0)
            )

            screen.blit(score_text, (10, 10))

            # Collision
            for obs in obstacles:
                if player_rect.colliderect(obs["rect"]):
                    print("GAME OVER! Score:", score)
                    running = False
                                        
            pygame.display.update()
            clock.tick(60)
            

        print(inputhing)
        pygame.quit()



    elif inputhing in PACKAGES:
        try:

            program_folder = Path(__file__).parent
            downloads = Path.home() / "Downloads"

            for file_name in PACKAGES[inputhing]:

                source = program_folder / file_name
                destination = downloads / file_name

                shutil.copy2(source, destination)

                print(f"Installed: {file_name}")

            print("Installation completed!")

        except FileNotFoundError as e:
            print("Missing file:", e)

        except Exception as e:
            print("Installation error:", e)


    elif inputhing == "/r100":
        a = random.randint(1, 100)
        inu = 101
        while inu != a:
            inu = int(input("Insert number from 1 to 100:"  ))
            if inu != a:
                if inu < a:
                    print("Too small!")
                elif inu > a:
                    print("Too big!")
        print(f'You got it! the number was {a}')

    elif inputhing == "/rpers":
        a = int((input("Insert start number:" )))
        b = int((input("Insert maximum number:" )))
        secret_num = random.randint(a, b)
        guess = None
        while guess != secret_num:
            guess = int(input(f'Insert number from {a} to {b}:' ))
            if guess != secret_num:
                if guess < secret_num:
                    print("Too small!")
                elif guess > secret_num:
                    print("Too big!")
        print(f' You got it! The num was {secret_num}')


    elif inputhing == "/spam":
        while True:
            print("spamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspamspam")

    elif inputhing == "/i_feel_lucky":
        print("Ok good for ya")
    
    elif inputhing == "/rnum":
                a = (random.randint(0, 10000000000))
                print(f'The random number is {a}')


    elif inputhing == "/time":
        from datetime import datetime

        now = datetime.now()
        print(f"Time: {now.hour}:{now.minute}:{now.second}")

    elif inputhing == "/date":
        from datetime import datetime

        now = datetime.now()
        print("Date:", now.strftime("%d/%m/%Y"))

    elif inputhing == "/":
        print("That isn't a command")
        time.sleep(120)
        print("You still here huh")
        time.sleep(30)
        print("You afk?")
        time.sleep(300)
        print("You sleeping???")
        time.sleep(120)
        print("Vro close the program")
        time.sleep(3)
        print("Bye GET OUT")
        break

    elif inputhing == "/wip":
        wip = True
        print("""
        The commands that are shown here are a work in progress and some won't even be added
        
        
        """)


    
    elif inputhing == "/guide":

        print("""
        Here is a list of commands and their explanation:
        /access - if you are dev
        /info - Version and other
        /help - List of commands without explanation
        /sum - Sum some numbers
        /sub - Subtract some numbers
        /mol - Moltiplicate some numbers
        /div - Divide some numbers
        /raqua - Square root (From: radice quadrata in italian)
        /esp - Esponentation of two numbers       
        /givelink - Gives the official link for MG24 studios website
        /feedback - Gives link to a google moduli to report and give me feedback
        /rick - Checks if your link is a rickroll link
        /rickshow - Shows a list of rickroll vids links
        /passchange - Changes admin password
        /whodev - Tells u more info about me
        /diceroll - Random number from 1 to 6
        /cdiceroll - Custom dice roll
        /devlogthis - BasicMG24 devlog
        /devlogall - All devlogs of all MG24 studios things
        /play1 - play a mini stickrunner
        /install1 - Install the programs cover image
        /install2 - Install the play1 textures
        /r100 - guess with one chance the number (0-100)
        /rpers - personalized /r100 command
        /rnum - random number (0-10000000000)
        /time - tells you what time is it
        /date - tells you what's the date today
        / - you sleeping on your keyboard?
        /wip - Unlocks wip commands
        """)


    elif inputhing == "/666" and secret_wip == True:
        import pygame

        pygame.init()
        pygame.display.set_caption("666")
        screen = pygame.display.set_mode((800, 600))
        screen.fill((255, 0, 0))

        bottone = pygame.Rect(50, 50, 100, 40)

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bottone.collidepoint(event.pos):
                        pygame.quit()
                        exit()

            pygame.draw.rect(screen, (144, 0, 0), bottone)

            pygame.display.flip()

        


    elif inputhing == "/secret_guide":
        print("""
        /wip2 - Unlock wip secret commands
        /secret_info - Shows secret commands without their explanation
        /666 - ???
        """)

    elif inputhing == "/secret_info":
        print("/wip2 /secret_guide")

    elif inputhing == "/wip2":
        secret_wip = True

    elif inputhing == "/exit":
        print("Closing BasicMG24 1.1...")
        time.sleep(2)
        break

    else:
        print("Unknown command. Type /help or /guide")
