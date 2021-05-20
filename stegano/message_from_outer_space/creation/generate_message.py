# Source of inspiration: https://www.daniweb.com/programming/software-development/code/263775/create-a-synthetic-sine-wave-wave-file

import wave
import math
import struct


def _generate_silence(audio_bytes, samples):
    silence_byte = struct.pack('h', 0)
    for _ in range(samples):
        audio_bytes.append(silence_byte)


def _generate_beep(audio_bytes, sample_rate, samples, high_bit):
    sine_frequency = 1760
    for i in range(samples):
        amplitude_modifier = 1 if high_bit else 0.25
        sine_value = amplitude_modifier * math.sin(2 * math.pi * sine_frequency * (i / sample_rate))  # Sine wave sample
        sine_value = int(sine_value * 32767)  # WAVE files represent samples in 16 bits
        audio_bytes.append(struct.pack('h', sine_value))


def generate_sinewave_from_binary(bits, sample_rate):
    """We will generate an audible version of a binary signal
    The signal consists of a beep (i.e., a 1 or 0 depending on the bit) followed by a pause
    The pause itself will be a zeroed sine wave, i.e., a silence

    The beep itself is represented as a higher (1) or lower (0) amplitude.

    Every beep and silence part will be of a 500ms duration.
    Total playback output = amount of bits * 2 * 500ms == amount of bits * 1sec

    :return:
    """
    signal_element_duration = 500 # milliseconds
    samples_per_element = int(signal_element_duration * (sample_rate / 1000))
    audio_bytes = []

    total_bits = len(bits)
    counter = 0
    for b in bits:
        _generate_beep(audio_bytes, sample_rate, samples_per_element, (b == 1))
        _generate_silence(audio_bytes, samples_per_element)
        counter += 1
        print('\rAt bit {}/{}'.format(str(counter), str(total_bits)), end='')

    # Speedup Python wave https://soledadpenades.com/posts/2009/fastest-way-to-generate-wav-files-in-python-using-the-wave-module/
    audio_str = b''.join(audio_bytes)
    return audio_str


def save_audio_string(filename, sample_rate, audio_string):
    channel_count = 1  # We do mono for this challenge

    with wave.open(filename, 'wb') as wave_fp:
        wave_fp.setparams((1, 2, sample_rate, 0, 'NONE', 'not compressed'))
        wave_fp.writeframes(audio_string)


def get_bits_from_file(filename):
    bits = []
    with open(filename, 'r') as fp:
        for line in fp:
            line = line.strip()
            if line != '':
                bits.append(int(line))
    return bits


if __name__ == '__main__':
    input_filename = 'input.txt'
    # input_filename = 'input_tester.txt'
    output_filename = 'message_from_outer_space.wav'
    sample_rate = 44100  # in hertz
    save_audio_string(output_filename, sample_rate, generate_sinewave_from_binary(get_bits_from_file(input_filename), sample_rate))
