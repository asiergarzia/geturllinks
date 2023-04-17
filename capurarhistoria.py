import sqlite3
import os

# Ruta a la base de datos del historial de Google Chrome en Windows
# Cambiar la ruta si se está utilizando otro sistema operativo o navegador
data_path = os.path.expanduser(
    "~") + r"\AppData\Local\Google\Chrome\User Data\Default"
history_db = os.path.join(data_path, "history")

# Consulta para obtener el historial completo de Google Chrome
query = "SELECT url, title, visit_count, last_visit_time FROM urls ORDER BY last_visit_time DESC"

# Conecta a la base de datos y realiza la consulta
conn = sqlite3.connect(history_db)
cursor = conn.cursor()
cursor.execute(query)
results = cursor.fetchall()

# Imprime los resultados
with open('template2.txt', "a", encoding="utf-8") as file:
    for row in results:
        url = row[0]
        title = row[1]
        visit_count = row[2]
        last_visit_time = row[3]
        file.write(title + " : " + url + "/n")

print(f"{title} ({url}) - Visitado {visit_count} veces, última visita en {last_visit_time}")
