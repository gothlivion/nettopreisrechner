import tkinter as tk

def berechne_netto_preis(bruttopreis, mehrwertsteuersatz=19):
    try:
        bruttopreis = float(bruttopreis)
        mehrwertsteuersatz = float(mehrwertsteuersatz)
        nettopreis = bruttopreis / (1 + mehrwertsteuersatz / 100)
        return f"{nettopreis:.2f}"
    except ValueError:
        return "Ungültige Eingabe"

def on_calculate():
    bruttopreis = bruttopreis_entry.get()
    mehrwertsteuersatz = mwst_entry.get() or 19  # Default-Wert 19, falls leer
    result = berechne_netto_preis(bruttopreis, mehrwertsteuersatz)
    result_label.config(text=f"Nettopreis: {result}")

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Nettopreis Rechner")
root.configure(bg="#e6f7ff")  # Hintergrundfarbe des Fensters

# Styles
entry_bg = "#ffffff"  # Hintergrundfarbe der Eingabefelder
entry_fg = "#000000"  # Textfarbe der Eingabefelder
button_bg = "#4CAF50"  # Hintergrundfarbe des Buttons
button_fg = "#ffffff"  # Textfarbe des Buttons
label_bg = "#e6f7ff"  # Hintergrundfarbe der Labels
label_fg = "#000000"  # Textfarbe der Labels

# Erstelle und platziere Widgets
tk.Label(root, text="Bruttopreis:", bg=label_bg, fg=label_fg).grid(row=0, column=0, padx=10, pady=10, sticky="w")
bruttopreis_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
bruttopreis_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Mehrwertsteuersatz (%):", bg=label_bg, fg=label_fg).grid(row=1, column=0, padx=10, pady=10, sticky="w")
mwst_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
mwst_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Berechnen", command=on_calculate, bg=button_bg, fg=button_fg)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Nettopreis: ", bg=label_bg, fg=label_fg)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Starte die Hauptschleife
root.mainloop()


