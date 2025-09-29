# Import the main modules of expyriment
from expyriment import design, control, stimuli

from expyriment.misc.constants import C_GREY
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices

def hermannGrid(sizeSquares = 10, colorSquares = "black", spaceBetween = 2, backgroundColor = C_GREY, rows = 10, columns = 10):
    exp = design.Experiment(name = "Circle", background_colour=backgroundColor)

    control.set_develop_mode()

    # Initialize the experiment: Must be done before presenting any stimulus
    control.initialize(exp)



    #control.set_develop_mode()
    
    square = stimuli.Rectangle(size = (sizeSquares,sizeSquares), colour=colorSquares,position=((sizeSquares + spaceBetween) * columns / 2 * -1, (sizeSquares + spaceBetween) * rows / 2 * -1))
    
    square.present(update=False,clear=True)

    for r in range(rows):
        for c in range(columns):
            square.present(update=False, clear=False)
            square.move((spaceBetween + sizeSquares,0))
        square.move(((spaceBetween + sizeSquares) * columns * -1,0))
        square.move((0,spaceBetween + sizeSquares))
    square.move((0,(spaceBetween + sizeSquares) * -1))
    square.present(update=True,clear=False)
            
            

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

hermannGrid(sizeSquares = 30, colorSquares = "black", spaceBetween = 2, backgroundColor = C_GREY, rows = 10, columns = 20)