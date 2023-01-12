import random


def generate_key():
    n = 16
    valid_chars = "0123456789abcdefghijklmnopqrstuvwxyzабвггдеёжзийклмнопрстуфхцчшщъыьэюя!@#№$%&?*-" \
                  "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    master_key = ''
    master_key_list = random.sample(valid_chars, n)

    for i in range(len(master_key_list)):
        master_key = master_key + master_key_list[i]

    return master_key




