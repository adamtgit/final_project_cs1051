﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image doc office = "doc room 2.png"
image operating_table = "operating room.png"
image 1hr = "one hour later.jpg"
image patient = "neutral lois.png"
image patient angry = "angry lois.png"
image doctor = "doc.png"
define doctor = Character("Dr. [docname]")
define patient = Character("Lois Griffin")
image patient_family = "peter and lois.png"
image body = "human body.png"
image red = "red.jpg"
image blue = "blue.jpg"
image white = "white.jpg"

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
    menu:
        "How long have you been feeling this pain?":
            show doctor with dissolve:
            doctor "Since two days ago!"
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
            jump fail_screen
    menu:
        "Do you mind if I take a look?":
            patient "Sure."
        "I'll write you a note for some painkillers and you'll be right on your way.":
            jump fail_screen
        "Take off your shirt.":
            patient "How rude! I will take off my shirt in time, thank you very much!"

label physical_exam:
    scene blue
    show body:
        xzoom 0.5 yzoom 0.5
    "What do you do first?"
    menu:
        "Inspect":
            "You find nothing out of the ordinary."
        "Palpate":
            jump warning_screen
        "Percuss":
            jump warning_screen
        "Auscultate":
            jump warning_screen
    "What do you do next?"
    menu:
        "Palpate":
            jump warning_screen
        "Percuss":
            jump warning_screen
        "Auscultate":
            "All findings are normal."
    "What do you do next?"
    menu:
        "Palpate":
            jump warning_screen
        "Percuss":
            "The lower right of the abdomen is tender to the touch."
    "You then palpate the patient and find that the patient experiences pain once you quickly take your hands off of her abdomen."

label diagnostic_tests:
    scene doc office
    show doctor at left with moveinleft
    doctor "Now it's time to run some tests. We'll start with a:"
    menu:
        "Complete blood count":
            "Results indicated an elevated white blood cell count."
            jump diagnostic_tests1
        "Stress Test":
            jump warning_screen2
        "CT Scan":
            jump warning_screen2
        "Endoscopy":
            jump warning_screen2
        "Colonoscopy":
            jump warning_screen2


label diagnostic_tests1:
    scene doc office
    show doctor at left with moveinleft
    doctor "What test should we run next?"
    menu:
        "Stress Test":
            jump warning_screen2
        "CT Scan":
            "Results indicated a circle of inflamed tissue about 6 mm in diameter located in the bottom right of the patient's abdomen."
        "Endoscopy":
            jump warning_screen2
        "Colonoscopy":
            jump warning_screen2

label guess:
    scene doc office
    "Now it's time to diagnose the patient. What do you think the patient has?"
    menu:
        "Ovarian Cyst":
            "Nice try but patients with ovarian cysts do not usually show rebound pain (from the physical exam) and don't have elevated white blood cell counts either."
            jump guess
        "Irritable Bowel Syndrome":
            "Nice try but irritable bowel syndrome patients exhibit flatulence, bloating, and chronic, long-lasting abdominal pain."
            jump guess
        "Appendicitis":
            "Correct!"
            jump treatment
        "Stomach Ulcer":
            "Nice try. Patients with ulcers are indeed suffering from a bacterial infection, but the pain is not near the stomach."
            jump guess


label treatment:
    scene doc office
    "What should be the most appropriate course of treatment?"
    menu:
        "Give an ice pack":
            jump fail_screen
        "Surgery to remove the appendix":
            scene operating_table
            scene 1hr
            scene doc office
            show patient:
                xzoom 0.3 yzoom 0.3
            patient "Thank you, Dr. [docname]!"

            return
        "Prescribe antibiotics":
            jump fail_screen

label warning_screen:
    scene red
    pause 1.0

    show text "WARNING: Please try again."
    pause 2.0

    hide text with dissolve
    pause 1.0

    jump physical_exam

label warning_screen2:
    scene red
    pause 1.0

    show text "WARNING: Please try again."
    pause 2.0

    hide text with dissolve
    pause 1.0

    jump diagnostic_tests

label fail_screen:
    scene black
    pause 1.0

    show text "You failed." with dissolve
    pause 2.0

    hide text with dissolve
    pause 1.0

    return







    # This ends the game.
