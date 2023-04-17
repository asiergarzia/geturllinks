import android

droid = android.Android()

# Ejecuta un comando en la shell de Android para obtener el archivo del historial
history_file = droid.shell(
    'su -c "cat /data/data/com.android.chrome/app_chrome/Default/History"').result

# Abre el archivo de historial y lee los datos
with open(history_file, "rb") as f:
    data = f.read()

# Procesa los datos para extraer las URL y los títulos de las páginas visitadas
for line in data.split(b"\n"):
    if line.startswith(b"www.") or line.startswith(b"http"):
        url = line.split(b"|")[1]
        title = line.split(b"|")[2]
        print(f"{title.decode()} ({url.decode()})")
