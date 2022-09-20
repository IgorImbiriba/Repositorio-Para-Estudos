print('vamos fazer caonversoes de temperaturas?')
c = float(input('digite um valor entre -273 a 100 para °C: '))
k = float(input('digite um valor entre 0 a 373 para °K: '))
f = float(input('digite um vafor entre -459 a 212 para °: '))

k_to_c = k - 273 
c_to_k = c + 273
f_to_c = (f -32) / 1.8
f_to_c2 = ((f -32)*5)/9
c_to_f = c * 1.8 + 32
f_to_k = (f - 32) * 5/9 + 273
k_to_f = (k -273) * 1.8 + 32

print("""Você digitou as segintes temperaturas:
{:.1f} °C
{:.1f} °K
{:.1f} °f
Todas as converções estão abaixo
de {:.1f}°K para °C: {:.1f}°C
de {:.1f}°C para °K: {:.1f}°K
de {:.1f}°f para °C: {:.1f}°C
de {:.1f}°C para °f: {:.1f}°f
de {:.1f}°f para °K: {:.1f}°K
de {:.1f}°K para °f: {:.1f}°f""".format(
    c, k, f,
    k, k_to_c,
    c, c_to_k,
    f, f_to_c,
    c, c_to_f,
    f, f_to_k,
    k, k_to_f))