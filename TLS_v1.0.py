import time as t, os

class road:
    def __init__(self):
        pass
    
    def lights(self):
        def green():
            for i in range(10):
                clear()
                print(f" Green light! GO GO GO!!!                               ({10-i})\n")
                t.sleep(1/2)
        def yellow():
            clear()
            print(" Yellow light... Prep To STOP\n")
            t.sleep(2)
        def red():
            for i in range(10):
                clear()
                print(f" Red light! STOP STOP STOP!                            ({10-i})")
                t.sleep(1/2)
        return {"red":red, "yellow":yellow, "green":green}
        
road = road()     
traffic = road.lights()

def run():
    while 1:
        traffic["green"]()
        traffic["yellow"]()
        traffic["red"]()

run()
