import adafruit_rfm9x
import busio
import board
import constants
import controller
import decoder
import keypad
import rotaryio

if __name__ == "__main__":
  keypad = keypad.Keypad(board, constants.NEO_TRELLIS_ADDR)

  # Rotary encoder constants
  encoder_divisor = 4 # modify if encoder doesn't update as expected with detents // see: https://learn.adafruit.com/rotary-encoder/circuitpython#the-rotaryio-dot-incrementalencoder-divisor-argument-3150163
  PIN_A = board.D1
  PIN_B = board.D2

  incremental_encoder = rotaryio.IncrementalEncoder(PIN_A, PIN_B, divisor=encoder_divisor)
  rotary_encoder = rotary.Encoder(incremental_encoder)
  
  # Transreceiver constants
  CS = DigitalInOut(board.CE1)
  RESET = DigitalInOut(board.D25)
  spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

  transreceiver = adafruit_rfm9x.RFM9x(spi, CS, RESET, constants.RF69_FREQUENCY)
  transreceiver.frequency_mhz = constants.RF69_FREQUENCY

  animation_decoder = decoder.AnimationDecoder(keypad, rotary_encoder)

  radioSender = controller.RadioSender(animation_decoder, transreceiver)
  radioSender.run_loop()