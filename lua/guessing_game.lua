math.randomseed(os.time()) -- инициализация генератора случайных чисел
local secret = math.random(1, 100)
print('Отгадай число от 1 до 100')

while true do
    io.write('Введите число: ')
    local s = io.read()
    if #s == 0 then
        break
    end
    local num = tonumber(s)
    if num == secret then
        print('Вы угадали')
        break
    end
    if secret > num then
        print('Загаданное число больше')
    end
    if secret < num then
        print('Загаданное число меньше')
    end
end
