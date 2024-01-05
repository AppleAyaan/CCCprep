m = int(input())
n = int(input())

counter = 0

for x in range(m, n+1):
  skip = False
  number = str(x)
  rotated = ""
  
  for y in range(len(number)):
    if number[y] == "6":
      rotated += "9"
    elif number[y] == "9":
      rotated += "6"
    elif number[y] == "8":
      rotated += "8"
    elif number[y] == "1":
      rotated += "1"
    elif number[y] == "0":
      rotated += "0"
    else:
      skip = True
      break
  
  if number == rotated[::-1] and skip == False:
    counter = counter + 1
    
print (counter)