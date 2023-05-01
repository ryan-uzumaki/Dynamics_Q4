import scipy as sci

class Task:
    s = 0
    v_lim = 0

    def __init__(self):
        self.s = 5144.7
        self.v_lim = 100/3.6


class Train:
    state = ""
    v = 0
    M = 0
    F_tra = 0
    F_bra = 0
    rou = 0.0
    D = 0
    px = 0
    kax = 0
    kbx = 0
    F = 0
    a = 0
    Gx = 0

    def __init__(self, sta, vel):
        self.state = sta
        self.F_tra = 289000
        self.F_bra = 760000
        self.v = vel
        self.M = 287000
        self.rou = 1.08
        self.D = 1000*(3.48+0.14*self.v+0.01*self.v**2)

        if self.state == "traction":
            self.px = 1
            self.kax = 1
            self.kbx = 0
            self.F = self.kax*self.F_tra + self.kbx*self.F_bra
            self.a = (self.px*self.F-self.D-self.Gx)/self.rou*self.M

        elif self.state == "braking":
            self.px = 1
            self.kax = 0
            self.kbx = 1
            self.F = self.kax*self.F_tra + self.kbx*self.F_bra
            self.a = (self.px*self.F-self.D-self.Gx)/self.rou*self.M

        elif self.state == "cruising":
            self.kax = 1
            self.kbx = 0
            self.F = self.kax*self.F_tra + self.kbx*self.F_bra
            self.px = self.D/self.F
            self.a = (self.px*self.F-self.D-self.Gx)/self.rou*self.M

        elif self.state == "taxi":
            self.px = 0
            self.kax = 0
            self.kbx = 0
            self.F = self.kax * self.F_tra + self.kbx * self.F_bra
            self.a = 0





def traction():
    pass

def cruising():
    pass

def taxi():
    pass

def braking():
    pass


train_traction = Train("traction", 10)
print(train_traction.D)



