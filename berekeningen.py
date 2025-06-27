import math

def omtrek_cirkel(straal):
    if straal < 0:
        return 0
    return 2 * math.pi * straal

def oppervlakte_rechthoek(lengte, breedte):
    if lengte < 0 or breedte < 0:
        return 0
    return lengte * breedte

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

def gemiddelde(getallen):
    if not isinstance(getallen, list):
        return 0
    return sum(getallen) / len(getallen)

assert omtrek_cirkel(1) == 3,14

assert gemiddelde(getallen) == sum / len 
