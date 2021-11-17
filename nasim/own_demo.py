"""Script for running PenboxDemoScenario 1

Usage
-----

$ python demo [-ai] [-h] env_name
"""

import os.path as osp

import nasim
from nasim.agents.dqn_agent import DQNAgent
from nasim.agents.keyboard_agent import run_keyboard_agent, run_generative_keyboard_agent

DQN_POLICY_DIR = osp.join(
    osp.dirname(osp.abspath(__file__)),
    "agents",
    "policies"
)
DQN_POLICIES = {
    "tiny": osp.join(DQN_POLICY_DIR, "dqn_tiny.pt"),
    "small": osp.join(DQN_POLICY_DIR, "dqn_small.pt")
}

##Set the scenario
scenario = 15

if __name__ == "__main__":
    #Change Envirnoment 
    env = nasim.load("nasim\scenarios\own_S\Permutations\Own_S_14.yaml")


    line_break = f"\n{'-' * 60}"
    print(line_break)
    print(f"Running Demo on Penbox environment")
    print("Player controlled")
    ret, steps, goal = run_generative_keyboard_agent(env, "readable")
    print(line_break)
    print("Episode Complete")
    print(line_break)
    if goal:
        print("Goal accomplished. Sensitive data retrieved!")
    print(f"Final Score={ret}")
    print(f"Steps taken={steps}")

