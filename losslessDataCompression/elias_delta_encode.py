from math import floor
from math import log

from binary_representation_without_msb import Binary_Representation_Without_MSB
from elias_gamma_encode import EliasGammaEncode

def EliasDeltaEncode(x):
    Gamma = EliasGammaEncode(1 + floor(log(x, 2)))
    binary_without_MSB = Binary_Representation_Without_MSB(x)
    return Gamma+binary_without_MSB
