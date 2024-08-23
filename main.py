class SetOperations:
    def __init__(self):
        # Este diccionario es como una estantería donde guardamos nuestras cajitas (conjuntos).
        # Cada conjunto se guarda como una matriz (sí, como una lista de 0s y 1s) que dice si un elemento está en la cajita o no.
        self.conjuntos = {}

    def create_set(self, set_name, elements):
        # Aquí estamos creando una nueva cajita. Si ya existe una con ese nombre, no podemos crearla de nuevo.
        if set_name in self.conjuntos:
            raise ValueError(f"El conjunto '{set_name}' ya existe.")

        # Antes de guardar los elementos, vamos a asegurarnos de que todos son válidos (letras y números).
        validated_elements = self._validate_elements(elements)

        # Convertimos esos elementos en una matriz binaria que será nuestra cajita.
        self.conjuntos[set_name] = {
            "matrix": self._convert_to_matrix(validated_elements),
            "order": elements  # También guardamos el orden original por si lo necesitamos más tarde.
        }

    def operate_sets(self, operation, set1, set2=None, set3=None):
        # Aquí es donde la magia sucede. Dependiendo de la operación, trabajamos con una, dos o tres cajitas.
        # Primero, chequeamos si las cajitas que queremos usar existen.
        if set1 not in self.conjuntos:
            raise ValueError(f"El conjunto '{set1}' no existe.")
        if set2 and set2 not in self.conjuntos:
            raise ValueError(f"El conjunto '{set2}' no existe.")
        if set3 and set3 not in self.conjuntos:
            raise ValueError(f"El conjunto '{set3}' no existe.")

        # Luego, dependiendo de la operación, llamamos a la función adecuada.
        if operation == "complemento":
            return self._complement(set1)
        elif operation == "union":
            return self._union(set1, set2, set3)
        elif operation == "interseccion":
            return self._intersection(set1, set2, set3)
        elif operation == "diferencia":
            return self._difference(set1, set2, set3)
        elif operation == "diferencia simetrica":
            return self._symmetric_difference(set1, set2, set3)
        else:
            raise ValueError("Operación no válida. Las operaciones válidas son: complemento, unión, intersección, diferencia, diferencia simétrica.")

    def _validate_elements(self, elements):
        # Este método es como un portero de discoteca: solo deja entrar letras A-Z y números 0-9.
        valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for element in elements:
            if element not in valid_characters:
                raise ValueError(f"Elemento '{element}' no válido. Solo se permiten letras A-Z y dígitos 0-9.")
        return elements

    def _convert_to_matrix(self, elements):
        # Aquí convertimos los elementos en una matriz binaria de tamaño 36 (26 letras + 10 dígitos).
        # La matriz es como un tablero de luces, donde 1 significa que el elemento está en la cajita y 0 que no está.
        matrix = [0] * 36
        valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for element in elements:
            index = valid_characters.index(element)
            matrix[index] = 1
        return matrix

    def _complement(self, set_name):
        # Esto es para encontrar los elementos que NO están en la cajita.
        # Comparamos nuestra cajita con un tablero donde todas las luces están encendidas (matriz de 1s).
        universal_set = [1] * 36
        result = []
        for i in range(36):
            result.append(1 if self.conjuntos[set_name]["matrix"][i] == 0 else 0)
        return self._matrix_to_set(result)

    def _union(self, set1, set2=None, set3=None):
        # Aquí hacemos la unión: prendemos las luces si el elemento está en cualquiera de las cajitas.
        result = []
        for i in range(36):
            if self.conjuntos[set1]["matrix"][i] == 1 or \
                    (set2 and self.conjuntos[set2]["matrix"][i] == 1) or \
                    (set3 and self.conjuntos[set3]["matrix"][i] == 1):
                result.append(1)
            else:
                result.append(0)
        return self._matrix_to_set(result)

    def _intersection(self, set1, set2=None, set3=None):
        # Aquí hacemos la intersección: solo encendemos las luces si el elemento está en TODAS las cajitas.
        result = []
        for i in range(36):
            if self.conjuntos[set1]["matrix"][i] == 1 and \
                    (not set2 or self.conjuntos[set2]["matrix"][i] == 1) and \
                    (not set3 or self.conjuntos[set3]["matrix"][i] == 1):
                result.append(1)
            else:
                result.append(0)
        return self._matrix_to_set(result)

    def _difference(self, set1, set2=None, set3=None):
        # Esto es para encontrar los elementos que están en la primera cajita pero NO en las otras.
        result = []
        for i in range(36):
            if self.conjuntos[set1]["matrix"][i] == 1 and \
                    (not set2 or self.conjuntos[set2]["matrix"][i] == 0) and \
                    (not set3 or self.conjuntos[set3]["matrix"][i] == 0):
                result.append(1)
            else:
                result.append(0)
        return self._matrix_to_set(result)

    def _symmetric_difference(self, set1, set2=None, set3=None):
        # La diferencia simétrica es como una operación XOR: las luces se prenden si el elemento está en una cajita pero no en todas.
        result = []
        for i in range(36):
            count = 0
            if self.conjuntos[set1]["matrix"][i] == 1:
                count += 1
            if set2 and self.conjuntos[set2]["matrix"][i] == 1:
                count += 1
            if set3 and self.conjuntos[set3]["matrix"][i] == 1:
                count += 1

            # Si el conteo es impar, el elemento está en la diferencia simétrica.
            result.append(1 if count % 2 != 0 else 0)
        return self._matrix_to_set(result)

    def _matrix_to_set(self, matrix):
        # Aquí convertimos nuestra matriz de vuelta a un conjunto de elementos para que sea más fácil de entender.
        valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        result_set = []
        for i in range(36):
            if matrix[i] == 1:
                result_set.append(valid_characters[i])
        return result_set

    def display_sets(self):
        # Este método simplemente imprime todos los conjuntos que has creado hasta ahora.
        if not self.conjuntos:
            print("No se han creado conjuntos.")
        else:
            for set_name, data in self.conjuntos.items():
                print(f"Conjunto {set_name}: {data['order']}")

def display_menu():
    operations = SetOperations()

    while True:
        print("\nMenu Principal:")
        print("1. Crear conjunto")
        print("2. Operar conjuntos")
        print("3. Mostrar todos los conjuntos")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            # Crear un nuevo conjunto
            set_name = input("Ingrese el nombre del conjunto: ")
            elements = input("Ingrese los elementos del conjunto (sin espacios, ej: ABC123): ")
            try:
                operations.create_set(set_name, list(elements))
                print(f"Conjunto '{set_name}' creado exitosamente.")
            except ValueError as e:
                print(e)

        elif choice == '2':
            # Operar entre conjuntos
            print("Operaciones disponibles: complemento, unión, intersección, diferencia, diferencia simétrica")
            operation = input("Ingrese la operación que desea realizar: ").lower()
            set1 = input("Ingrese el nombre del primer conjunto: ")
            set2 = None
            set3 = None
            if operation in ["union", "interseccion", "diferencia", "diferencia simetrica"]:
                set2 = input("Ingrese el nombre del segundo conjunto: ")
                use_set3 = input("¿Desea operar con un tercer conjunto? (s/n): ").lower()
                if use_set3 == 's':
                    set3 = input("Ingrese el nombre del tercer conjunto: ")

            try:
                result = operations.operate_sets(operation, set1, set2, set3)
                print(f"Resultado de {operation}: {result}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            # Mostrar todos los conjuntos creados
            operations.display_sets()

        elif choice == '4':
            # Salir del programa
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejecutar el menú interactivo
display_menu()
