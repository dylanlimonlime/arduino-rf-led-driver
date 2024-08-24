import constants
def normalize_alpha(rotary_position):
  # bounds (-inf, inf)? normalize range into [0, 1] for RGBA

  #TODO
  return 1

def set_alpha_bytes(alpha_value) # [0, 1.0]
  # set normalize on a scale of 100
  
  return '%02x' % alpha_int

def convert_rgb_to_hex_bytes(rgb_tuple):
  return '%02x%02x%02x' % rgb_tuple

class AnimationDecoder:

  def __init__(self, keypad, rotary_encoder):
    # API doc: https://docs.circuitpython.org/projects/neotrellis/en/latest/api.html#adafruit_neotrellis.neotrellis.NeoTrellis
    self.keypad         = keypad
    # API doc: https://docs.circuitpython.org/en/latest/shared-bindings/rotaryio/index.html
    self.rotary_encoder = rotary_encoder
    
    self.keypad_event = -1 # 0 - 16

    self.did_update = False
  
  @property
  def rotary_encoder(self):
    return self._rotary_encoder

  @property
  def keypad_event(self):
    return self._keypad_event

  @property
  def did_update(self):
    return self._did_update

  @keypad_event.setter
  def keypad_event(self, value):
    self.keypad_event = value

  def query_rotary_position(self):
    # TODO: check rotary_encoder

    self.did_update = True

  
  def create_message(self):
      fx = constants.FX_MAP[self._keypad_event]
      
      signal = fx.name
      signal += ';'
      

      # TODO: finish signal formatting
      # alpha + rgb iteration

      alpha_value = normalize_alpha(self.rotary_encoder.last_position)
      alpha_int = int(alpha_value * 100)




      self.did_update = False
      return signal