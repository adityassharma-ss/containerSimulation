# Container Terminal Simulation

This project simulates a basic container terminal using the SimPy library. The simulation includes vessels arriving at the terminal, berthing, and unloading containers using quay cranes and terminal trucks. The logic is built as per defined in the problem statement.

- I have uploaded same code in the both normal python file & notebook file.

# Table of Contents:

## Overview:

The goal of this simulation is to model the operations of a container terminal. It includes the following elements:

    Vessels arriving at random intervals.
    Berthing at one of the two available berths.
    Unloading containers using quay cranes.
    Transporting containers to the yard using terminal trucks.

## Simulation Details:

    Vessel Arrival: Vessels arrive at the terminal following an exponential distribution with an average interval of 5 hours.
    Berthing: There are 2 berths available at the terminal. If both berths are occupied, the vessel waits.
    Unloading: Each vessel carries 150 containers. A quay crane takes 3 minutes to unload each container.
    Transporting: There are 3 terminal trucks available to transport containers from the quay cranes to the yard. Each truck takes 6 minutes to transport a container and return.

## Usage:

    Save the code in a file named container_terminal_sim.py.
    Run the simulation: 

    ```
    python container_terminal_sim.py
    ```

## How It Solves the Problem:

The simulation models the operations of a container terminal, allowing us to observe and analyze the flow of vessels, the utilization of resources (berths, cranes, and trucks), and potential bottlenecks. By using SimPy, we can efficiently manage resource allocation and scheduling, providing insights into the terminal's operations.

You can customize the simulation by changing the parameters in the container_terminal_sim.py file, such as the number of berths, cranes, and trucks, the inter-arrival time of vessels, and the time taken for discharging and transporting containers.

## Solution Explaination:

The container terminal simulation models the arrival, berthing, and unloading of vessels using the SimPy library. Vessels arrive at random intervals, determined by an exponential distribution, and request one of the two berths. Once berthed, a vessel uses one of two quay cranes to unload its 150 containers. Each container is then transported to the yard by one of three available trucks. The unloading and transportation processes are simulated by requesting the respective resources (cranes and trucks), performing the operations (taking a fixed amount of time), and logging each event. The simulation tracks and logs the sequence of events, including vessel arrivals, container discharges, and container transportations, providing insights into the terminal's operation and resource utilization over a specified simulation time.