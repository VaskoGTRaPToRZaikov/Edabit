import random

SYMBOLS = ['🍒', '🍋', '🍊', '🍇', '🍉', '⭐', '💎', '7️⃣']

PAYOUTS = {
    ('7️⃣', '7️⃣', '7️⃣', '7️⃣'): 1000,
    ('💎', '💎', '💎', '💎'): 500,
    ('⭐', '⭐', '⭐', '⭐'): 300,
    ('🍉', '🍉', '🍉', '🍉'): 250,
    ('🍇', '🍇', '🍇', '🍇'): 200,
    ('🍊', '🍊', '🍊', '🍊'): 175,
    ('🍋', '🍋', '🍋', '🍋'): 150,
    ('🍒', '🍒', '🍒', '🍒'): 125,
    ('7️⃣', '7️⃣', '7️⃣'): 100,
    ('💎', '💎', '💎'): 50,
    ('⭐', '⭐', '⭐'): 30,
    ('🍉', '🍉', '🍉'): 20,
    ('🍇', '🍇', '🍇'): 15,
    ('🍊', '🍊', '🍊'): 10,
    ('🍋', '🍋', '🍋'): 8,
    ('🍒', '🍒', '🍒'): 6,
}

def spin_slots():
    return [random.choice(SYMBOLS) for _ in range(4)]

def check_win(symbols):
    if len(set(symbols)) == 1:
        combo = tuple(symbols)
        return PAYOUTS.get(combo, 100)

    if symbols[0] == symbols[1] == symbols[2]:
        combo = tuple(symbols[:3])
        return PAYOUTS.get(combo, 5)

    return 0

def play_game():
    print("🎰 Добре дошли в Slot Machine! 🎰")
    print("=" * 50)
    balance = 100

    while balance > 0:
        print(f"\n💰 Текущ баланс: {balance} лв")

        try:
            bet = int(input("Въведете залог (или 0 за изход): "))
            if bet == 0:
                print(f"Благодарим за играта! Финален баланс: {balance} лв")
                break

            if bet > balance:
                print("❌ Нямате достатъчно средства!")
                continue

            if bet <= 0:
                print("❌ Залогът трябва да е положително число!")
                continue

        except ValueError:
            print("❌ Моля, въведете валидно число!")
            continue

        balance -= bet
        symbols = spin_slots()

        print(f"\n🎰 [{' | '.join(symbols)}]")

        multiplier = check_win(symbols)

        if multiplier > 0:
            winnings = bet * multiplier
            balance += winnings
            print(f"🎉 ПЕЧАЛБА! x{multiplier} = {winnings} лв")

            if multiplier >= 1000:
                print("💰💰💰 ДЖАКПОТ!!! 💰💰💰")

        else:
            print("😔 Няма печалба. Опитайте отново!")

    if balance == 0:
        print("\n💸 Нямате повече средства. Играта приключи!")

if __name__ == "__main__":
    play_game()