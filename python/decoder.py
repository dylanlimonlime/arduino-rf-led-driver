import constants

def normalize_alpha(rotary_position, min_position, max_position):
  # normalize range so it starts at 0
  new_max_position = max_position + -(min_position)
  new_min_position = 0

  return round(rotary_position / new_max_position, 2)

def set_alpha_bytes(alpha_value) # [0, 1.0]
  # set normalize on a scale of 100
  
  return '%02X' % alpha_int

def convert_rgb_to_hex_bytes(rgb_tuple):
  return '%02X%02X%02X' % rgb_tuple

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
    if self.rotary_encoder.is_new_position():
      self.rotary_encoder.update_position()
      self.did_update = True

  # max single message length is 252 bytes 
  # I don't ever expect this function to exceed that but just in case, 
  # may want to add guard for string length on the color_signal
  def create_message(self):
      fx = constants.FX_MAP[self._keypad_event]
      
      signal = fx.name
      signal += constants.SIGNAL_DELIMITER

      if fx.name == 'stop':
        return signal

      rotary_encoder_position = self.rotary_encoder.last_position
      rotary_encoder_min_val  = self.rotary_encoder.MIN_POSITION
      rotary_encoder_max_val  = self.rotary_encoder.MAX_POSITION

      alpha_value = normalize_alpha(rotary_encoder_position, rotary_encoder_min_val, rotary_encoder_max_val)
      alpha_int = int(alpha_value * 100)

      signal += alpha_int
      signal += constants.SIGNAL_DELIMITER

      colors = [convert_rgb_to_hex_bytes(rgb) for rgb in fx.rgb]

      color_signal = ','.join(colors)
      signal += color_signal
      signal += SIGNAL_DELIMITER

      self.did_update = False
      return signal