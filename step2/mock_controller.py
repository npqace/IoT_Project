class MockModbusMaster:
    def __init__(self):
        print("MockModbusMaster initialized")

    def switch_actuator_1(self, state):
        print(f"Mock: Actuator 1 switched to {'ON' if state else 'OFF'}")

    def switch_actuator_2(self, state):
        print(f"Mock: Actuator 2 switched to {'ON' if state else 'OFF'}")

    def switch_actuator_3(self, state):
        print(f"Mock: Actuator 3 switched to {'ON' if state else 'OFF'}")
