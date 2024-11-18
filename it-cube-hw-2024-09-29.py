a = int(input('Введите 4-значное число: '))
q = a % 10
r = a // 10 % 10
s = a // 100 % 10
t = a // 1000

print(f'q={q} r={r} s={s} t={t}')
if q > r:
    q, r = r, q
print(f'q={q} r={r} s={s} t={t}')
if r > s:
    r, s = s, r
print(f'q={q} r={r} s={s} t={t}')
if s > t:
    s, t = t, s
print(f'q={q} r={r} s={s} t={t}')

print('-------')
if q > r:
    q, r = r, q
print(f'q={q} r={r} s={s} t={t}')
if r > s:
    r, s = s, r
print(f'q={q} r={r} s={s} t={t}')

print('-------')
if q > r:
    q, r = r, q
print(f'q={q} r={r} s={s} t={t}')
print('-------')

print(t, s, r, q)
