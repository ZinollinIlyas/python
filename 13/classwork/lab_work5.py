coordinates = {
    'border_x': 12,
    'border_y': 6,
    'house_x': 12,
    'house_y': -40
}

if (coordinates['house_x'] == coordinates['border_x'] and coordinates['house_y'] == coordinates['border_y']) or \
        (coordinates['house_x'] <= coordinates['border_x'] and coordinates['house_y'] == coordinates['border_y']) or \
        (coordinates['house_x'] >= coordinates['border_x'] and coordinates['house_y'] == coordinates['border_y']) or \
        (coordinates['house_x'] == coordinates['border_x'] and coordinates['house_y'] >= coordinates['border_y']) or \
        (coordinates['house_x'] == coordinates['border_x'] and coordinates['house_y'] <= coordinates['border_y']):
    print("border")
elif coordinates['house_x'] < coordinates['border_x'] and coordinates['house_y'] > coordinates['border_y']:
    print("NW")
elif coordinates['house_x'] > coordinates['border_x'] and coordinates['house_y'] > coordinates['border_y']:
    print("NE")
elif coordinates['house_x'] > coordinates['border_x'] and coordinates['house_y'] < coordinates['border_y']:
    print("SE")
elif coordinates['house_x'] < coordinates['border_x'] and coordinates['house_y'] < coordinates['border_y']:
    print("SW")
