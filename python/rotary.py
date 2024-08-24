class Encoder:
  def __init__(self, rotary_encoder):
    self.rotary_encoder = rotary_encoder
    self.last_position = rotary_encoder.position
  
  ## TODO: helpers for: update last position, check if last position changed