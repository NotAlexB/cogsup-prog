# Import the main modules of expyriment
from expyriment import design, control, stimuli
def launching_function(timeGap = 0, spaceGap = 0, SpeedDifference = 1):
    
    # Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
    exp = design.Experiment(name = "Circle")

    # Initialize the experiment: Must be done before presenting any stimulus
    control.initialize(exp)

    # Create a fixation cross (color, size, and position will take on default values)
    #fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered

    # hary is on the left
    harry = stimuli.Rectangle((50,50), colour = "red", position = (-400,0))

    # roughly 50 pixels makes it still look like harry is causing josh to move

    # josh is on the right
    josh = stimuli.Rectangle((50,50), colour = "green", position=(0 + spaceGap,0))

    # Start running the experiment
    control.start(subject_id=1)

    # Present the fixation cross


    # Leave it on-screen for 1,000 ms

    # Remove the cross and replace it with a circle

    # josh presents
    josh.present(clear=True, update=False)

    # harry presents
    harry.present(clear=False, update=True)

    # they both wait a sec
    exp.clock.wait(1000)

    # I like to move it move it, harry bumps into josh
    for i in range(175):
        harry.move((2,0))
        harry.present(clear = True, update=False)
        josh.present(clear = False, update = True)

    # delayed reaction time

    exp.clock.wait(timeGap)

    # around 50 ms there is not perception of stopped motion

    # Josh is hit, poor josh
    for i in range(175 // SpeedDifference):
        josh.move((2 * SpeedDifference,0))
        harry.present(clear = True, update=False)
        josh.present(clear = False, update = True)
        
    # it doesn't look like Harry caused the movement at this speed

    #circle.present(clear=True, update=True)

    # Leave it on-screen until a key is pressed
    exp.keyboard.wait()

    # End the current session and quit expyriment
    control.end()