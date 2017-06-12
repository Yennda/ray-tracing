from algebra import la
import numpy.linalg as l
import numpy as np
import math as m
from scipy import constants as c
import matplotlib.pyplot as plt


class Tools:
    @staticmethod
    def mm_from_ang(x):
        return x * 1e-12

    @staticmethod
    def deg_from_rad(x):
        return x / (2 * m.pi) * 360

    @staticmethod
    def rad_from_deg(x):
        return x / 180 * m.pi

    @staticmethod
    def ang_from_kev(e):
        return c.c / (e * 1e3 * c.eV / c.h) * 1e10

    @staticmethod
    def kev_from_ang(l):
        return c.c * c.h / c.e / (l * 1e-10) / 1e3

    @staticmethod
    def mol(x, y, e):
        return ((y - e) < x) and (x < (y + e))

    @staticmethod
    def mols(x, y, e: float):
        norm = la.norm(la.minus(x, y))
        return norm < e

    @staticmethod
    def normalize(vec):
        norm = l.norm(vec)
        if norm == 0:
            raise ValueError
        return vec / norm

    @staticmethod
    def rotate(vec, angles):
        # if u == 'r':
        #     angles = la.x(angles, m.pi)
        # elif u == 'd':
        #     angles = [Tools.rad_from_deg(a) for a in angles]

        Rx = [
            [1, 0, 0],
            [0, m.cos(angles[0]), -m.sin(angles[0])],
            [0, m.sin(angles[0]), m.cos(angles[0])]
        ]
        Ry = [
            [m.cos(angles[1]), 0, m.sin(angles[1])],
            [0, 1, 0],
            [-m.sin(angles[1]), 0, m.cos(angles[1])]
        ]
        Rz = [
            [m.cos(angles[2]), -m.sin(angles[2]), 0],
            [m.sin(angles[2]), m.cos(angles[2]), 0],
            [0, 0, 1]
        ]
        return la.dotmv(Rx, la.dotmv(Ry, la.dotmv(Rz, vec)))

    @staticmethod
    def gauss(x, s, mi):
        output = m.exp(-(x - mi) ** 2 / (2 * s ** 2))
        if output < 1e-9:
            return 0
        return output

    @staticmethod
    def qroot(a, b, c):
        # print(a)
        # print(b)
        # print(c)
        D = b ** 2 - 4 * a * c
        if D < 0:
            raise ValueError
        elif D == 0:
            return -b / (2 * a)
        else:
            x1 = (-b + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)
            return x1

    @staticmethod
    def imaging_equation(f, a):
        return 1 / (1 / f - 1 / a)

    @staticmethod
    def shoelace(x: list):
        sum_first = 0
        sum_second = 0
        for i in range(len(x) - 1):
            sum_first += x[i][0] * x[i + 1][1]
            sum_second += x[i + 1][0] * x[i][1]
        return 0.5 * (sum_first + x[-1][0] * x[0][1] - sum_second - x[0][0] * x[-1][1])

    @staticmethod
    def vec_show(vectors: list):
        x = np.arange(0,1,0.01)
        fig, axes = plt.subplots(1, 3, figsize=(12, 4))
        # axes[0].set_title(vectors)
        axes[0].set_xlabel('x')
        axes[0].set_ylabel('y')
        axes[1].set_xlabel('z')
        axes[1].set_ylabel('x')
        axes[2].set_xlabel('z')
        axes[2].set_ylabel('y')
        for vec in vectors:
            axes[0].plot(vec[0]*x,vec[1]*x)
            axes[1].plot(vec[2] * x, vec[0] * x)
            axes[2].plot(vec[2] * x, vec[1] * x)
        fig.savefig('display/vec_show.png', dpi=200, bbox_inches='tight')
