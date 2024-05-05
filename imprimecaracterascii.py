import keyboard

for i in range(128):
  char = chr(i)
  print(i, char)
  if keyboard.is_pressed("ñ"):
    ascii = ord("ñ")
    print("El valor ASCII de la letra ñ es", ascii)
    break

