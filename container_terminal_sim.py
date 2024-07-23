import simpy
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

RANDOM_SEED = 42
SIMULATION_TIME = 1000  
INTER_ARRIVAL_TIME = 5  
CONTAINERS_PER_VESSEL = 150
TIME_TO_DISCHARGE_CONTAINER = 3 
TIME_TO_TRANSPORT_CONTAINER = 6 

NUMBER_OF_BERTHS = 2
NUMBER_OF_CRANES = 2
NUMBER_OF_TRUCKS = 3

class ContainerTerminal:
    def __init__(self, env):
        self.env = env
        self.berths = simpy.Resource(env, NUMBER_OF_BERTHS)
        self.cranes = simpy.Resource(env, NUMBER_OF_CRANES)
        self.trucks = simpy.Resource(env, NUMBER_OF_TRUCKS)

    def discharge_container(self, vessel_id):
        yield self.env.timeout(TIME_TO_DISCHARGE_CONTAINER)
        logging.info(f'Time {self.env.now}: Vessel {vessel_id} discharges a container')

    def transport_container(self, vessel_id):
        yield self.env.timeout(TIME_TO_TRANSPORT_CONTAINER)
        logging.info(f'Time {self.env.now}: Truck transports a container for Vessel {vessel_id}')

    def handle_vessel(self, vessel_id):
        logging.info(f'Time {self.env.now}: Vessel {vessel_id} arrives')
        with self.berths.request() as berth_request:
            yield berth_request
            logging.info(f'Time {self.env.now}: Vessel {vessel_id} berths')
            for _ in range(CONTAINERS_PER_VESSEL):
                with self.cranes.request() as crane_request:
                    yield crane_request
                    logging.info(f'Time {self.env.now}: Crane starts discharging a container from Vessel {vessel_id}')
                    yield self.env.process(self.discharge_container(vessel_id))

                with self.trucks.request() as truck_request:
                    yield truck_request
                    logging.info(f'Time {self.env.now}: Truck starts transporting a container for Vessel {vessel_id}')
                    yield self.env.process(self.transport_container(vessel_id))

            logging.info(f'Time {self.env.now}: Vessel {vessel_id} leaves')

def vessel_generator(env, terminal):
    vessel_id = 0
    while True:
        yield env.timeout(random.expovariate(1 / INTER_ARRIVAL_TIME) * 60)  
        vessel_id += 1
        env.process(terminal.handle_vessel(vessel_id))

def main():
    random.seed(RANDOM_SEED)
    env = simpy.Environment()
    terminal = ContainerTerminal(env)
    env.process(vessel_generator(env, terminal))
    env.run(until=SIMULATION_TIME)

if __name__ == '__main__':
    main()

