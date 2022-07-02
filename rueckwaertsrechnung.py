def main():
    print("Hallo und herzlich willkommen beim Rückwärtsrechner.")
    gewinn = ask_user_for_number("Welche Gewinnsumme soll ausgeschüttet werden? ")
    rabatt = ask_user_for_number("Welcher Rabatt wird dem Kunden gutgeschrieben (in %)? ")
    liste = listenpreis(gewinn=gewinn, rabatt=rabatt)
    print(f"Der Listenpreis beträgt dann {liste}.")


def ask_user_for_number(prompt: str) -> float:
    text = input(prompt)
    number = float(text)
    return number


def listenpreis(gewinn: float, rabatt: float) -> float:
    prozent_liste = gewinn / (100-rabatt)
    liste = prozent_liste * 100
    return liste


if __name__ == "__main__":
    main()