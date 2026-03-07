# Dizionario per memorizzare i dipendenti e la loro sede attuale (1 o 2)
dipendenti = {}

# Costante: la sede che possiede la linea telefonica fissa
SEDE_CON_LINEA = 1

def aggiungi_dipendente(nome, sede):
    """Registra un nuovo dipendente con la sede iniziale."""
    dipendenti[nome] = sede
    print(f"Dipendente {nome} aggiunto in sede {sede}.")

def sposta_dipendente(nome, nuova_sede):
    """Cambia la sede di un dipendente (es. quando si sposta fisicamente)."""
    if nome in dipendenti:
        dipendenti[nome] = nuova_sede
        print(f"{nome} ora è in sede {nuova_sede}.")
    else:
        print("Dipendente non trovato.")

def gestisci_chiamata(nome_chiamato):
    """Gestisce una chiamata in arrivo sulla sede con linea."""
    if nome_chiamato not in dipendenti:
        print("Dipendente sconosciuto.")
        return

    sede_dest = dipendenti[nome_chiamato]

    if sede_dest == SEDE_CON_LINEA:
        # Il dipendente è nella sede che ha ricevuto la chiamata
        print(f"Chiamata per {nome_chiamato} – è in sede {sede_dest}. Risponde subito.")
    else:
        # Il dipendente è nell'altra sede: inoltro immediato
        print(f"Chiamata per {nome_chiamato} – non è in sede {SEDE_CON_LINEA}. "
              f"Inoltro alla sede {sede_dest} in corso...")
        print(f"Chiamata inoltrata. {nome_chiamato} risponde in sede {sede_dest}.")

def leggi_sede(messaggio):
    """Richiede all'utente di inserire un numero di sede valido (1 o 2)."""
    while True:
        valore = input(messaggio)
        if valore.isdigit():
            numero = int(valore)
            if numero == 1 or numero == 2:
                return numero
        print("Errore: inserisci 1 o 2.")

def menu():
    """Interfaccia testuale per interagire con il centralino."""
    while True:
        print("\n=== Centralino con inoltro chiamate (senza classi, senza try) ===")
        print("1. Aggiungi dipendente")
        print("2. Sposta dipendente")
        print("3. Gestisci chiamata")
        print("4. Esci")
        scelta = input("Scegli: ")

        if scelta == '1':
            nome = input("Nome dipendente: ")
            sede = leggi_sede("Sede iniziale (1 o 2): ")
            aggiungi_dipendente(nome, sede)

        elif scelta == '2':
            nome = input("Nome dipendente: ")
            if nome in dipendenti:
                nuova_sede = leggi_sede("Nuova sede (1 o 2): ")
                sposta_dipendente(nome, nuova_sede)
            else:
                print("Dipendente non trovato.")

        elif scelta == '3':
            nome = input("Nome dipendente da chiamare: ")
            gestisci_chiamata(nome)

        elif scelta == '4':
            print("Chiusura centralino.")
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    # Aggiungiamo alcuni dipendenti di esempio
    aggiungi_dipendente("Mario", 1)
    aggiungi_dipendente("Luigi", 2)
    aggiungi_dipendente("Anna", 1)
    menu()
