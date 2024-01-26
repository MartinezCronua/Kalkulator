def dodawanie(x, y):
	return x + y
def odejmowanie(x, y):
	return x - y
def mnozenie(x, y):
	return x * y
def dzielenie(x, y):
	if y !=0:
		return x / y
	else:
		return "Nie można dzielić przez zero."

while True:
	print("Wybierz operację:")
	print("1. Dodawanie")
	print("2. Odejmowanie")
	print("3. Mnożenie")
	print("4. Dzielenie")
	print("0. Wyjście")

	choice = input("Wprowadź numer operacji (0-4): ")
	if choice == '0':
		break
	if choice in ('1', '2', '3', '4'):
		num1 = float(input("Wprowadź pierwszą liczbę: "))
		num2 = float(input("Wprowadź drugą liczbę: "))

	if choice == '1':
		print(num1, "+", num2, "=", dodawanie(num1, num2))
	elif choice == '2':
		print(num1, "-", num2, "=", odejmowanie(num1, num2))
	elif choice == '3':
		print(num1, "*", num2, "=", mnozenie(num1, num2))
	elif choice == '4':
		result = dzielenie(num1, num2)
		print(num1, "/", num2, "=", result)
	else:
		print("Nieprawidłowy wybór. Wprowadź liczbę od 0 do 4.")

