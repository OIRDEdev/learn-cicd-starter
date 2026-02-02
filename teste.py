import threading
import time
import random

saldo = 100

def sacar(valor):
    global saldo
    saldo_atual = saldo          # 1️⃣ lê o saldo
    time.sleep(random.random())  # 2️⃣ força troca de contexto
    saldo = saldo_atual - valor  # 3️⃣ escreve depois
    print(f"Saque {valor} | saldo final: {saldo}")

threads = []

# duas operações concorrentes
t1 = threading.Thread(target=sacar, args=(80,))
t2 = threading.Thread(target=sacar, args=(30,))

threads.append(t1)
threads.append(t2)

t1.start()
t2.start()

for t in threads:
    t.join()

print("Saldo esperado lógico: -10 ou erro")
print("Saldo REAL:", saldo)
