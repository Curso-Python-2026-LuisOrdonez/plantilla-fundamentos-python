# ejercicio_propina.py
# Este programa calcula cuánto dejar de propina en un restaurante

print("--- Calculadora de Propinas para conocimiento basico ---")

# 1. Pedir el total de la cuenta
cuenta = float(input("¿Cuánto fue el total de la cuenta?: $"))

# 2. Pedir el porcentaje de propina (ejemplo: 10, 15, 20)
porcentaje = int(input("¿Qué porcentaje de propina quieres dejar? (10, 15, etc): "))

# 3. Calcular la propina y el total final
propina = cuenta * (porcentaje / 100)
total_a_pagar = cuenta + propina

# 4. Mostrar los resultados
print(f"\nResumen:")
print(f"Cuenta inicial: ${cuenta}")
print(f"Propina ({porcentaje}%): ${propina}")
print(f"TOTAL A PAGAR: ${total_a_pagar}")
# Prueba de conexion LTI Moodle.
# Intento de sincronización final.
# Intento de sincronización final.
