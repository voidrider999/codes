ships = {}
while true do
    io.write("Введите название корабля: ")
    local ship = io.read()
    if ship == "" then
        break
    end
    if ships[ship] == nil then
        ships[ship] = 1
    else
        ships[ship] = ships[ship] + 1
    end
    for k,v in pairs(ships) do
        print(k.. ":" ..v)
    end
end
