# Import the main modules of expyriment
from expyriment import design, control, stimuli

from expyriment.misc.constants import C_GREY
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices

def kanizsaRectngle(rectangeAspectRatio = 1, rectangleScalingFactor = 1, circleScalingFactor = 1):
    exp = design.Experiment(name = "Circle", background_colour=C_GREY)

    control.set_develop_mode()

    # Initialize the experiment: Must be done before presenting any stimulus
    control.initialize(exp)



    #control.set_develop_mode()

    width = exp.screen.size[0]
    length = exp.screen.size[1]

    radius = int(width * 0.05 * circleScalingFactor)

    squareWidth = int(width * 0.25 * rectangleScalingFactor)
    squareLength = squareWidth * rectangeAspectRatio

    circle1 = stimuli.Circle(radius = radius, colour = "black", position=(squareWidth//2,squareLength//2))
    circle2 = stimuli.Circle(radius = radius, colour = "black", position=(squareWidth//2 * -1,squareLength//2)) 
    circle3 = stimuli.Circle(radius = radius, colour = "white", position=(squareWidth//2,squareLength//2 * -1))
    circle4 = stimuli.Circle(radius = radius, colour = "white", position=(squareWidth//2 * -1,squareLength//2 * -1))

    square = stimuli.Rectangle(size = (squareWidth,squareLength), colour= C_GREY)

    circle1.present(clear = True, update = False)
    circle2.present(clear = False, update = False)
    circle3.present(clear = False, update = False)
    circle4.present(clear = False, update = False)
    square.present(clear = False, update = True)



    exp.keyboard.wait()

    """
    # Create a fixation cross (color, size, and position will take on default values)
    fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered

    # Create a 50px-radius circle
    circle = stimuli.Circle(radius=50)

    # Start running the experiment
    control.start(subject_id=1)

    # Present the fixation cross
    fixation.present(clear=True, update=True)

    # Leave it on-screen for 1,000 ms
    exp.clock.wait(1000)

    # Remove the cross and replace it with a circle
    circle.present(clear=True, update=True)

    # Leave it on-screen until a key is pressed
    exp.keyboard.wait()
    """

    # End the current session and quit expyriment
    control.end()

kanizsaRectngle(rectangleScalingFactor=0.5, rectangeAspectRatio= 0.5, circleScalingFactor= 0.5)