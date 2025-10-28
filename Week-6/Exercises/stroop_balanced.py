from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_j, K_f
import random
import itertools
import csv

""" Constants """
KEYS = [K_j, K_f]
TRIAL_TYPES = ["match", "mismatch"]
COLORS = ["red", "blue", "green","orange"]

N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16

INSTR_START = """
In this task, you have to indicate whether the meaning of a word and the color of its font match.
Press J if they do, F if they don't.\n
Press SPACE to continue.
"""
INSTR_MID = """You have finished half of the experiment, well done! Your task will be the same.\nTake a break then press SPACE to move on to the second half."""
INSTR_END = """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = """Correct"""
FEEDBACK_INCORRECT = """Wrong"""

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()
    
def derangements(lst):
    ders = []
    for perm in itertools.permutations(lst):
        if all(origional != perm[idx] for idx, origional in enumerate(lst)):
            ders.append(perm)
    return ders
    
PERMS = derangements(COLORS)
#print(PERMS)


def subject_trials(subject_id):
    perm = PERMS[(subject_id-1) % len(PERMS)]
    base = [{"word" : w, "color": w} for w in COLORS] + [{"word" : w, "color":c} for w, c in zip(COLORS,perm)]

    block_reps = N_TRIALS_IN_BLOCK // len(base)
    trials = []
    
    for b_index in range(1,N_BLOCKS + 1):
        block = base * block_reps
        random.shuffle(block)
        for t_index, trial in enumerate(block, 1):
            trials.append({
                "subject_id" : subject_id, "block_id": b_index, "trial_id": t_index,
                "trial_type": "match" if trial["word"] == trial["color"] else "mismatch",
                "word": trial["word"], "color": trial["color"]
                #"correct_key": ord(trial["color"][0])
            })
    return trials
"""
N_SUBJECTS = 1

all_trials = [trial for id in range(1,N_SUBJECTS + 1) for trial in subject_trials(id)]

csv_cols = ["subject_id", "block_id", "trial_id", "trial_type", "word", "color"]

with open("cb.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=csv_cols)
    w.writeheader()
    w.writerows(all_trials)
    
assert(1==0)
"""
""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_cnt', 'trial_cnt', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

stims = stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

""" Experiment """
def run_trial(subject_id, block_id, trial_id, trial_type, word, color):
    stim = stims[word][color]
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(KEYS)
    correct = key == K_j if trial_type == "match" else key == K_f
    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])
    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=1000)

control.start(subject_id=1)

present_instructions(INSTR_START)

subject_id = 1

with open("cb.csv", "r") as f:
    reader = csv.DictReader(f)
    trials = [row for row in reader if row["subject_id"] == str(subject_id)]

for trial in trials:
    if trial["trial_id"] == 1 and trial["block_id"] != 1:
        present_instructions(INSTR_MID)
    run_trial(**trial)
    
    
"""
for block_id in range(1, N_BLOCKS + 1):
    for trial_id in range(1, N_TRIALS_IN_BLOCK + 1):
        trial_type = random.choice(TRIAL_TYPES)
        if trial_type == "match":
            word = random.choice(COLORS)
            color = word
        else:
            while True:
                word = random.choice(COLORS)
                color = random.choice(COLORS)
                if not (word == color):
                    break
        run_trial(block_id, trial_id, trial_type, word, color)
    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)
"""
present_instructions(INSTR_END)

control.end()