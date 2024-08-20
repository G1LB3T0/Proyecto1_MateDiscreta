class SetOperations:
    def __init__(self):
        # Usamos un diccionario para almacenar matrices que representan los conjuntos y sus elementos en el orden ingresado
        self.conjuntos = {}

    def create_set(self, set_name, elements):
        if set_name in self.conjuntos:
            raise ValueError(f"El conjunto '{set_name}' ya existe.")
        validated_elements = self._validate_elements(elements)
        self.conjuntos[set_name] = {
            "matrix": self._convert_to_matrix(validated_elements),
            "order": elements
        }

    def operate_sets(self, operation, set1, set2=None):
        if set1 not in self.conjuntos:
            raise ValueError(f"El conjunto '{set1}' no existe.")
        if set2 and set2 not in self.conjuntos:
            raise ValueError(f"El conjunto '{set2}' no existe.")

        if operation == "complemento":
            return self._complement(set1)
        elif operation == "union":
            return self._union(set1, set2)
        elif operation == "interseccion":
            return self._intersection(set1, set2)
        elif operation == "diferencia":
            return self._difference(set1, set2)
        elif operation == "diferencia simetrica":
            return self._symmetric_difference(set1, set2)
        else:
            raise ValueError("Operacion no valida. Las operaciones validas son: complemento, union, interseccion, diferencia, diferencia simetrica.")

    def _validate_elements(self, elements):
        valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for element in elements:
            if element not in valid_characters:
                raise ValueError(f"Elemento '{element}' no valido. Solo se permiten letras A-Z y digitos 0-9.")
        return elements

    def _convert_to_matrix(self, elements):
        matrix = [0] * 36  # Matriz de tamaño 36 (26 letras + 10 digitos)
        valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for element in elements:
            index = valid_characters.index(element)
            matrix[index] = 1
        return matrix

    def _complement(self, set_name):
        universal_set = [1] * 36  # Conjunto universal
        result = []
        for i in range(36):
            result.append(1 if self.conjuntos[set_name]["matrix"][i] == 0 else 0)
        return self._matrix_to_set(result)

    def _union(self, set1, set2):
        result = []
        for i in range(36):
            if self.conjuntos[set1]["matrix"][i] == 1 or self.conjuntos[set2]["matrix"][i] == 1:
                result.append(1)
            else:
                result.append(0)
        return self._matrix_to_set(result)

    def _intersection(self, set1, set2):
        #Esta funcion lo que hace es comparar 
        result = []
        for i in range(36):
            if self.conjuntos[set1]["matrix"][i] == 1 and self.conjuntos[set2]["matrix"][i] == 1:
                result.append(1)
            else:
                result.append(0)
        return self._matrix_to_set(result)

    def _difference(self, set1, set2):
        result = []
        for i in range(36):
            if self.conjuntos[set1]["matrix"][i] == 1 and self.conjuntos[set2]["matrix"][i] == 0:
                result.append(1)
            else:
                result.append(0)
        return self._matrix_to_set(result)

    def _symmetric_difference(self, set1, set2):
        result = []
        for i in range(36):
            if self.conjuntos[set1]["matrix"][i] != self.conjuntos[set2]["matrix"][i]:
                result.append(1)
            else:
                result.append(0)
        return self._matrix_to_set(result)

    def _matrix_to_set(self, matrix):
        valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        result_set = []
        for i in range(36):
            if matrix[i] == 1:
                result_set.append(valid_characters[i])
        return result_set

    def display_sets(self):
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
        choice = input("Seleccione una opcion: ")

        if choice == '1':
            set_name = input("Ingrese el nombre del conjunto: ")
            elements = input("Ingrese los elementos del conjunto (sin espacios, ej: ABC123): ")
            try:
                operations.create_set(set_name, list(elements))
                print(f"Conjunto '{set_name}' creado exitosamente.")
            except ValueError as e:
                print(e)

        elif choice == '2':
            print("Operaciones disponibles: complemento, union, interseccion, diferencia, diferencia simetrica")
            operation = input("Ingrese la operacion que desea realizar: ").lower()
            set1 = input("Ingrese el nombre del primer conjunto: ")
            set2 = None
            if operation in ["union", "interseccion", "diferencia", "diferencia simetrica"]:
                set2 = input("Ingrese el nombre del segundo conjunto: ")

            try:
                result = operations.operate_sets(operation, set1, set2)
                print(f"Resultado de {operation}: {result}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            operations.display_sets()

        elif choice == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida, por favor intente de nuevo.")

# Ejecutar el menu interactivo
display_menu()
