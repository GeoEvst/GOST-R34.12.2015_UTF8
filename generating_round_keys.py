from iterative_constants import generate_iter_consts, generate_table_galois, multiply_in_galois_field

galois_row = (1, 148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148)
galois_row_r = (148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1)

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

c = ['6ea276726c487ab85d27bd10dd849401', 'dc87ece4d890f4b3ba4eb92079cbeb02', 'b2259a96b4d88e0be7690430a44f7f03',
'7bcd1b0b73e32ba5b79cb140f2551504', '156f6d791fab511deabb0c502fd18105', 'a74af7efab73df160dd208608b9efe06',
'c9e8819dc73ba5ae50f5b570561a6a07', 'f6593616e6055689adfba18027aa2a08', '98fb40648a4d2c31f0dc1c90fa2ebe09',
'2adedaf23e95a23a17b518a05e61c10a', '447cac8052ddd8824a92a5b083e5550b', '8d942d1d95e67d2c1a6710c0d5ff3f0c',
'e3365b6ff9ae07944740add0087bab0d', '5113c1f94d76899fa029a9e0ac34d40e', '3fb1b78b213ef327fd0e14f071b0400f',
'2fb26c2c0f0aacd1993581c34e975410', '41101a5e6342d669c4123cd39313c011', 'f33580c8d79a5862237b38e3375cbf12',
'9d97f6babbd222da7e5c85f3ead82b13', '547f77277ce987742ea93083bcc24114', '3add015510a1fdcc738e8d936146d515',
'88f89bc3a47973c794e789a3c509aa16', 'e65aedb1c831097fc9c034b3188d3e17', 'd9eb5a3ae90ffa5834ce2043693d7e18',
'b7492c48854780e069e99d53b4b9ea19', '056cb6de319f0eeb8e80996310f6951a', '6bcec0ac5dd77453d3a72473cd72011b',
'a22641319aecd1fd835291039b686b1c', 'cc843743f6a4ab45de752c1346ecff1d', '7ea1add5427c254e391c2823e2a3801e',
'1003dba72e345ff6643b95333f27141f', '5ea7d8581e149b61f16ac1459ceda820']


def hex_to_int(x):
    cnt = 2
    block = []
    for i in range(16):
        x_1 = x[2 * i:cnt]
        cnt += 2
        x_i = int(x_1, 16)
        block.append(x_i)
    return block


def int_to_hex(bytes_list):
    block_hex = ''
    for i in range(16):
        y = hex(bytes_list[i])[2:]
        if len(y) < 2:
            block_hex += '0' + y
        else:
            block_hex += y
    return block_hex


def block_to_xor(left_block, right_block):
    x_conv = []
    cnt = 2
    for i in range(16):
        left_block_int, right_block_int = int(left_block[2 * i:cnt], 16), int(right_block[2 * i:cnt], 16)
        x_conv.append(left_block_int ^ right_block_int)
        cnt += 2
    return x_conv


def l_conv(x):
    for i in range(16):
        xor_byte = 0
        for j in range(16):
            byte = multiply_in_galois_field(x[i + j], galois_row[j])
            xor_byte = xor_byte ^ byte
        x.append(xor_byte)
    return x[16:]


def x_s_conversion(k_1, c_n):
    x_conv = block_to_xor(k_1, c_n)
    s_conversion = []
    s_x_s = ''
    for i in range(16):
        s_conversion.append(s_box[x_conv[i]])
        s_x_s += hex(s_box[x_conv[i]])[2:]
    return s_conversion


round_keys = []
key = '8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef'


round_keys.append(key)
constants = generate_iter_consts()

for i in range(1):
    k = key[:32]
    left = key[:32]
    right = key[32:]
    left = x_s_conversion(left, constants[0][1])
    print(int_to_hex(left))






