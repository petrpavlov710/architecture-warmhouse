def get_location_by_sensor_id(id: str) -> str:
    match id:
        case "1":
            return "Living Room"
        case "2":
            return "Bedroom"
        case "3":
            return "Kitchen"
        case _:
            return "Unknown"


def get_sensor_id_by_location(location: str) -> int:
    match location:
        case "Living Room":
            return "1"
        case "Bedroom":
            return "2"
        case "Kitchen":
            return "3"
        case _:
            return "0"
