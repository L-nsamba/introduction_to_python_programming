class Laptops:

    #HardDisk = None
    #Architecture = None
    #Model = None

    def __init__(self, HardDisk, Architecture,Model):
        self.HardDisk = HardDisk
        self.Architecture = Architecture
        self.Model = Model

    def TurnOn(self):
        print("This Laptop can run by pressing the power button.")

    def bits(self):
        print("This Type might support a few software applications.")
