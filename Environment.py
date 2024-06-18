# This flie contains the needed objects for:
# 1) Creating an global environment

class Env:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class path:
    def __init__(self, StartPos, GoalPos):
        self.StartPos = StartPos
        self.GoalPos = GoalPos