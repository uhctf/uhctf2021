# Solution

## Key 1

Connect usb serial, reset device, and read device output.

## Key 2

1. Enable maintenance mode by grounding pin 5.
2. Connect with wifi to the device (passwd in description).
3. Visit webpage on device IP.

## Key 3

1. Enter your wifi credentials on the maintenance page
2. Connect buzzer.
3. Listen to outputs from the buzzer when grounding the KEYPAD_PINS
4. When the correct code is entered visit the webpage on the device.

## Key 4

1. Run wireshark/tcpdump between this device (eg create hotspot, device needs internet access)
2. Check for updates in device
3. Check wireshark for http traffic

## Key 5

1. Enter all previous keys on the maintenance page.
2. Download key
3. Use key to decrypt `image.bin` (keep in mind offset starts at `0x1000`)
4. In decrypted image search for `UHCTF`