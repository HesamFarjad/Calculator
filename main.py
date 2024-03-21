import art


#add
def add(n1, n2):
  return n1 + n2


#subtract
def subtract(n1, n2):
  return n1 - n2


#multiply
def multiply(n1, n2):
  return n1 * n2


#divide
def divide(n1, n2):
  return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
  print(art.logo)
  num1 = float(input("What's the first number? "))
  print("\n")
  for i in operations:
    print(i)
  print("\n")
  symbol = input("Pick an operation from the line above: ")
  print("\n")
  num2 = float(input("What's the second number? "))
  print("\n")

  cal_function = operations[symbol]
  answer1 = cal_function(num1, num2)
  print(f" {num1} {symbol} {num2} = {answer1}")
  print("\n")

  cal_is_over = False
  while not cal_is_over:
    symbol2 = input("Pick another operation: ")
    print("\n")
    num3 = float(input("What's the next number? "))

    cal_function2 = operations[symbol2]
    answer2 = cal_function2(answer1, num3)
    print("\n")
    print(f" {answer1} {symbol2} {num3} = {answer2}")
    print("\n")
    question_continue = input(
        f"Do you want to continue with \"{answer2}\" ? \" Y \" or \" N \" "
    ).lower()
    print("\n")
    if question_continue == "n":
      # print("Thank you for using the calculator")
      cal_is_over = True
      calculator()
    answer1 = answer2


calculator()
