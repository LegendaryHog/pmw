
import RPi.GPIO as G

G.cleanup()
G.setmode(G.BCM)
G.setup(6, G.OUT)

try:
    elem = G.PWM(6,1000)
    elem.start(0)

    while True:
        print("Duty cycle:")
        D = input()
        if D == 'q':
            break
        D = int(D)
        elem.start(D)

finally:
    G.output(6,0)
    G.cleanup()