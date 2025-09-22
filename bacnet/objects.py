from bacpypes.object import AnalogValueObject, BinaryValueObject, MultiStateValueObject

def create_object(object_type):
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