def min_coins(V, coins):
  result = [0] * len(coins)

  for i in range(len(coins) - 1, -1, -1):
      while V >= coins[i]:
          V -= coins[i]
          result[i] += 1

  return result

def print_coins(result, coins):
  for i in range(len(result)):
      if result[i] > 0:
          print(result[i], "monedas de", coins[i])

def main():
  coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

  V1 = 2550
  V2 = 8432
  V3 = 263

  result1 = min_coins(V1, coins)
  result2 = min_coins(V2, coins)
  result3 = min_coins(V3, coins)

  print("Para V =", V1, "se necesitan en total")
  print_coins(result1, coins)
  print()

  print("Para V =", V2, "se necesitan en total")
  print_coins(result2, coins)
  print()

  print("Para V =", V3, "se necesitan en total")
  print_coins(result3, coins)

if __name__ == "__main__":
  main()
