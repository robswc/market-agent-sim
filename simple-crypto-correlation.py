from agents.agent_sim import Agent
from engines.simple_matching_engine import SimpleEngine
import random
import time
from datetime import datetime
import csv

def import_csv(file):
    with open(file, newline='') as f:
        return list(csv.reader(f))[0]

def create_agents(n_agents):
    # Create agent list
    agent_list = []
    for i in range(n_agents):
        # Create a new_agent var, set it to Agent() Class.
        new_agent = Agent()
        # Set new_agent's name to i.
        new_agent.name = i
        # Give agent a strategy.
        selector = random.randint(1, 5)
        if selector == 1:
            new_agent.strategy.append('rsi')
        if selector == 2:
            new_agent.strategy.append('rsi')
        if selector == 3:
            new_agent.strategy.append('rsi')
        if selector == 4:
            new_agent.strategy.append('rsi')
        if selector == 5:
            new_agent.strategy.append('noise')
        # Add new agent to the list of agent classes.
        agent_list.append(new_agent)

    # Return the agent list
    return agent_list


# Creates 10 agents
agents = create_agents(50)

# Create engine object.
Engine = SimpleEngine()


# Starts the simulation
Engine.set_price(int(import_csv('data/crypto/latest.csv')[400]))
print('set price', int(import_csv('data/crypto/latest.csv')[400]))
time.sleep(2)
def start_sim(steps, save):
    price_data = import_csv('data/crypto/latest.csv')[:400]
    price_data = list(map(int, price_data))
    Engine.set_price(int(import_csv('data/crypto/latest.csv')[400]))
    for i in range(steps):
        for agent in agents:
            agent_action = agent.process_state(price_data)
            Engine.add_order(agent_action)
            # print(agent_action)
            # print(Engine.get_price())
            price_data.append(Engine.get_price())
            print('*End Tick*\n')

    if save:
        # print(price_data)
        # datetime.now().strftime("%d-%b-%Y %H-%M-%S")
        with open('data/saved/{}.csv'.format('latest'), 'w', newline='') as f:
            w = csv.writer(f)
            w.writerows([price_data])

    Engine.set_price(int(import_csv('data/saved/latest.csv')[100]))
    return price_data


# Start simulation, do 10 steps.
# start_sim(100, save=True)

def monte_carlo(sims, steps):
    monte_carlo_list = []
    for i in range(sims):
        monte_carlo_list.append(start_sim(steps, save=False))

    monte_carlo_list.append(import_csv('data/crypto/latest.csv'))
    with open('data/monte-carlo/{}.csv'.format('latest'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerows(monte_carlo_list)

monte_carlo(10, 500)