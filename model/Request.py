class Request:
    """
    1. Hall Call : Floor + Direction (encoded as RequestType.PICKUP_UP / PICKUP_DOWN)
    2. Elevator Call : Floor (encoded as RequestType.DESTINATION)
    """

    # - floor : int
    # - request_type : RequestType

    # + Request()
    # + get_floot() : int # Floor
    # + get_direction() : Direction

    def __init__(self, floor, request_type):
        self.floor = floor
        self.request_type = request_type

    def get_floor(self):
        return self.floor
    
    def get_request_type(self):
        return self.request_type