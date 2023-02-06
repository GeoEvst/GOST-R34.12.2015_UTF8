from TEXT_to_HEX import hex_to_text, text_to_hex
from generating_round_keys import encrypt, decrypt, gen_round_keys, int_to_hex, hex_to_int, block_to_xor
from private_key_generator import gen_gamma, generate_random_key
import textwrap


def to_pack_data(text):
    chip_box = textwrap.wrap(text, 32)
    i = len(chip_box)
    if len(chip_box[i - 1]) < 32:
        x = 32 - len(chip_box[i - 1])
        last_chip = chip_box[i - 1]
        last_chip = last_chip + '0' * x
        chip_box[i - 1] = last_chip
    return chip_box


def gamma_mode_encrypt(data, round_keys, gamma):
    chip_data_block = ''
    for i in range(len(data)):
        gamma = gamma[:len(gamma) - len(str(i))]
        gamma = gamma + str(i)
        chip_gamma = encrypt(gamma, round_keys)
        data_n = hex_to_int(data[i])
        chip_data = block_to_xor(chip_gamma, data_n)
        chip_data = int_to_hex(chip_data)
        chip_data_block += chip_data
    return chip_data_block


def gamma_mode_decrypt(chip, round_keys, gamma):
    open_text = ''
    for i in range(len(chip)):
        gamma = gamma[:len(gamma) - len(str(i))]
        gamma = gamma + str(i)
        chip_gamma = encrypt(gamma, round_keys)
        data_n = hex_to_int(chip[i])
        message = block_to_xor(data_n, chip_gamma)
        open_text += int_to_hex(message)
    return open_text


# master_key = '8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef'
# open_data = ['1122334455667700ffeeddccbbaa9988', '00112233445566778899aabbcceeff0a', '112233445566778899aabbcceeff0a00', '2233445566778899aabbcceeff0a0011']
# # chip = to_pack_data('f195d8bec10ed1dbd57b5fa240bda1b885eee733f6a13e5df33ce4b33c45dee4a5eae88be6356ed3d5e877f13564a3a5cb91fab1f20cbab6d1c6d15820bdba73')
# IV = '1234567890abcef0'
# IV = IV + '0' * 16
# chip = gamma_mode_encrypt(open_data, master_key, IV)
# print(chip)
# x = to_pack_data(chip)
# open_d = gamma_mode_decrypt(x, master_key, IV)
# print(open_d)

# Аналог встроенной функции wrap
# def to_wrap(text):
#     cnt = 0
#     chip_box = []
#     chip = ''
#     x = 0
#     for i in range(len(text)):
#         cnt += 1
#         m = cnt % 32
#         chip += text[i]
#         if cnt == 32:
#             chip_box.append(chip[0:cnt])
#             x = cnt
#             chip = ''
#         elif m == 0 and cnt > 32:
#             chip_box.append(text[x:cnt])
#             x = cnt
#             chip = ''
#         elif m != 0 and cnt == len(text):
#             chip_box.append(text[x:])
#     return chip_box


