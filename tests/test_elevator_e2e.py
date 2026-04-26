import unittest

from controller.ElevatorController import ElevatorController
from model.Direction import Direction
from model.Elevator import Elevator
from model.RequestType import RequestType


class ElevatorE2ETests(unittest.TestCase):
    def test_hall_request_gets_served(self):
        controller = ElevatorController(number_of_floors=10)
        e1 = Elevator()
        e2 = Elevator()
        e1.set_floor(0)
        e2.set_floor(6)
        controller.add_elevator(e1)
        controller.add_elevator(e2)

        self.assertTrue(controller.request_elevator(4, RequestType.PICKUP_UP))

        controller.step()
        controller.step()

        self.assertEqual(e2.get_floor(), 4)
        self.assertEqual(e2.get_direction(), Direction.IDLE)
        self.assertEqual(len(e2.requests), 0)

    def test_destination_request_gets_served(self):
        controller = ElevatorController(number_of_floors=10)
        elevator = Elevator()
        controller.add_elevator(elevator)

        self.assertTrue(controller.request_destination(elevator, 3))

        controller.step()
        controller.step()
        controller.step()

        self.assertEqual(elevator.get_floor(), 3)
        self.assertEqual(elevator.get_direction(), Direction.IDLE)
        self.assertEqual(len(elevator.requests), 0)

    def test_invalid_hall_request_type_raises(self):
        controller = ElevatorController(number_of_floors=10)
        controller.add_elevator(Elevator())

        with self.assertRaises(ValueError):
            controller.request_elevator(4, RequestType.DESTINATION)

    def test_same_floor_destination_raises(self):
        controller = ElevatorController(number_of_floors=10)
        elevator = Elevator()
        controller.add_elevator(elevator)

        with self.assertRaises(ValueError):
            controller.request_destination(elevator, 0)

    def test_request_fails_if_no_elevator_exists(self):
        controller = ElevatorController(number_of_floors=10)
        self.assertFalse(controller.request_elevator(2, RequestType.PICKUP_DOWN))


if __name__ == "__main__":
    unittest.main()
