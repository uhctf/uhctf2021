import wave


def wave_to_binary_decode(filename):
    bits = []
    frame_size = 2
    sine_treshold = 600000000
    with wave.open(filename, 'rb') as wave_fp:
        reset_hit = False
        max_sine_value = 0
        for _ in range(0, wave_fp.getnframes(), frame_size):
            frame_value = int.from_bytes(wave_fp.readframes(frame_size), "little", signed=True)

            if frame_value == 0:
                #  We hit a pause block; i.e., we know we saw all sine wave sample data
                if not reset_hit:
                    bits.append(1 if max_sine_value >= sine_treshold else 0)
                    max_sine_value = 0
                    reset_hit = True
                    print('\r{} bits found'.format(str(len(bits))), end='')
            else:
                max_sine_value = max(max_sine_value, frame_value)
                reset_hit = False
    return bits


def wave_to_max_sine_values(filename, samples_needed):
    max_values = []
    frame_size = 2
    with wave.open(filename, 'rb') as wave_fp:
        reset_hit = False
        max_sine_value = 0
        for _ in range(0, wave_fp.getnframes(), frame_size):
            frame_value = int.from_bytes(wave_fp.readframes(frame_size), "little", signed=True)

            if frame_value == 0:
                #  We hit a pause block; i.e., we know we saw all sine wave sample data
                if not reset_hit:
                    max_values.append(max_sine_value)
                    max_sine_value = 0
                    reset_hit = True
                    print('\r{} max values found'.format(str(len(max_values))), end='')
                    if len(max_values) >= samples_needed:
                        return max_values
            else:
                max_sine_value = max(max_sine_value, frame_value)
                reset_hit = False
    return max_values


if __name__ == '__main__':
    input_filename = 'message_from_outer_space.wav'
    parsed_output_file = 'parsed_bits.txt'
    dry_max_value_run = False
    samples_needed = 100

    if dry_max_value_run:
        print(wave_to_max_sine_values(input_filename, samples_needed))
    else:
        bits = wave_to_binary_decode(input_filename)

        with open(parsed_output_file, 'w') as fp:
            for bit in bits:
                fp.write(str(bit) + '\n')
