import constants
import time
from adafruit_neotrellis.neotrellis import NeoTrellis

NUM_KEY_PADS = 16

INIT_DELAY_SECONDS = 0.05  # 50 ms

class Keypad:
  def __init__(self, board, neo_trellis_addr):
    self.board = board

    i2c_bus = self.board.I2C()
    # API doc: https://docs.circuitpython.org/projects/neotrellis/en/latest/api.html#adafruit_neotrellis.neotrellis.NeoTrellis
    self.trellis = NeoTrellis(i2c_bus, neo_trellis_addr)

  def keypad_callback(self, event):
    if event.edge == NeoTrellis.EDGE_FALLING:
      self.trellis.pixels[event.number] = constants.OFF
    elif if event.edge == NeoTrellis.EDGE_RISING:
      self.trellis.pixels[event.number] = constants.GREEN

    return self.trellis.pixels[event.number]
      

  def initialize_key_handlers(self, transmit_signal_callback):
    for i in range(NUM_KEY_PADS):
      self.trellis.activate_key(i, NeoTrellis.EDGE_RISING)
      self.trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
      self.trellis.callbacks[i] = lambda event: transmit_signal_callback(event, self.keypad_callback)

      self.trellis.pixels[i] = constants.PURPLE
      time.sleep(INIT_DELAY_SECONDS)

    for i in range(NUM_KEY_PADS):
      self.trellis.pixels[i] = constants.OFF
      time.sleep(INIT_DELAY_SECONDS)
    
