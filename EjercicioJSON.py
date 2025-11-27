import json

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo} | Autor: {self.autor} | ISBN: {self.isbn} | Estado: **{estado}**"

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "disponible": self.disponible
        }

class Biblioteca:

    def __init__(self, nombre_archivo="biblioteca_data.json"):
        self.libros = {}
        self.nombre_archivo = nombre_archivo
        self.cargar_libros()

    def añadir_libro(self, libro: Libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"\nLibro '{libro.titulo}' añadido con éxito.")
            self.guardar_libros()
        else:
            print(f"\nERROR: El libro con ISBN {libro.isbn} ya existe.")

    def prestar_libro(self, isbn: str):
        if isbn in self.libros:
            libro = self.libros[isbn]
            if libro.disponible:
                libro.disponible = False
                print(f"\nLibro '{libro.titulo}' prestado. ¡Disfrútalo!")
                self.guardar_libros()
            else:
                print(f"\nERROR: El libro '{libro.titulo}' ya está prestado.")
        else:
            print(f"\nERROR: No se encontró el libro con ISBN {isbn}.")

    def devolver_libro(self, isbn: str):
        if isbn in self.libros:
            libro = self.libros[isbn]
            if not libro.disponible:
                libro.disponible = True
                print(f"\nLibro '{libro.titulo}' devuelto. ¡Gracias!")
                self.guardar_libros()
            else:
                print(f"\nERROR: El libro '{libro.titulo}' ya estaba disponible.")
        else:
            print(f"\nERROR: No se encontró el libro con ISBN {isbn}.")

    def mostrar_disponibles(self):
        disponibles = [libro for libro in self.libros.values() if libro.disponible]

        print("\n---Libros Disponibles ---")
        if disponibles:
            for libro in disponibles:
                print(f"* {libro}")
        else:
            print("No hay libros disponibles en este momento.")


    def guardar_libros(self):
        datos_a_guardar = [libro.to_dict() for libro in self.libros.values()]
        try:
            with open(self.nombre_archivo, 'w', encoding='utf-8') as f:
                json.dump(datos_a_guardar, f, indent=4)
        except IOError as e:
            print(f"Error al guardar los datos: {e}")

    def cargar_libros(self):
        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as f:
                datos_cargados = json.load(f)
                for data in datos_cargados:
                    libro = Libro(**data)
                    self.libros[libro.isbn] = libro
            print(f"**Datos cargados** desde '{self.nombre_archivo}' ({len(self.libros)} libros).")
        except FileNotFoundError:
            print(f"Archivo '{self.nombre_archivo}' no encontrado. Se inicia con una **colección vacía**.")
        except json.JSONDecodeError:
            print("ERROR: El archivo JSON está corrupto o vacío.")
        except IOError as e:
            print(f"Error al cargar los datos: {e}")


if __name__ == "__main__":
    biblioteca = Biblioteca()

    print("\n--- 1. Añadiendo Libros ---")
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-8437604947")
    libro2 = Libro("El código Da Vinci", "Dan Brown", "978-0307474278")
    libro3 = Libro("Python para Dummies", "Stephen Lott", "978-1119547372")

    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    biblioteca.mostrar_disponibles()

    print("\n--- 2. Prestando Libros ---")
    biblioteca.prestar_libro("978-8437604947")
    biblioteca.prestar_libro("978-1119547372")
    biblioteca.prestar_libro("978-8437604947")

    biblioteca.mostrar_disponibles()

    print("\n--- 3. Devolviendo Libros ---")
    biblioteca.devolver_libro("978-8437604947")
    biblioteca.devolver_libro("978-8437604947")

    biblioteca.mostrar_disponibles()

    print("\nEl sistema ha terminado. Los datos se han persistido automáticamente.")