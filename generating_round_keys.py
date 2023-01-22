from iterative_constants import generate_iter_consts, generate_table_galois, multiply_in_galois_field

galois_row = [1, 148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148]
galois_row_r = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1]

s_box = [252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 213, 35, 197, 4, 77,
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
         89, 166, 116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182]


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


def block_to_xor(k_n, c_n):
    x_conv = []
    cnt = 2
    for i in range(16):
        k1_int, c_int = int(k_n[2 * i:cnt], 16), int(c_n[2 * i:cnt], 16)
        x_conv.append(k1_int ^ c_int)
        cnt += 2
    # print(int_to_hex(x_conv))
    return x_conv


def l_conv(x):
    print('x =', x)
    for i in range(16):
        xor_byte = 0
        for j in range(16):
            byte = multiply_in_galois_field(x[i + j], galois_row_r[j])
            xor_byte = xor_byte ^ byte
        x.append(xor_byte)
        print(x)
    return x[16:]


def x_s_conversion(k_1, c_n):
    x_conv = block_to_xor(k_1, c_n)
    s_conversion = []
    s_x_s = ''
    for i in range(16):
        s_conversion.append(s_box[x_conv[i]])
        s_x_s += hex(s_box[x_conv[i]])[2:]
    return s_conversion


key = '7766554433221100FFEEDDCCBBAA9988EFCDAB89674523011032547698BADCFE'
key_r = '8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef'
constants = generate_iter_consts()


constants_reversed = []
for i in range(32):
    const_n = constants[i][1]
    cn_r = ''
    cnt_1 = 2
    cnt_2 = 0
    for j in range(16):
        if j == 0:
            cn_r += const_n[-2:]
        else:
            cn_r += const_n[-cnt_1:-cnt_2]
        cnt_1 += 2
        cnt_2 += 2
    constants_reversed.append(cn_r)


n = hex_to_int("0998ca37a7947aabb78f4a5ae81b748a")
l_n = l_conv(n)
print(int_to_hex(l_n))

gal = []
for i in range(16):
    gal.append(multiply_in_galois_field(n[i], galois_row_r[i]))
print(gal)

x_g = 0
for i in range(16):
    x_g = x_g ^ gal[i]
print(hex(x_g)[2:])
print(constants[0])