def fall_distance(time):
    """
    Calculates the distance travelled by an object in free fall.
    Parameters:
        time: the time (in seconds) for which the object has fallen.
    Returns:
        the distance (in meters) travelled by the object.
    """
    # Calculate the distance travelled by the object.
    distance = (1/2)*9.8*time**2
    # Return the distance.
    return distance