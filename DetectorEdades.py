# Sistema para detectar categorías de edad

print("Sistema de detección de edades")
print("-" * 30)

seguir_programa = "si"

# Bucle while para continuar el programa hasta que el usuario decida salir
while seguir_programa == "si":
    try:
        # Pedimos la edad al usuario
        edad = int(input("¿Cuál es tu edad? "))

        # Revisamos en qué categoría está
        if edad < 13:
            print("Eres un niño")
            print("No eres mayor de edad")
        elif edad < 18:
            print("Eres un adolescente")
            print("No eres mayor de edad")
        elif edad < 65:
            print("Eres un adulto") 
            print("Eres mayor de edad")
        else:
            print("Eres un adulto mayor")
            print("Eres mayor de edad")
        
        # Preguntamos si quiere continuar
        seguir_programa = input("\n¿Quieres comprobar otra edad? (si/no): ").lower()
    
    except ValueError:
        print("Por favor, ingresa un número válido para la edad.")

print("\n¡Gracias por usar el sistema!")
