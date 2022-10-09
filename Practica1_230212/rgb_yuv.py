#creamos dos funciones que convierten de rgb a yuv y deshacen el cambio.
def rgb2yuv(r, g, b):
    #como vemos cada valor de yuv es la combinación de los 3 valores rgb ponderados.
    y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    u = -0.148 * r - 0.291 * g + 0.439 * b + 128
    v = 0.439 * r - 0.368 * g - 0.071 * b + 128

    return [y, u, v]


def yuv2rgb(y, u, v):
    #aquí debemos deshacer los cambios, como vemos es realizar la operación contraria (hemos aislado las variables r,g,b.
    b = 1.164 * (y - 16) + 2.018 * (u - 128)
    g = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (u - 128)
    r = 1.164 * (y - 16) + 1.596 * (v - 128)

    return [r, g, b]

#empieza el script donde se introduciran los valores, se llamarà a las funciones y los resultado se mostraran en pantalla.
print("Red:")
r = float(input())
print("Green:")
g = float(input())
print("Blue:")
b = float(input())

[Y, U, V] = rgb2yuv(r, g, b)
print("Y: ", Y)
print("U: ", U)
print("V: ", V)

[R, G, B] = yuv2rgb(Y, U, V)

print("If we recover the original values: ")
print("R: ", R)
print("G: ", G)
print("B: ", B)
