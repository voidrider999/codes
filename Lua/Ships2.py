ships = {}

while true do
    print("Введите название корабля: ")
    local ship = io.read()
    
    if ships[ship] == nil then
        ships[ship] = 1
        print(ships)
    else
        ships[ship] = ships[ship] + 1
    end
end
