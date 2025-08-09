offices = {
    {"john", "sam"},
    {"peter", "stu", "miles", "isaac"},
    {"martha", "chloe", "zanthia"}
}

for _, office in ipairs(offices) do
    io.write(#office .. ": ")
    for _, person in ipairs(office) do
        io.write(person .. " ")
    end
    io.write("\n")
end
