class Tool:
    def __init__(self):
        self.strength = 100

    def action(self):
        self.strength -= 10


class Saw(Tool):
    def action(self):
        if self.strength > 0:
            print("ZZZZZZ")
            super().action()


class Axe(Tool):
    def action(self):
        if self.strength > 0:
            print("BABAH")
            super().action()


class Drill(Tool):
    def action(self):
        if self.strength > 0:
            print("DRRRRR")
            super().action()


class Hammer(Tool):
    def action(self):
        if self.strength > 0:
            print("TUKTUKTUK")
            super().action()


class Screwdriver(Tool):
    def action(self):
        if self.strength > 0:
            print("ZHHHHHHH")
            super().action()


class Robot:
    def __init__(self, tool=None):
        self.tool = tool
        self.has_tool = False

    def setup_tool(self, tool):
        if self.has_tool:
            print("Tool is already equiped")
        else:
            self.has_tool = True
            self.tool = tool

    def drop_tool(self):
        if self.has_tool:
            self.has_tool = False
            self.tool = None
        else:
            print("Nothing to drop!")

    def action(self):
        if not self.has_tool:
            print("I don't have a tool")
        else:
            if self.tool.strength > 0:
                self.tool.action()
            else:
                print("Instrument is broken")
                self.tool = None
                self.has_tool = False


axe = Axe()
saw = Saw()
drill = Drill()
hammer = Hammer()
screwdriver = Screwdriver()
robot = Robot()
robot.setup_tool(axe)
for i in range(15):
    robot.action()
