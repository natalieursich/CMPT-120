def main():
  
  #set this to any double
  doubleValue = 2.467239
  print(doubleValue)
  
  #set this to any int
  intValue = 4
  print(intValue)
  
  #print out addition, subtraction, multiplication, and division of these two values
  print(doubleValue + intValue)
  print(doubleValue - intValue)
  print(doubleValue * intValue)
  print(doubleValue / intValue)

  #populate this list
  myFriends = ["lex", "syd", "charlotte", "julia", "shannon", "grace"]
  print(myFriends)
  
  #print out your friends at index 2 and index 3
  print(myFriends[2])
  print(myFriends[3])
  
  #populate this list with five numbers
  fiveNumbers = [3, 4, 6, 71, 94]
  
  #do each of the four equations with different numbers each time.
  print(fiveNumbers[0] + fiveNumbers[3])
  print(fiveNumbers[4] - fiveNumbers[2])
  print(fiveNumbers[1] * fiveNumbers[4])
  print(fiveNumbers[3] / fiveNumbers[2])
  
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  print(fiveNumbers)
  fiveNumbers[2] = 17
  fiveNumbers[0] = 63
  
  #print out the list
  print(fiveNumbers)
  
  
main()
