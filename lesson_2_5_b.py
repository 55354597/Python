price_list = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78,
              48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
for i in price_list:
    r, k = int(i // 1), int(f"{i % 1:.02f}"[2:])
    print(f"{r} руб. {k:02d} коп.", end=" ")
print(f"old: {(price_list)} - {price_list}")
price_list.sort()
print(f"new: {(price_list)} - {price_list}")
