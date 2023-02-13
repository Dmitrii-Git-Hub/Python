# Задача "Идти ли в школу?"
is_holiday = False
temperature = -30
age = 15
age_limit = 11
temperature_limit = -27
if is_holiday == True:
  print("holiday")
elif temperature >= temperature_limit:
  print("to school")
elif age < age_limit:
  print("home")
else:
  print("to school :(")
