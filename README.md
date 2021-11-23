# Competition 1v1 running

## Environment

<img src=https://github.com/jidiai/Competition_Olympics-Running/blob/main/assets/olympics%20running.gif width=600>

check details in Jidi Competition [RLChina2021智能体竞赛](http://www.jidiai.cn/compete_detail?compete=12)


### 做出的修改：

<b>奖励重塑：</b>修改了环境，重新设置了奖励的分配，使得奖励组成不只有零和博弈，还有探索环境的奖励。

<b>算法微调：</b>修改了官方PPO算法的actor loss部分，增加了对actor分布熵的约束，未来计划加入RND、ICM等辅助部件。


---
## Dependency

>conda create -n olympics python=3.8.5

>conda activate olympics

>pip install -r requirements.txt

---

## Run a game

>python olympics/main.py

---

## Train a baseline agent 

>python rl_trainer/main.py

By default parameters, the total reward of training is shown below.

<img src=https://github.com/jidiai/Competition_Olympics-Running/blob/main/assets/PPO%20map1%20training%20(run1).png>
