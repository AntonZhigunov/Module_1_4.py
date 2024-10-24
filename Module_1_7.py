immutable_var = 1, 2, 3, 4, "test"
print(immutable_var)
print("immutable_var[2] = 25 операция не возможна. Кортедж для хранения массива данных, не изменения.")
mutable_list = [1, 2, 6, "e", "r", "test"]
print(mutable_list)
print(mutable_list[::2])
mutable_list[1]="dwa"
print(mutable_list)
mutable_list.remove("dwa")
mutable_list.extend([2,"black","cats"])
print(mutable_list)
print(2 in mutable_list)
print("dwa" not in mutable_list)