# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Circle")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
#fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered

# Create a 50px-radius circle
harry = stimuli.Shape(vertex_list = geometry.vertices_regular_polygon(3,50), colour = "purple", position=(-100,0))

josh = stimuli.Shape(vertex_list = geometry.vertices_regular_polygon(6,28), colour = "yellow", position=(100,0))

line1 = stimuli.Line(start_point=(-100,20), end_point=(-100,70), line_width=3)
line2 = stimuli.Line(start_point=(100,20), end_point=(100,70), line_width=3)

text1 = stimuli.TextLine(text = "triangle", position = (-100,90), text_colour= "white")

text2 = stimuli.TextLine(text = "hexagon", position = (100,90), text_colour= "white")

# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross


# Leave it on-screen for 1,000 ms

# Remove the cross and replace it with a circle

#exp.keyboard.wait()

line1.present(clear = True, update = False)\

text1.present(clear = False, update = False)

harry.present(clear=False, update=False)

line2.present(clear = False, update = False)

text2.present(clear = False, update = False)

josh.present(clear=False, update=True)



#exp.clock.wait(500)

#circle.present(clear=True, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()