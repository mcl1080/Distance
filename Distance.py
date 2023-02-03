from math import sqrt, cos, sin, radians, atan2


def distance_between_points(lat1, lon1, lat2, lon2):
    """This function takes the lat and lon in decimal format and calculates the distance between them on a sphere"""

    # Convert latitude and longitude to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # The radius of Earth in miles
    r = 3956.0883381231684613995179014794

    # Haversine formula to calculate distance
    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    a = (
            sin(d_lat / 2) ** 2
            + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = r * c

    return distance


def convert_latitude(latitude):
    """This function converts latitude to the number of degrees from the North Pole"""
    if latitude >= 0:
        return 90 - latitude
    else:
        return abs(latitude) + 90


def distance_between_polar_points(r1, theta1, r2, theta2):
    """ This Function takes the lat and lon, converts the lat to a distance from the North Pole, and the lon as the
    angle. Then uses those distances and angles as polar coordinates which are converted to cartesian coordinates and
    the distance is calculated using the pythagorean theorem."""
    # Convert latitude to miles
    r1 = convert_latitude(r1) * 69.046767
    r2 = convert_latitude(r2) * 69.046767

    # Convert polar coordinates to cartesian coordinates
    x1 = r1 * cos(radians(theta1))
    y1 = r1 * sin(radians(theta1))
    x2 = r2 * cos(radians(theta2))
    y2 = r2 * sin(radians(theta2))

    # Distance formula to calculate distance
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    return distance


def parse_coordinate(coordinate):
    # split the input string into direction and values
    parts = coordinate.upper().split()
    if parts[0] in ["N", "S", "W", "E"]:
        direction = parts[0]
        values = parts[1:]
    else:
        direction = "none"
        values = parts
    # determine the format of the values
    if len(values) == 3:
        # degrees-minutes-seconds format
        minutes = int(values[-2])
        seconds = float(values[-1])
        decimal_minutes = minutes / 60 + seconds / 3600
        decimal_degrees = abs(int(values[0])) + decimal_minutes
    elif len(values) == 2:
        # degrees-decimal minutes format
        minutes = float(values[-1])
        decimal_minutes = minutes / 60
        decimal_degrees = abs(int(values[0])) + decimal_minutes
    else:
        # decimal degrees format
        decimal_degrees = float(values[0])

    # determine the sign based on the direction or negative values
    sign = 1
    if direction in ["S", "W"] or values[0][0] == "-":
        sign = -1

    # return the decimal degrees with the correct sign
    return sign * decimal_degrees


print("Input Coordinates in any of these formats DMS, DDM, or DD. You can use N,E,S,W or negative signs.")
print("Separate each part with a space, and separate Lat and Lon with comma space.")
while True:
    lat_1, lon_1 = list(input("Coordinates 1: ").split(", "))
    lat_2, lon_2 = list(input("Coordinates 2: ").split(", "))

    lat_1 = parse_coordinate(lat_1)
    lon_1 = parse_coordinate(lon_1)
    lat_2 = parse_coordinate(lat_2)
    lon_2 = parse_coordinate(lon_2)

    g_dist = distance_between_points(lat_1, lon_1, lat_2, lon_2)
    print(f"Globe: {round(g_dist, 3):,} Miles")
    f_dist = distance_between_polar_points(lat_1, lon_1, lat_2, lon_2)
    print(f"Flat: {round(f_dist, 3):,} Miles")
    dif = f_dist - g_dist
    print(f"Difference: {round(dif, 3):,} Miles")
    print(f"-------------------------------")
