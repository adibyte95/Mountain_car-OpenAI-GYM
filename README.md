# TOPIC
A car is on a one-dimensional track, positioned between two "mountains". The goal is to drive up the mountain on the right; however, the car's engine is not strong enough to scale the mountain in a single pass. Therefore, the only way to succeed is to drive back and forth to build up momentum.

# Approach
in this game no intermediate rewards is given. only a final reward is given when the cart reaches the flag. So in order to steer the cart towards the flag we have give reward of +15 if the cart pulls back on the left hill or moves forward on the right hill. further more there is an penalty of -10 for each step that the cart takes, this ensures that the cart reaches the goal(flag) in minimum number of timesteps also huge reward of +10000 is given if the cart finaly reaches the flag in less than 200 timesteps which is our goal. 

# Gameplay
![gameplay video](https://github.com/adibyte95/Mountain_car-OpenAI-GYM/blob/master/media/gameplay.gif)

# Note
pull requests for further improvement is invited
