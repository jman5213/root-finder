import os

def slowest():
  while True:
    quit = ["end","quit","done","finish","finished","complete"]
    x = input("Your test number:\n>>> ")
    if x.lower() in quit:
      break
    else:
      x = int(x)
    y = int(input("Your root:\n>>> "))
    epsilon = 0.01
    done = False
    step = epsilon**y
    numGuesses = 0
    ans = 0.0
    while abs(ans**y - x) >= epsilon and ans <= x:
      ans += step
      numGuesses += 1
    print("numGuesses =",numGuesses)
    if abs(ans**y - x) >= epsilon:
      print("Failed on square root of", x)
    else:
      for i in range(0, len(str(x))):
        if round(ans,i)**y == x:
          print(round(ans, i), "is the answer of",y,"^", round(ans, i),"\n")
          print("what the computer found =",ans)
          done = True
          break
      if done == False:
        print(ans, "is close to the answer of",x,"root",y,"\n")

def speed():
  while True:
    quit = ["end","quit","done","finish","finished","complete"]
    x = input("Your test number:\n>>> ")
    if x.lower() in quit:
      break
    else:
      x = int(x)
    y = int(input("Your root:\n>>> "))
    epsilon = 0.01
    numGuesses = 0
    done = False
    low = 0.0
    high = max(1.0, x)
    ans = (high+low)/2.0
    while abs(ans**y - x) >= epsilon:
      print("low =",low,"high =",high,"ans =",ans)
      numGuesses += 1
      if ans**2<x:
        low = ans
      else:
        high = ans
      ans = (high+low)/2.0
    for i in range(0, len(str(x))):
      if round(ans,i)**y == x:
        print("\n",round(ans, i), "is the answer of",y,"^", round(ans, i),"\n")
        print("what the computer found =",ans,"\n")
        print("numGuesses =",numGuesses)
        done = True
        break
    if done == False:
      print("\n",ans, "is close to the answer of",x,"root",y,"\n")
      print("numGuesses =",numGuesses)
      input("")
      os.system("clear")


speed()