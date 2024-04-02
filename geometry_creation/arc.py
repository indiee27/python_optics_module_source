from os import error
from matplotlib import pyplot as plt
import numpy as np
from numpy.core.defchararray import find, index
from scipy.sparse import dia
import math

def make_arc(grid_size, arc_pos, radius, diameter, focus_pos, plot_arc_def=False):
    grid_size = round(grid_size)
    arc_pos = round(arc_pos)
    focus_pos = round(arc_pos)
    diameter = round(diameter)
    radius = round(radius)

    if any(grid_size < 1):
        error_message = "The grid size must be positive"
        raise ValueError(error_message)
    
    if radius <= 0:
        error_message = "Radius must be positive"
        raise ValueError(error_message)
    
    if diameter <= 0:
        error_message = "Diameter must be positive"
        raise ValueError(error_message)

    if any(arc_pos < 1) or any(arc_pos > grid_size):
        error_message = "The centre of the arc must be in the grid"
        raise ValueError(error_message)

    if diameter > 2*radius:
        error_message = "The diameter of the arc must be less than twice the radius of curvature"
        raise ValueError(error_message)
    
    if math.remainder(diameter,2):
        error_message = "The diameter must be an odd number of grid points"
        raise ValueError(error_message)
    
    if all(arc_pos == focus_pos):
        error_message = "The focus_pos must be different to the arc_pos"
        raise ValueError(error_message)
    
    Nx = grid_size[0]
    Ny = grid_size[1]
    ax = arc_pos[0]
    ay = arc_pos[1]
    fx = focus_pos[0]
    fy = focus_pos[1]

    if radius.imag != 0:
        half_arc_angle = math.asin(diameter / 2 / radius)

        distance_cf = math.sqrt(math.pow((ax-fx),2) + math.pow((ay-fy),2))
        cx = round(radius/distance_cf*(fx - ax) + ax)
        cy = round(radius/distance_cf*(fy - ay) + ay)
        c = (cx, cy)

        arc = make_circle(Nx, Ny, cx, cy, radius)

        v1 = arc_pos - c

        length_1 = math.sqrt(sum(math.pow((arc_pos),2)))

        arc_ind = find(arc == 1)

        for item in arc_ind:
            p = np.unravel_index([Nx, Ny], arc_ind(item))

            v2 = p - c

            length_2 = math.sqrt(sum(math.pow((p-c),2)))

            theta = math.acos(sum(v1*v2/(length_1*length_2)))

            if theta > half_arc_angle:
                arc(arc_ind(item)) = 0
        
    else:
        ang = math.atan((fx - ax)/(fy - ay)) + math.pi/2

        arc = make_line(Nx, Ny, arc_pos, ang, (diameter - 1)/2) or make_line(Nx, Ny, arc_pos, ang + math.pi, (diameter - 1)/2)

    if plot_arc_def = True:
        ax = plt.figure()
        plt.imshow(arc, extent=[-1, 1])
        plt.xlabel("X-position [grid points]")
        plt.ylabel("Y-position [grid points]")

    return arc