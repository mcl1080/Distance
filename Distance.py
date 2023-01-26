import math


def distance_between_points(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # The radius of Earth in miles
    r = 3958.8

    # Haversine formula to calculate distance
    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    a = (
        math.sin(d_lat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = r * c

    return distance


def convert_latitude(latitude):
    if latitude >= 0:
        return 90 - latitude
    else:
        return abs(latitude) + 90


def distance_between_polar_points(r1, theta1, r2, theta2):
    # Convert latitude
    r1 = convert_latitude(r1)
    r2 = convert_latitude(r2)

    # Convert latitude degrees to miles
    r1 = r1 * 69.09409442795118
    r2 = r2 * 69.09409442795118

    # Convert polar coordinates to cartesian coordinates
    x1 = r1 * math.cos(math.radians(theta1))
    y1 = r1 * math.sin(math.radians(theta1))
    x2 = r2 * math.cos(math.radians(theta2))
    y2 = r2 * math.sin(math.radians(theta2))

    # Distance formula to calculate distance
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    return distance


print("Input Decimal Coordinates in this format 37.233, -115.812. Decimal Degrees separated by comma space.")
while True:
    lat_1, lon_1 = list(map(float, input("Coordinates 1: ").split(", ")))
    lat_2, lon_2 = list(map(float, input("Coordinates 2: ").split(", ")))

    g_dist = round(distance_between_points(lat_1, lon_1, lat_2, lon_2), 3)
    print(f"Globe: {g_dist} Miles")
    f_dist = round(distance_between_polar_points(lat_1, lon_1, lat_2, lon_2), 3)
    print(f"Flat: {f_dist} Miles")
    dif = round(f_dist - g_dist, 3)
    print(f"Difference: {dif} Miles")
    print(f"-------------------------------")
