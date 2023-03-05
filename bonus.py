from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math


def get_main_function():
    x = np.linspace(0, math.pi * 3 / 2, 30)
    y = np.linspace(0, math.pi * 3 / 2, 30)
    X, Y = np.meshgrid(x, y)
    print()
    return np.sin(X * Y)


def make_function_noisy(z):
    max_noise = 0.1
    t = 2 * np.random.rand(30 * 30) * max_noise - max_noise
    t = t.reshape(30, 30)
    print()
    return np.add(z, t)


def get_function():
    print()
    return make_function_noisy(get_main_function())


def make_clean_function(z):
    u, s, v = np.linalg.svd(z)
    print(s)
    s_array = np.zeros((line_array_size(z), column_array_size(z)))
    print(s_array.shape)
    print()
    for i in range(line_array_size(z)):
        for j in range(column_array_size(z)):
            if i == j:
                if s[j] > 0.5:
                    s_array[i][j] = s[j]
    cleaned_matrix = u @ s_array @ v
    return cleaned_matrix


def line_array_size(z):
    print()
    return(z.shape[0])


def column_array_size(z):
    return(z.shape[1])


def get_denoised_function():
    return make_clean_function(get_function())


def show_my_matrix(Z):
    x = np.linspace(0, math.pi * 3 / 2, 30)
    y = np.linspace(0, math.pi * 3 / 2, 30)
    X, Y = np.meshgrid(x, y)
    print(X)
    ax = plt.axes(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='black')
    ax.set_title('surface');
    ax.view_init(60, 35)
    print()
    plt.show()


def show_main():
    Z = get_main_function()
    print()
    show_my_matrix(Z)


def show_noisy():
    Z = get_function()
    show_my_matrix(Z)


def show_denoised():
    Z = get_denoised_function()
    show_my_matrix(Z)


show_main()
show_noisy()
show_denoised()

