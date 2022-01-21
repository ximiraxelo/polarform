def adjust_angle(angle):
    new_angle = angle
    while new_angle > 180:
        new_angle -= 360
    while new_angle < -180:
        new_angle += 360
    return new_angle
