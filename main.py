import numpy as np
from matplotlib import pyplot as plt

noisy_matrix = plt.imread("noisy.jpg")

red_matrix_factor = np.zeros((noisy_matrix.shape[0], noisy_matrix.shape[1]))
print(red_matrix_factor.shape)
green_matrix_factor = np.zeros((noisy_matrix.shape[0], noisy_matrix.shape[1]))
print(green_matrix_factor.shape)
blue_matrix_factor = np.zeros((noisy_matrix.shape[0], noisy_matrix.shape[1]))
print(blue_matrix_factor.shape)

for i in range(noisy_matrix.shape[0]):
    for j in range(noisy_matrix.shape[1]):
        red_matrix_factor[i][j] = noisy_matrix[i][j][0]
        print(red_matrix_factor[i][j])
        green_matrix_factor[i][j] = noisy_matrix[i][j][1]
        print(green_matrix_factor[i][j])
        blue_matrix_factor[i][j] = noisy_matrix[i][j][2]
        print(blue_matrix_factor[i][j])

u_red, s_red, v_red = np.linalg.svd(red_matrix_factor)
print(s_red.shape)
u_green, s_green, v_green = np.linalg.svd(green_matrix_factor)
print(s_green)
u_blue, s_blue, v_blue = np.linalg.svd(blue_matrix_factor)
print(s_blue)

s_red_array = np.zeros((noisy_matrix.shape[0], noisy_matrix.shape[1]))
print(s_red_array.shape)
s_green_array = np.zeros((noisy_matrix.shape[0], noisy_matrix.shape[1]))
print(s_green_array.shape)
s_blue_array = np.zeros((noisy_matrix.shape[0], noisy_matrix.shape[1]))
print(s_blue_array.shape)

print(len(s_red))

for i in range(noisy_matrix.shape[0]):
    for j in range(noisy_matrix.shape[1]):
        if i == j:
            if s_red[j] > 1350:
                s_red_array[i][j] = s_red[j]
            if s_green[j] > 1350:
                s_green_array[i][j] = s_red[j]
            if s_blue[j] > 1350:
                s_blue_array[i][j] = s_red[j]

cleaned_red_matrix = u_red @ s_red_array @ v_red
print()
cleaned_green_matrix = u_green @ s_green_array @ v_green
print()
cleaned_blue_matrix = u_blue @ s_blue_array @ v_blue
print()

cleaned_matrix = np.zeros((noisy_matrix.shape[0], noisy_matrix.shape[1], 3), dtype='uint8')

for i in range(noisy_matrix.shape[0]):
    for j in range(noisy_matrix.shape[1]):
        cleaned_matrix[i][j][0] = cleaned_red_matrix[i][j]
        print()
        cleaned_matrix[i][j][1] = cleaned_green_matrix[i][j]
        print()
        cleaned_matrix[i][j][2] = cleaned_blue_matrix[i][j]

plt.imshow(cleaned_matrix)
plt.show()
print()
plt.imsave("denoised.jpg", cleaned_matrix)





# print(len(u_red[0]))
# print(len(u_red[1]))
# print()
# print(len(s_red))
# print()
# print(len(v_red[0]))
# print(len(v_red[1]))






