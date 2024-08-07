# Particle-Swarn-Optimization

This repository contains a Python implementation of the Particle Swarm Optimization (PSO) algorithm to solve the Traveling Salesman Problem (TSP).

# Overview

The Traveling Salesman Problem (TSP) is a well-known combinatorial optimization problem that aims to find the shortest possible route visiting each city exactly once and returning to the origin city. This implementation uses the Particle Swarm Optimization (PSO) algorithm, a computational method inspired by the social behavior of birds flocking or fish schooling, to find an approximate solution to the TSP.

# Installation

To run the code, you need to have Python installed on your machine. You can install the required libraries using the following command:

pip install numpy

# Usage

The main script pso_tsp.py runs the PSO algorithm to solve the TSP. You can modify the parameters such as the number of particles and the number of iterations to see how they affect the solution.

# Functions

calculate_distance(tour, distance_matrix): 
Calculates the total distance of a given tour based on the distance matrix.

initialize_particles(num_particles, num_cities): 
Initializes the particles with random tours.

update_velocity(particle, p_best, g_best): 
Updates the velocity of a particle based on its personal best tour and the global best tour.

apply_velocity(particle, velocity): 
Applies the velocity to a particle to generate a new tour.

pso_tsp(distance_matrix, num_particles=30, max_iterations=1000): 
Main function to solve the TSP using PSO.