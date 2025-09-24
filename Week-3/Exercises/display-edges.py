# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Circle")

control.set_develop_mode()

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

#control.set_develop_mode()

width = exp.screen.size[0]
length = exp.screen.size[1]

square1 = stimuli.Rectangle((width // 20, width // 20), line_width= 1, position = (width//2 - width // 40, length //2-1 - width // 40), colour='red')
square2 = stimuli.Rectangle((width // 20, width // 20), line_width= 1, position = (((width//2) * -1) + width // 40, length //2 - width // 40), colour='red')
square3 = stimuli.Rectangle((width // 20, width // 20), line_width= 1, position = (width//2 - width // 40, ((length //2) * -1) + width // 40), colour='red')
square4 = stimuli.Rectangle((width // 20, width // 20), line_width= 1, position = (((width//2) * -1) + width // 40, ((length //2) * -1) + width // 40), colour='red')
 
square1.present(clear=True, update=False)
square2.present(clear=False, update= False)
square3.present(clear=False, update=False)
square4.present(clear=False, update= True)

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