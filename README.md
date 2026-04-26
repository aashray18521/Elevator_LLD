# Elevator LLD Practice

## 1. Requirements:
1. Primary Capabilities:
    a. Elevator can be called from hall => UP or DOWN
    b. Elevator can be requested to go to a floor
    c. How many elevators and floors are there?
    d. Simulation needed? ( simulate time to show elevator(s) state. )
2. Error Handling:
    a. Floor out of bounds
    b. Current floor == Destination floor
3. Out of Scope:


## 2. Entites:
Here we identify the nouns for model classes and other classes that might be needed (IFF)
1. Elevator (class)
2. Floor (int)
3. Request (class)
4. ElevatorController (class) => Orchestrator

## 3. Class Design:
Design various attributes of the class.

## 4. Implementatio:
Implement various methods needed in the classes.
1. Define Core Logic
2. Consider Edge Cases

## 5. Extensibility


## Takeaways
1. Each class makes the decision about the data that it owns.

## Run E2E Tests
From project root:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

This verifies:
1. Hall request assignment and servicing
2. Destination request servicing
3. Invalid request type handling
4. Same-floor destination error handling
5. No-elevator assignment handling
