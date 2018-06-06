def divide_land(length, width):
    if length > width:
        return divide_land(length - width, width)
    elif length < width:
        return divide_land(length, width - length)
    else:
        return length

print divide_land(1680, 640)
