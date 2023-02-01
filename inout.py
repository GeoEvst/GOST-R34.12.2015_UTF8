from TEXT_to_HEX import hex_to_text, text_to_hex
import textwrap


print('Введи ключ 16 символов')

def to_pack_data():
    text = text_to_hex(input())
    chip_box = textwrap.wrap(text, 32)
    i = len(chip_box)
    if len(chip_box[i - 1]) < 32:
        x = 32 - len(chip_box[i - 1])
        last_chip = chip_box[i - 1]
        last_chip = last_chip + '0' * x
        chip_box[i - 1] = last_chip
    return chip_box


print(to_pack_data())
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

