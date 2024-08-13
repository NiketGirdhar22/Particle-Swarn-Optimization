import numpy as np
import random

def calculate_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i - 1], tour[i]] for i in range(len(tour)))

def initialize_particles(num_particles, num_cities):
    particles = []
    for _ in range(num_particles):
        tour = list(range(num_cities))
        random.shuffle(tour)
        particles.append(tour)
    return particles

def update_velocity(particle, p_best, g_best):
    new_velocity = []
    for i in range(len(particle)):
        if random.random() < 0.5:
            swap_index = p_best.index(particle[i])
            new_velocity.append((i, swap_index))
        if random.random() < 0.5:
            swap_index = g_best.index(particle[i])
            new_velocity.append((i, swap_index))
    return new_velocity

def apply_velocity(particle, velocity):
    new_particle = particle[:]
    for (i, j) in velocity:
        new_particle[i], new_particle[j] = new_particle[j], new_particle[i]
    return new_particle

def pso_tsp(distance_matrix, num_particles=30, max_iterations=1000):
    num_cities = distance_matrix.shape[0]
    particles = initialize_particles(num_particles, num_cities)
    velocities = [[] for _ in range(num_particles)]

    p_best = particles[:]
    p_best_distances = [calculate_distance(tour, distance_matrix) for tour in particles]

    g_best = min(particles, key=lambda tour: calculate_distance(tour, distance_matrix))
    g_best_distance = calculate_distance(g_best, distance_matrix)

    for iteration in range(max_iterations):
        for i in range(num_particles):
            particle = particles[i]
            velocity = update_velocity(particle, p_best[i], g_best)
            new_particle = apply_velocity(particle, velocity)

            particles[i] = new_particle
            velocities[i] = velocity

            current_distance = calculate_distance(new_particle, distance_matrix)
            if current_distance < p_best_distances[i]:
                p_best[i] = new_particle
                p_best_distances[i] = current_distance

                if current_distance < g_best_distance:
                    g_best = new_particle
                    g_best_distance = current_distance

        print(f"Iteration {iteration+1}/{max_iterations}, Best Distance: {g_best_distance}")

    return g_best, g_best_distance

num_cities = 5
random_matrix = np.random.rand(num_cities, num_cities)
distance_matrix = 20 + random_matrix * (150 - 20)
print(distance_matrix)
best_tour, best_distance = pso_tsp(distance_matrix, num_particles=30, max_iterations=100)
print(f"Best Tour: {best_tour}")
print(f"Best Distance: {best_distance}")
