from project.datasets import Simple, Split, Xor
N = 200

def classify_simple(pt):
    "Classify based on x position"
    if pt[0] >= 0.50:
        return 0
    else:
        return 1

def classify_split(pt):
    "Classify based on x position"
    if pt[0] >= 0.20 and pt[0] <= 0.8:
        return 0
    else:
        return 1

def classify_xor(pt):
    "Classify based on x position"
    if (pt[0] <= 0.4 and pt[1] <= 0.4) or (pt[0] >=0.50 and pt[1] >= 0.50):
        return 0
    else:
        return 1

Simple(N, vis=True).graph("simple", model=classify_simple)
Split(N, vis=True).graph('split', model=classify_split)
Xor(N, vis=True).graph('xor', model=classify_xor)