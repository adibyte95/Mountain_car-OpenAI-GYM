import gym
import keras
from keras.models import load_model
import numpy as np
from gym import wrappers

model = load_model('mountain_car-dqn_model.h5')
env = gym.make('MountainCar-v0').env
env= wrappers.Monitor(env, 'submission files', force = True)

scores = 0
EPISODES = 1

for e in range(EPISODES):
    state = env.reset()
    done = False
    time_taken = 0
    while not done:
        # uncomment this to see the actual rendering 
        env.render()
        time_taken +=1
        state = np.reshape(state, [1,2])
        action = model.predict(state)
        action = np.argmax(action)
        next_state, reward, done, info = env.step(action)
        state = next_state
    print('time taken:', time_taken)