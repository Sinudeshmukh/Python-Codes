class Computer:
    def __init__(self, device, ram):
        self.device = device
        self.ram = ram

    def config(self):
        print('Computer Configuration is', self.device, self.ram)


comp1 = Computer('HP', '8 GB')
comp2 = Computer('Dell', '16 GB')

comp1.config()
comp2.config()
