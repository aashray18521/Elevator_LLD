"""
We do not re-use the "Direction" enum here because the hall calls
are never "IDLE."
Accepting "Direction" would let invalid values creep in, which would 
require additional validation to catch them.

Using "RequestType" makes them impossible at the type level itself.
"""

from enum import Enum

class RequestType(Enum):
    PICKUP_UP = 1
    PICKUP_DOWN = 2
    DESTINATION = 3