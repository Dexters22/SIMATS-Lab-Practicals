import numpy as np, random

# Frozen Lake Grid: S=0,F=0,H=-1,G=1
grid = np.array([[0,0,0,-1],[0,-1,0,-1],[0,0,0,1]])
actions = ['up','down','left','right']
Q = np.zeros((3,4,4))  # states x actions

alpha, gamma, eps = 0.8, 0.9, 0.2

def move(s,a):
    i,j=s
    if a=='up': i-=1
    elif a=='down': i+=1
    elif a=='left': j-=1
    elif a=='right': j+=1
    if 0<=i<3 and 0<=j<4: return (i,j)
    return s

for _ in range(1000):
    s = (0,0)
    done=False
    while not done:
        a = random.choice(actions) if random.random()<eps else actions[np.argmax(Q[s])]
        ns = move(s,a)
        r = 100 if grid[ns]==1 else -1 if grid[ns]==0 else -100
        Q[s][actions.index(a)] += alpha*(r + gamma*max(Q[ns]) - Q[s][actions.index(a)])
        s = ns
        if grid[s]!=0: done=True

# Test learned policy
s=(0,0)
path=[s]
while grid[s]!=1:
    a = actions[np.argmax(Q[s])]
    s=move(s,a)
    path.append(s)
print("Optimal path:", path)
