import math

def quadraticEq(a: float, b: float, c: float):
    delta = (b * b) - (4 * a * c)
    if delta < 0:
        return "Nie ma rzeczywistych rozwiazan"
    elif delta == 0:
        x1 = (-b) / (2 * a)
        return f"Jest jedno rozwiazanie: x = {round(x1,2)}"
    else:
        sqrtDelta = math.sqrt(delta)
        x1 = (-b + sqrtDelta) / (2 * a)
        x2 = (-b - sqrtDelta) / (2 * a)
        return f"Są dwa rozwiązania: x1 = {round(x1,2)}, x2 = {round(x2,2)}"
