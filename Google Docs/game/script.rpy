# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define eileen = Character("Eileen")
image bg room = "bg room.jpg"
image lois happy = "peter and lois"
image lois angry = "angry lois.png"
image lois neutral = "neutral lois.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room:

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lois neutral at left with moveinleft:
        xzoom 0.2 yzoom 0.2




    # These display lines of dialogue.

    eileen "How was your day?"
    menu:
        "Great!":
            show lois happy with dissolve:
                xzoom 0.9 yzoom 0.9
            eileen "So was mine!"
        "Terrible ...":
            show lois angry:
                xzoom 2 yzoom 2
            eileen "Same..."

    # This ends the game.

    return
