from Kuznechic import gamma_mode_encrypt, gamma_mode_decrypt, to_pack_data
from generating_round_keys import encrypt, decrypt, hex_to_int, int_to_hex,gen_round_keys

print('Введи ключ шифрования без пробелов в шестнадцатиричном формате (256 бит)')
master_key = input()
round_keys = gen_round_keys(master_key)
print(master_key)
print('Итерационные ключи:', round_keys)

print('Если хочешь зашифровать введи 1, если расшифровать введи 0')
crypt_flag = int(input())
if crypt_flag == 1:
    print('Введи 1 если хочешь зашифровать пакет данных в режиме гаммирования,'
          ' введи 0 если хочешь зашифровать один блок данных (128 бит)')
    mode_flag = int(input())
    if mode_flag == 1:
        print('введи синхропосылку - IV')
        IV = input()
        IV = IV + '0' * 16
        print('введи пакет данных в шестнадцатиричном формате без пробелов')
        open_data = input()
        open_data = to_pack_data(open_data)
        print(open_data)
        chip = gamma_mode_encrypt(open_data, round_keys, IV)
        print('Шифр: ', chip)
    else:
        print('Введи блок данных 128 бит')
        data = input()
        chip = encrypt(data, round_keys)
        print('Шифр: ', int_to_hex(chip))
else:
    print('Введи 1 если хочешь расшифровать пакет данных в режиме гаммирования,'
          ' введи 0 если хочешь расшифровать один блок данных (128 бит)')
    mode_flag = int(input())
    if mode_flag == 1:
        print('введи синхропосылку - IV')
        IV = input()
        print('введи пакет данных в шестнадцатиричном формате без пробелов')
        IV = IV + '0' * 16
        chip_data = input()
        chip_data = to_pack_data(chip_data)
        chip = gamma_mode_decrypt(chip_data, round_keys, IV)
        print('Сообщение: ', chip)
    else:
        print('Введи блок зашифрованных данных 128 бит')
        chip = input()
        data = decrypt(chip, round_keys)
        print('Данные: ', int_to_hex(data))



# Тестовый ключ шифрования: 8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef
# Тестовый блок данных из Гост 34.12-2015: 1122334455667700ffeeddccbbaa9988
# Тестовый пакет данных из Гост 34.13-2015 (Режим гаммирования): 1122334455667700ffeeddccbbaa998800112233445566778899aabbcceeff0a112233445566778899aabbcceeff0a002233445566778899aabbcceeff0a0011
# Тестовая синхропосылка: 1234567890abcef0
# Результат операций найдете в соответствующих ГОСТах

# f195d8bec10ed1dbd57b5fa240bda1b885eee733f6a13e5df33ce4b33c45dee4a5eae88be6356ed3d5e877f13564a3a5cb91fab1f20cbab6d1c6d15820bdba73