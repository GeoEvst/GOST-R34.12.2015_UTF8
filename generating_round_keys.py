from iterative_constants import generate_iter_consts, generate_table_galois, multiply_in_galois_field

# Ряд Галуа

galois_row = (1, 148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148)

# Таблица нелинейного преобразования Кузнечика (s-box)

s_box = (252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77,
         233, 119, 240, 219, 147, 46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193,
         249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142, 79,
         5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31,
         235, 52, 44, 81, 234, 200, 72, 171, 242, 42, 104, 162, 253, 58, 206, 204,
         181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183, 93, 135,
         21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177,
         50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87,
         223, 245, 36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3,
         224, 15, 236, 222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74,
         167, 151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100, 159, 38, 65,
         173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59,
         7, 88, 179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136, 217, 231, 137,
         225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133, 97,
         32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82,
         89, 166, 116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182)


# Преобразование из HEX в десятичное число

def hex_to_int(x):
    cnt = 2
    block = []
    for i in range(len(x)//2):
        x_1 = x[2 * i:cnt]
        cnt += 2
        x_i = int(x_1, 16)
        block.append(x_i)
    return block


# Преобразование из десятичного числа в HEX

def int_to_hex(bytes_list):
    block_hex = ''
    for i in range(len(bytes_list)):
        y = hex(bytes_list[i])[2:]
        if len(y) < 2:
            block_hex += '0' + y
        else:
            block_hex += y
    return block_hex


# Сложение блоков по модулю 2 (Побитовый XOR)

def block_to_xor(left_block, right_block):
    x_conv = []
    for i in range(16):
        x_conv.append(left_block[i] ^ right_block[i])
    return x_conv


# Линейное преобразование (L - преобразование)

def l_conv(x):
    for i in range(16):
        xor_byte = 0
        for j in range(16):
            byte = multiply_in_galois_field(x[i + j], galois_row[j])
            xor_byte = xor_byte ^ byte
        x.append(xor_byte)
    return x[16:]


# Сложение по модулю 2 и нелинейное преобразование (X, S - преобразование)

def x_s_conversion(k_1, c_n):
    x_conv = block_to_xor(k_1, c_n)
    s_conversion = []
    s_x_s = ''
    for i in range(16):
        s_conversion.append(s_box[x_conv[i]])
        s_x_s += hex(s_box[x_conv[i]])[2:]
    return s_conversion


# Функция формирования десяти раундовых ключей (X, S, L - преобразования на основе мастер ключа и итерационных констант)

def gen_round_keys(key):
    round_keys = []
    key = hex_to_int(key)
    round_keys.append(key[:16])
    round_keys.append(key[16:])
    constants = generate_iter_consts()

    for i in range(32):
        k = key[:16]
        left = key[:16]
        right = key[16:]
        left = x_s_conversion(left, constants[i])
        left.reverse()
        left = l_conv(left)
        left.reverse()
        left = block_to_xor(left, right)
        left.extend(k)
        key = left
        if (i + 1) % 8 == 0:
            round_keys.append(key[:16])
            round_keys.append(key[16:])
    for i in range(10):
        print(int_to_hex(round_keys[i]))
    return round_keys


round_key = gen_round_keys('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef')
print(round_key)
