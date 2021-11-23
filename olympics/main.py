import sys
from os import path
father_path = path.dirname(__file__)
sys.path.append(str(father_path))
from generator import create_scenario
import argparse
from agent import *
import time
from scenario.running import Running


import random
import numpy as np
import matplotlib.pyplot as plt
import json

import cv2

def store(record, name):
    with open('logs/'+name+'.json', 'w') as f:
        f.write(json.dumps(record))

def load_record(path):
    file = open(path, "rb")
    filejson = json.load(file)
    return filejson

RENDER = True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--map', default="map4", type=str,
                        help= "map1/map2/map3/map4")
    parser.add_argument("--seed", default=1, type=int)
    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)

    agent1 = random_agent()
    agent2 = random_agent()

    map_index_seq = list(range(5,7))
    time_s = time.time()
    for i in range(20):
        print("==========================================")
        ind = map_index_seq.pop(0)
        print("map index: ", ind)
        Gamemap = create_scenario("map"+str(ind))
        map_index_seq.append(ind)

        rnd_seed = random.randint(0, 1000)
        game = Running(Gamemap, seed = rnd_seed)
        game.map_num =ind

        obs = game.reset()
        if RENDER:
            game.render()

        done = False
        step = 0
        if RENDER:
            game.render('MAP {}'.format(ind))

        while not done:
            step += 1

            #action1 = agent1.act(obs[0])
            #action2 = agent2.act(obs[1])
            action1 = [0, 0]
            action2 = [0, 0]

            obs_visual = np.array(obs[0])
            obs_visual[obs_visual > 4] = 0
            cv2.imshow("vis", obs_visual)
            key = cv2.waitKey(200)
            if key == 97:
                action1[1] -= 10
            elif key == 100:
                action1[1] += 10
            elif key == 119:
                action1[0] += 10
            elif key == 115:
                action1[0] -= 10

            #print("obs0:{} \n\n obs1:{} \n".format(obs[0], obs[1]))

            obs, reward, done, _ = game.step([action1, action2])

            if RENDER:
                game.render()

        print('Episode Reward = {}'.format(reward))

