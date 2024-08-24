import adafruit_rfm9x
import busio
import board
import constants
import rotaryio
import time

class RadioSender:
  def __init__(self, animation_decoder, transreceiver):
    self.animation_decoder = animation_decoder
    # API doc: https://docs.circuitpython.org/projects/rfm9x/en/latest/api.html#adafruit_rfm9x.RFM9x
    self.transreceiver  = transreceiver

  def transmit_signal_callback(self, event, keypad_callback):
    self.animation_decoder.query_rotary_position()
    if keypad_callback(event) != constants.OFF or self.animation_decoder.did_update:
      keypad_index = event.number
      if keypad_index != self.animation_decoder.current_keypad_event:
        self.animation_decoder.set_keypad_event(keypad_index)

      self.transreceiver.send_with_ack(self.animation_decoder.create_message())
    
  def run_loop(self):
    self.keypad.initialize_key_handlers(self.transmit_signal_callback)
    self.transreceiver.ack_retries = 10
    while True:
      self.keypad.trellis.sync()
    
      time.sleep(constants.PENDING_COMMAND_CYCLE_DELAY_SECONDS)



