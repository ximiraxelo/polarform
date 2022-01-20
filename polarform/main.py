import cmath
import numpy as np
import matplotlib.pyplot as plt
from utils import adjust_angle

RAD_TO_DEG = 180/np.pi
DEG_TO_RAD = np.pi/180
ORIGIN = [0, 0]

class Polar():
    '''
    polar.Polar(mag=0, phase=0)

    Represent a complex number in polar form

    Parameters:

    - mag: integer, float or complex
        The magnitude (absolute value) of the complex number

        This parameter can be a complex built-in python number, and they will be converted to a polar form

    - phase: integer or float
        The phase (angle) of the complex number in degrees

        This parameter, regardless of the input, operates in the interval [-180, 180]  
    
    Returns:

    - Polar: polar
        A polar representantion of a complex number, with magnitude and phase
    '''
    def __init__(self, mag=0, phase=0):
        if isinstance(mag, complex):
            self.mag = round(abs(mag), 6)
            self.phase = round(cmath.phase(mag) * RAD_TO_DEG, 4)
        else:
            self.mag = abs(float(mag))
            self.phase = float(adjust_angle(phase))

    def __repr__(self):
        return f'{self.mag}∠{self.phase}°'

    def __add__(self, operator):
        if isinstance(operator, int) or isinstance(operator, float):
            rectangular = self.rect() + operator
            return Polar(abs(rectangular), cmath.phase(rectangular) * RAD_TO_DEG)

        if isinstance(operator, complex):
            rectangular = self.rect() + operator
            return Polar(round(abs(rectangular), 6), round(cmath.phase(rectangular) * RAD_TO_DEG, 4))

        if isinstance(operator, Polar):
            rectangular = self.rect() + operator.rect()
            return Polar(abs(rectangular), cmath.phase(rectangular) * RAD_TO_DEG) 

    def __radd__(self, operator):
        if isinstance(operator, int) or isinstance(operator, float):
            rectangular = self.rect() + operator
            return Polar(abs(rectangular), cmath.phase(rectangular) * RAD_TO_DEG)

        if isinstance(operator, complex):
            rectangular = self.rect() + operator
            return Polar(round(abs(rectangular), 6), round(cmath.phase(rectangular) * RAD_TO_DEG, 4))

    def __sub__(self, operator):
        if isinstance(operator, int) or isinstance(operator, float):
            rectangular = self.rect() - operator
            return Polar(abs(rectangular), cmath.phase(rectangular) * RAD_TO_DEG)

        if isinstance(operator, complex):
            rectangular = self.rect() - operator
            return Polar(round(abs(rectangular), 6), round(cmath.phase(rectangular) * RAD_TO_DEG, 4))

        if isinstance(operator, Polar):
            rectangular = self.rect() - operator.rect()
            return Polar(abs(rectangular), cmath.phase(rectangular) * RAD_TO_DEG)

    def __rsub__(self, operator):
        if isinstance(operator, int) or isinstance(operator, float):
            rectangular = self.rect() - operator
            return Polar(abs(rectangular), cmath.phase(rectangular) * RAD_TO_DEG)

        if isinstance(operator, complex):
            rectangular = self.rect() - operator
            return Polar(round(abs(rectangular), 6), round(cmath.phase(rectangular) * RAD_TO_DEG, 4))

    def __mul__(self, operator):
        if isinstance(operator, int) or isinstance(operator, float):
            mag_res = self.mag * operator
            return Polar(mag_res, self.phase)

        if isinstance(operator, complex):
            mag_res = self.mag * abs(operator)
            phase_res = self.phase + cmath.phase(operator)*RAD_TO_DEG
            return Polar(round(mag_res, 6), round(phase_res, 4))

        if isinstance(operator, Polar):
            mag_res = self.mag * operator.mag
            phase_res = self.phase + operator.phase
            return Polar(mag_res, phase_res)

    def __rmul__(self, operator):
        if isinstance(operator, int) or isinstance(operator, float):
            mag_res = self.mag * operator
            return Polar(mag_res, self.phase)

        if isinstance(operator, complex):
            mag_res = self.mag * abs(operator)
            phase_res = self.phase + cmath.phase(operator)*RAD_TO_DEG
            return Polar(round(mag_res, 6), round(phase_res, 4))

    def __truediv__(self, operator):
        if isinstance(operator, int) or isinstance(operator, float):
            mag_res = self.mag / operator
            return Polar(mag_res, self.phase)

        if isinstance(operator, complex):
            mag_res = self.mag / abs(operator)
            phase_res = self.phase - cmath.phase(operator)*RAD_TO_DEG
            return Polar(round(mag_res, 6), round(phase_res, 4))

        if isinstance(operator, Polar):
            mag_res = self.mag / operator.mag
            phase_res = self.phase - operator.phase
            return Polar(mag_res, phase_res)

    def __rtruediv__(self, operator):
        if isinstance(operator, int) or isinstance(operator, float):
            mag_res = self.mag / operator
            return Polar(mag_res, self.phase)

        if isinstance(operator, complex):
            mag_res = self.mag / abs(operator)
            phase_res = self.phase - cmath.phase(operator)*RAD_TO_DEG
            return Polar(round(mag_res, 6), round(phase_res, 4))

    def __pow__(self, operator):
        if operator >= 0 and isinstance(operator, int):
            mag_res = (self.mag ** operator)
            phase_res = adjust_angle(self.phase * operator)
            return Polar(mag_res, phase_res)

    def __abs__(self):
        return self.mag

    def __complex__(self):
        return self.rect()

    def __eq__(self, operator):
        if isinstance(operator, Polar):
            if (self.mag == operator.mag) and (self.phase == operator.phase):
                return True
            return False

        if isinstance(operator, complex):
            if (self.mag == abs(operator)) and (self.phase == cmath.phase(operator) * RAD_TO_DEG):
                return True
            return False

    def __ne__(self, operator):
        if isinstance(operator, Polar):
            if (self.mag == operator.mag) and (self.phase == operator.phase):
                return False
            return True

        if isinstance(operator, complex):
            if (self.mag == abs(operator)) and (self.phase == cmath.phase(operator) * RAD_TO_DEG):
                return False
            return True

    def __round__(self, n=0):
        return Polar(round(self.mag, n), round(self.phase, n))

    def __getitem__(self, index):
        if index == 0:
            return self.mag
        if index == 1:
            return self.phase
        else:
            raise IndexError(f'the index {index} is out of range (0 or 1)')

    def rad(self):
        '''
        Polar.rad()

        Show the polar form with the phase in radians

        Will always be in the interval [-π/2, π/2]

        Returns: 

        - radians_form: string
        '''
        return f'{self.mag}∠{self.phase*DEG_TO_RAD} rad'

    def rect(self):
        '''
        Polar.rect()

        A rectangular representation of the polar form of the number

        Returns:

        - polar_form: complex
            A number in the form a + bj, where a and b can be integers or floats, and j represents the imaginary unit
        '''
        mag_abs = round(self.mag * np.cos(self.phase * DEG_TO_RAD),6)
        phase_abs = round(self.mag * np.sin(self.phase * DEG_TO_RAD),6)
        return complex(mag_abs, phase_abs) 

    def conj(self):
        '''
        Polar.conj()

        The complex conjugate of the polar form

        In practical case is a polar with the same magnitude and inverse phase

        Returns:

        - conjugate: polar
        '''
        return Polar(self.mag, -self.phase)

    def show(self, color='r', grid=True):
        mag_abs = self.mag * np.cos(self.phase * DEG_TO_RAD)
        phase_abs = self.mag * np.sin(self.phase * DEG_TO_RAD)
        lim = abs(np.ceil(self.mag * 1.2))
        plt.xlim(-lim, lim)
        plt.ylim(-lim, lim)
        plt.ylabel('Im', fontfamily='serif', fontsize=14)
        plt.xlabel('Re', fontfamily='serif', fontsize=14)
        if grid == True: plt.grid(linewidth=0.3) 
        plt.quiver(*ORIGIN, mag_abs, phase_abs, 
                    scale=1, 
                    scale_units='xy',
                    angles='xy', 
                    color=color, 
                    minshaft=3, 
                    zorder=2.5)
        plt.plot(*ORIGIN, '.k', zorder=3)
        plt.show()