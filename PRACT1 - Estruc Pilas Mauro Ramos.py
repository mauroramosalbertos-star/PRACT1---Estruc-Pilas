import tkinter as tk

OPS = [("I", "X"), ("I", "Y"), ("E", "Z"), ("E", "T"), ("E", "U"), ("I", "V"), ("I", "W"), ("E", "p"), ("I", "R")]
N, W, H, Y0 = 8, 100, 34, 50

pila, estados = [], []
for op, v in OPS:
    err = None
    if op == "I" and len(pila) == N:
        err = "DESBORDAMIENTO"
    elif op == "E" and not pila:
        err = "SUBDESBORDAMIENTO"
    elif op == "I":
        pila.append(v)
    else:
        pila.pop()
    estados.append((op, v, list(pila), err))

root = tk.Tk()
root.title("Estados de la pila")
c = tk.Canvas(root, width=W * len(OPS) + 20, height=Y0 + N * H + 110, bg="white")
c.pack()

for i, (op, v, p, err) in enumerate(estados):
    x = 20 + i * W
    rojo = "red" if err else "black"
    c.create_text(x + 35, 20, text=f"{'abcdefghi'[i]}) {'Insertar' if op == 'I' else 'Eliminar'}({v})", font=("Arial", 9, "bold"), fill=rojo)
    for j in range(N):
        y = Y0 + (N - 1 - j) * H
        c.create_rectangle(x, y, x + 70, y + H, fill="#9ec9ff" if j < len(p) else "white")
        if j < len(p):
            c.create_text(x + 35, y + H / 2, text=p[j], font=("Arial", 12, "bold"))
    ya = Y0 + (N - len(p)) * H - (H / 2 if p else 0)
    c.create_line(x + 98, ya, x + 74, ya, arrow=tk.LAST, fill="red", width=2)
    c.create_text(x + 35, Y0 + N * H + 18, text=f"TOPE={len(p)}", font=("Arial", 10, "bold"))
    if err:
        c.create_text(x + 35, Y0 + N * H + 40, text=err, fill="red", font=("Arial", 7, "bold"))

c.create_text(
    10, Y0 + N * H + 80, anchor="w", font=("Arial", 11, "bold"),
    text=f"Elementos finales: {len(pila)}   |   Errores: {', '.join('abcdefghi'[i] + ') ' + e[3] for i, e in enumerate(estados) if e[3]) or 'ninguno'}",
)

root.mainloop()