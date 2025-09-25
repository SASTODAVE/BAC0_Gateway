from bacpypes.object import AnalogValueObject, BinaryValueObject, MultiStateValueObject

def create_object(object_type):
    """
    Creates an object from an object type.
    :param object_type: type of the object
    :return: bacnet object
    """
    if object_type == "analog":
        return AnalogValueObject(
            objectIdentifier=("analogValue", 1),
            objectName="NoName",
            presentValue=0.0,
            statusFlags=[0, 0, 0, 0],
            units="noUnits",
        )
    elif object_type == "binary":
        return BinaryValueObject(
            objectIdentifier=("binaryValue", 1),
            objectName="NoName",
            presentValue="inactive",
            statusFlags=[0, 0, 0, 0],
        )
    elif object_type == "multistate":
        return MultiStateValueObject(
            objectIdentifier=("multiStateValue", 1),
            objectName="NoName",
            presentValue=0,
            numberOfStates=3
        )

    else:
        raise ValueError(f"Unknown type : {object_type}")

def create_objects_from_json(json_data):
    """
    Creates objects from JSON data.
    :param json_data:
    :return: list of bacnet objects
    """
    objects = []
    meter = json_data.get("meter_reading")
    if not meter:
        return []
    usage_point = meter.get("usage_point_id", "unknown")
    reading_type = meter.get("reading_type", {})
    measurement_kind = reading_type.get("measurement_kind", "analog")
    unit = reading_type.get("unit", "unitless")

    object_name = f"{measurement_kind.capitalize()}_{usage_point}"

    interval_reading = meter.get("interval_reading", [])
    initial_value = 0.0
    if interval_reading:
        initial_value = float(interval_reading[0].get("value", 0))

    obj = AnalogValueObject(
        objectIdentifier=("analogValue", 1),
        objectName=object_name,
        presentValue=initial_value,
        statusFlags=[0, 0, 0, 0],
        units=unit,
        covIncrement=1.0,
    )

    objects.append(obj)

    return objects