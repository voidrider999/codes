ships = {}
while true do
    io.write("Введите название корабля: ")
    local ship = io.read()
    if ship == "nil" then
        break
    end
    if ships[ship] == n then
        ships[ship] = 1
        print(ships)
    else
        ships[ship] = ships[ship] + 1
    end
    for k,v in pairs(ships) do
        print(k.. ":" ..v)
    end
end
