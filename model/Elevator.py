from model.Direction import Direction

class Elevator:
    # - floor : int
    # - direction : Direction

    # + Elevator()
    # + get_direciton : Direction
    # + get_floor() : int # Floor
    # + add_requests(request) : bool
    # + step() : void

    def __init__(self):
        self.floor = 0
        self.direction = Direction.IDLE
        self.requests = []

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def get_floor(self):
        return self.floor

    def set_floor(self, floor):
        self.floor = floor

    def add_requests(self, request):
        self.requests.append(request)
        return True
    
    def __drop_requests_for_current_floor(self):
        self.requests = [
            request for request in self.requests if request.get_floor() != self.floor
        ]

    def __set_to_idle_if_no_request(self):
        if len(self.requests) == 0:
            self.direction = Direction.IDLE
            return True
        return False
        
    def __find_nearest_request(self):
        nearest = None
        min_dis = float("inf")

        for request in self.requests:
            dis = abs(request.get_floor() - self.floor)
            if dis < min_dis:
                min_dis = dis
                nearest = request
        return nearest
    
    def __has_request_in_current_direction(self):
        if self.direction == Direction.UP:
            return any(request.get_floor() > self.floor for request in self.requests)
        if self.direction == Direction.DOWN:
            return any(request.get_floor() < self.floor for request in self.requests)
        return False

    def step(self):
        """
        Core Logic:
        1. If IDLE and queue is non-empty, pick the nearest request and set direction.
        2. Stop at the current floor if there is any matching request.
        3. If no pending requests in current direction, reverse.

        Edge Cases:
        1. If no requests, stay IDLE.
        """
        if self.__set_to_idle_if_no_request():
            return
        
        
        # Serve current floor first (if a request exists here).
        self.__drop_requests_for_current_floor()
        if self.__set_to_idle_if_no_request():
            return

        if self.direction == Direction.IDLE:
            nearest_request = self.__find_nearest_request()
            if nearest_request.get_floor() > self.floor:
                self.direction = Direction.UP
            else:
                self.direction = Direction.DOWN
        
        if self.direction == Direction.UP:
            self.floor += 1
        
        
        if self.direction == Direction.DOWN:
            self.floor -= 1

        self.__drop_requests_for_current_floor()
        if self.__set_to_idle_if_no_request():
            return

        if not self.__has_request_in_current_direction():
            self.direction = (
                Direction.DOWN if self.direction == Direction.UP else Direction.UP
            )
