import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0
    while guess != number_to_guess:
        guess = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
        attempts += 1
        if guess < number_to_guess:
            print("Daha yüksek bir sayı deneyin.")
        elif guess > number_to_guess:
            print("Daha düşük bir sayı deneyin.")
    print(f"Tebrikler! {attempts} denemede sayıları buldunuz.")

if __name__ == "__main__":
    guess_number()