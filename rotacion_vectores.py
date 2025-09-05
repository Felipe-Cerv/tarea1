#Cervantes Hernandez Jose Felipe 5-3

import numpy as np


def rot_x(x: float, y: float, z: float, theta: float) -> np.ndarray:
    """
    Rota un vector (x, y, z) sobre del eje X por un angulo determinado.

    Parameters:
        x (float): coordenada en el eje X del punto original.
        y (float): coordenada en el eje Y del punto original.
        z (float): coordenada en el eje Z del punto original.
        theta (float): ángulo de rotación en radianes.

    Returns:
        np.ndarray: vector rotado como numpy array [x', y', z'].
    """
    p = np.array([x, y, z])
    R = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])
    return R @ p


def rot_y(x: float, y: float, z: float, theta: float) -> np.ndarray:
    """
    Rota un vector (x, y, z) sobre del eje y por un angulo determinado.

    Parameters:
        x (float): coordenada en el eje X del punto original.
        y (float): coordenada en el eje Y del punto original.
        z (float): coordenada en el eje Z del punto original.
        theta (float): ángulo de rotación en radianes.

    Returns:
        np.ndarray: vector rotado como numpy array [x', y', z'].
    """
    p = np.array([x, y, z])
    R = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return R @ p


def rot_z(x: float, y: float, z: float, theta: float) -> np.ndarray:
    """
    Rota un vector (x, y, z) sobre del eje z por un angulo determinado.

    Parameters:
        x (float): coordenada en el eje X del punto original.
        y (float): coordenada en el eje Y del punto original.
        z (float): coordenada en el eje Z del punto original.
        theta (float): ángulo de rotación en radianes.

    Returns:
        np.ndarray: vector rotado como numpy array [x', y', z'].
    """
    p = np.array([x, y, z])
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])
    return R @ p


def rotar(x: float, y: float, z: float, theta: float, axis: str) -> np.ndarray:
    """
    Rota un vector (x, y, z) un ángulo theta alrededor de un eje específico.

    Parameters:
        x (float): coordenada en el eje X del punto original.
        y (float): coordenada en el eje Y del punto original.
        z (float): coordenada en el eje Z del punto original.
        theta (float): ángulo de rotación en radianes.
        axis (str): eje de rotación; puede ser 'x', 'y' o 'z'.

    Returns:
        np.ndarray: vector rotado como numpy array [x', y', z'].
    """
    if axis == 'x':
        return rot_x(x, y, z, theta)
    elif axis == 'y':
        return rot_y(x, y, z, theta)
    elif axis == 'z':
        return rot_z(x, y, z, theta)
    else:
        raise ValueError("El eje debe ser 'x', 'y' o 'z'.")
    

x = float(input("Posicion inicial en x: "))
y = float(input("Posicion inicial en y: "))
z = float(input("Posicion inicial en z: "))
angulo = float(input("Angulo de rotacion en grados: "))
eje = input("Eje de rotacion (x, y, z): ")

resultado = rotar(x, y, z, np.deg2rad(angulo), eje)

print("Vector rotado:", resultado)