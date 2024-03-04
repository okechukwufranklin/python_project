class Gun:

    def __init__(self, Bullet,pin):
        self.Bullet = Bullet
        self.pin = pin



    def is_empty(self):
        return self.Bullet == 0

    def Shoot_Gun(self,pin):
        if self.pin != pin:
            raise ValueError
        self.Bullet -= 1

    def reload_Gun(self):
        if self.Bullet > 5:
            return "Magazine full"
        self.Bullet += 5

    def Checkammo(self):
        return self.Bullet

    def Clip(self):
        if self.Bullet > 5:
            return "Magazine full"
