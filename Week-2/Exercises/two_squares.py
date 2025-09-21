# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Circle")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
#fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered


harry = stimuli.Rectangle((50,50), colour = "red", position = (-100,0))

josh = stimuli.Rectangle((50,50), colour = "green", position=(100,0))

# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross


# Leave it on-screen for 1,000 ms

# Remove the cross and replace it with a circle
josh.present(clear=True, update=False)

harry.present(clear=False, update=True)

#exp.clock.wait(500)

#circle.present(clear=True, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()