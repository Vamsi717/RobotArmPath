import math
import numpy as np
import matplotlib.pyplot as plt

def cylindrical_Coordinates(coordinate,length,angle):
    res_Cor = [0 ,0]
    res_Cor[0] = coordinate[0] + length*math.cos(math.radians(angle))
    res_Cor[1] = coordinate[1] + length*math.sin(math.radians(angle))
    return res_Cor

def arm_endPoint(initial_Cor,lengths,angles):
    endPoint = initial_Cor
    angle = 0
    for i in range(len(lengths)):
        angle += angles[i]
        endPoint = cylindrical_Coordinates(endPoint,lengths[i],angle)
    endPoint = np.round_(endPoint,decimals=3)
    return endPoint

def main():
    arms = [1,1,1]
    initial_angles = [60,-60,-60]
    fixed_Point = [0,0]
    endPoint = arm_endPoint(fixed_Point,arms,initial_angles)
    print(endPoint)


if __name__ == "__main__":
    main()