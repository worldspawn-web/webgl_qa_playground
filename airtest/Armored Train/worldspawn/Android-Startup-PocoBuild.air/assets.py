from helpers import poco

# 3D Elements
# This class contains all poco 3D variable definitions
#
# To add new one:
#   - self.name = poco(...)
#
# To use in main code:
#   - from assets import Assets3D
#   - assets = Assets3D()
#   - assets.name

class Assets3D:
    def __init__(self):
        # Main Scene
        self.depot = poco(name="SM_Depot")
        self.depot_light = poco(name="SM_DepotLight")
        self.mechanism = poco(name="SM_Mechanism")
        self.depot_door_l = poco(name="SM_Door_left")
        self.depot_door_r = poco(name="SM_Door_right")
        
        # Loco & Wagons
        self.loco = poco(name="SM_ArmoredTrain_01")
        self.wagon_tank = poco(name="SM_Wagon_TankGun_01")
        # ...there will be more later