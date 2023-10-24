# This program tests the performance of insertion sort vs selection sort in differing scenarios through Terminal.

# Imports
import subprocess

# Establishes test parameters
sizes = ['10000', '20000', '30000', '40000', '50000']
orientations = ['increasing', 'decreasing', 'random']

# Algorithm to run test
for orientation in orientations:
    for size in sizes:
        command = ['python', '-m', 'trace', '--count', '-C', '.', 'Sort.py', size, orientation]
        subprocess.run(command)
        input('paused')