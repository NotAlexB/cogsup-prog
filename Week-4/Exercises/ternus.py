from expyriment import design, control, stimuli
import random
from expyriment.misc.constants import K_SPACE

colors = [(255,0,0), (0,255,0), (0,0,255)]

def load(stims):
    for stim in stims:
        stim.preload()
    
def timed_draw(stims):
    t0 = exp.clock.time
    for i, stim in enumerate(stims):
        stim.present(clear = (i == 0), update = (i == (len(stims) - 1)))
    t1 = exp.clock.time
    
    return t1 - t0
    # return the time it took to draw

def present_for(stims, t=200):
    time = timed_draw(stims)
    exp.clock.wait(t - time)
    
def make_circles(radius, tags = False):
    width = exp.screen.size[0]
    length = exp.screen.size[1]
    stims = []
    for i in range(3):
        stims.append(stimuli.Circle(radius = radius, position = (width / 3 * (i - 1), 0)))
        if tags:
            stims.append(stimuli.Circle(radius = 10, position = (width / 3 * (i - 1), 0), colour = colors[i]))
        else:
            stims.append(stimuli.Circle(radius = radius, position =  (width / 3 * (i - 1), 0)))
    return stims
    
def run_trial(radius, ISI, tags):
    circles = make_circles(radius, tags)
    while True:
        if exp.keyboard.check(K_SPACE):
            break
        load(circles)
        t0 = exp.clock.time
        present_for(circles[2:])
        t1 = exp.clock.time
        exp.clock.wait(ISI - (t1-t0))
        load(circles)
        t2 = exp.clock.time
        present_for(circles[:4])
        t3 = exp.clock.time
        exp.clock.wait(ISI - (t3-t2))
    


""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

run_trial(100,200,False)
run_trial(100,1000,False)
run_trial(100,1000,True)

control.end()