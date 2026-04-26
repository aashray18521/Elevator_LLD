# class ElevatorController():
#     - elevator : List<Elevator>
#     + ElevatorController()
#     + request_elevator(floor, direction) -> bool
#     + step() -> void (simulation of elevator(s) movement)

from model.Request import Request
from model.RequestType import RequestType
from model.Direction import Direction

class ElevatorController:
    def __init__(self, number_of_floors=5):
        self.elevator_list = []
        self.number_of_floors = number_of_floors

    def add_elevator(self, elevator):
        self.elevator_list.append(elevator)

    def step(self):
        for elevator in self.elevator_list:
            elevator.step()

    def request_elevator(self, floor, request_type):
        """
        Core Logic:
        1. Find the best elevator to handle the request
        2. Send that request to the selected elevator:

        Edge Cases:
        1. Floor Out of Bounds
        """
        if floor < 0 or floor >= self.number_of_floors:
            raise ValueError("Not a valid floor")
        
        if request_type == RequestType.DESTINATION:
            raise ValueError("Not a valid request type")
        
        request = Request(floor, request_type)
        best_elevator = self.__select_best_elevator(request)
        if best_elevator is None:
            return False
        return best_elevator.add_requests(request)
    
    # Helper for inside-elevator destination requests.
    def request_destination(self, elevator, floor):
        if floor < 0 or floor >= self.number_of_floors:
            raise ValueError("Not a valid floor")
        if elevator.get_floor() == floor:
            raise ValueError("Already at destination floor")
        request = Request(floor, RequestType.DESTINATION)
        return elevator.add_requests(request)
    
    def __select_best_elevator(self, request):
        best = self.__best_moving_toward_me(request)
        if best is not None:
            return best
        return self.__select_nearest_to_me(request.get_floor())
    
    def __best_moving_toward_me(self, request):
        """
        Core Logic:
        1. Scan elevators moving in the request's direction.
        2. Keep only elevators that will pass the request's floor.
        3. Pick the closest elevator.
        """

        floor = request.get_floor()
        direction = (
            Direction.UP
            if request.get_request_type() == RequestType.PICKUP_UP
            else Direction.DOWN
        )

        best = None
        min_dis = float("inf")

        for elevator in self.elevator_list:
            if elevator.get_direction() != direction:
                continue
            elevator_floor = elevator.get_floor()

            if (direction == Direction.UP) and (elevator_floor > floor):
                continue
            if (direction == Direction.DOWN) and (elevator_floor < floor):
                continue
            
            dis = abs(elevator_floor - floor)
            if dis < min_dis:
                min_dis = dis
                best = elevator

        return best
    
    def __select_nearest_to_me(self, floor):
        nearest_idle = None
        min_dis = float("inf")

        for elevator in self.elevator_list:
            if elevator.get_direction() != Direction.IDLE:
                continue

            dis = abs(elevator.get_floor() - floor)
            if dis < min_dis:
                min_dis = dis
                nearest_idle = elevator
        
        if nearest_idle is not None:
            return nearest_idle
        
        ## There could be scenario(s) where None is IDLE and 
        ## None are moving towards the call
        nearest_any = None
        min_dis = float("inf")
        for elevator in self.elevator_list:
            dis = abs(elevator.get_floor() - floor)
            if dis < min_dis:
                min_dis = dis
                nearest_any = elevator
        return nearest_any
