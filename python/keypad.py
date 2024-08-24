import time
from adafruit_neotrellis.neotrellis import NeoTrellis

NUM_KEY_PADS = 16

# Color constants
OFF     = (0, 0, 0)
RED     = (255, 0, 0)
YELLOW  = (255, 150, 0)
GREEN   = (0, 255, 0)
CYAN    = (0, 255, 255)
BLUE    = (0, 0, 255)
PURPLE  = (180, 0, 255)


INIT_DELAY_SECONDS = 0.05  # 50 ms

class Keypad:
  def __init__(self, board, neo_trellis_addr):
    self.board = board

    i2c_bus = self.board.I2C()
    # API doc: https://docs.circuitpython.org/projects/neotrellis/en/latest/api.html#adafruit_neotrellis.neotrellis.NeoTrellis
    self.trellis = NeoTrellis(i2c_bus, neo_trellis_addr)

  def blink(self, event):
    if event.edge == NeoTrellis.EDGE_RISING:
      self.trellis.pixels[event.number] = CYAN
    elif event.edge == NeoTrellis.EDGE_FALLING:
      self.trellis.pixels[event.number] = OFF

  def initialize_key_handlers(self):
    for i in range(NUM_KEY_PADS):
      self.trellis.activate_key(i, NeoTrellis.EDGE_RISING)
      self.trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
      self.trellis.callbacks[i] = self.blink

      self.trellis.pixels[i] = PURPLE
      time.sleep(INIT_DELAY_SECONDS)

    for i in range(NUM_KEY_PADS):
      self.trellis.pixels[i] = OFF
      time.sleep(INIT_DELAY_SECONDS)
    
