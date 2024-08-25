class Encoder:
  MIN_POSITION = -24
  MAX_POSITION = 24

  def __init__(self, rotary_encoder):
    self.rotary_encoder = rotary_encoder
    self.last_position = rotary_encoder.position
  
  def is_new_position(self):
    return self.rotary_encoder.position != self.last_position
  
  def update_position(self):
    self.last_position = self.rotary_encoder.position

  @property
  def last_position(self):
    return self._last_position