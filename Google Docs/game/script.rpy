# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image doc office = "doc room.jpg"
image patient = "neutral lois.png"
image patient angry = "angry lois.png"
image doctor = "doc.png"
define doctor = Character("Dr. [docname]")
define patient = Character("Lois Griffin")

# The game starts here.


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene doc office:

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show doctor at left with moveinleft:

    screen failure(failMsg):
        window id "window":
            vbox:
                spacing 10
                text failMsg id "You failed."

    # These display lines of dialogue.
    python:
        docname = renpy.input("What would you like to be called?(first or last)", length=30)
        docname = docname.strip()

        if not docname:
            docname = "Anna Garcia"

    show patient at right with moveinright:
        xzoom 0.3 yzoom 0.3

    doctor "Hello, my name is Dr. [docname]."
    patient "Hello, my name is Lois Griffin."
    doctor "What brings you here today?"

    patient "My stomach hurts like a <REDACTED>."
    "What should you ask next?"
    menu:
        "How long have you been feeling this pain?":
            show doctor with dissolve:
            doctor "So was mine!"
        "How bad is it on a scale of 1 to 10?":
            show doctor:
            patient "10 being the worst or the best?"
            menu:
                "Worst":
                    patient "It's an 8."
                "Best":
                    patient "It's a 2."
        "Ma'am, are you pregnant?":
            show patient angry:
            patient "Excuse me?!"

    show failure(failMsg)




    # This ends the game.

    return
