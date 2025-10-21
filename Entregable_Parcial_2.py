
#Entregable parcial corte 2 de Programación 1
#Juan Camilo Impata Aguirre

def calculadora_cientifica(operacion, a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Los parametros deben ser numericos (int o float)")

    operaciones_validas = {
        "suma": lambda x, y: x + y,
        "resta": lambda x, y: x - y,
        "multiplicacion": lambda x, y: x * y,
        "division": lambda x, y: x / y,
        "potencia": lambda x, y: x ** y,
        "residuo": lambda x, y: x % y
    }

    if operacion not in operaciones_validas:
        raise ValueError(
            f"Operacion invalida: '{operacion}'. Operaciones validas: suma, resta, multiplicacion, division, potencia, residuo"
        )

    if operacion in ("division", "residuo") and b == 0:
        raise ZeroDivisionError(f"No se puede realizar {operacion} por cero")

    return round(operaciones_validas[operacion](a, b), 2)



class ValidadorPassword:
    def __init__(self, min_longitud=8, requiere_mayuscula=True,
                 requiere_minuscula=True, requiere_numero=True,
                 requiere_especial=True):
        self.min_longitud = min_longitud
        self.requiere_mayuscula = requiere_mayuscula
        self.requiere_minuscula = requiere_minuscula
        self.requiere_numero = requiere_numero
        self.requiere_especial = requiere_especial
        self.caracteres_especiales = set("!@#$%^&*()_+-=[]{}|;:,.<>?/")

    def validar(self, password):
        errores = []
        if len(password) < self.min_longitud:
            errores.append(f"Longitud minima no cumplida (minimo {self.min_longitud} caracteres)")
        if self.requiere_mayuscula and not any(c.isupper() for c in password):
            errores.append("Falta al menos una letra mayuscula")
        if self.requiere_minuscula and not any(c.islower() for c in password):
            errores.append("Falta al menos una letra minuscula")
        if self.requiere_numero and not any(c.isdigit() for c in password):
            errores.append("Falta al menos un numero")
        if self.requiere_especial and not any(c in self.caracteres_especiales for c in password):
            errores.append("Falta al menos un caracter especial")
        if errores:
            return (False, errores)
        else:
            return (True, [])

    def es_fuerte(self, password):
        return (
            len(password) >= 12
            and any(c.isupper() for c in password)
            and any(c.islower() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in self.caracteres_especiales for c in password)
        )


class GestorInventario:
    def __init__(self):
        self.inventario = []

    def agregar_producto(self, codigo, nombre, precio, cantidad):
        for p in self.inventario:
            if p[0] == codigo:
                raise ValueError("El codigo ya existe")
        if precio < 0 or cantidad < 0:
            raise ValueError("Precio o cantidad invalidos")
        self.inventario.append((codigo, nombre, float(precio), int(cantidad)))

    def mostrar_inventario(self):
        if not self.inventario:
            print("No hay productos en el inventario")
        else:
            print("Codigo | Nombre | Precio | Cantidad")
            for p in self.inventario:
                print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]}")

    def actualizar_stock(self, codigo, cantidad_cambio):
        for i, p in enumerate(self.inventario):
            if p[0] == codigo:
                nuevo = p[3] + cantidad_cambio
                if nuevo < 0:
                    raise ValueError("Stock resultante negativo")
                self.inventario[i] = (p[0], p[1], p[2], nuevo)
                return
        raise ValueError("El producto no existe")

    def productos_bajo_stock(self, limite=10):
        bajos = [p for p in self.inventario if p[3] < limite]
        if not bajos:
            print("No hay productos bajo el limite")
        else:
            for p in bajos:
                print(f"{p[1]} tiene solo {p[3]} unidades")

    def valor_total_inventario(self):
        if not self.inventario:
            print("No hay productos en el inventario")
            return 0
        total = sum(p[2] * p[3] for p in self.inventario)
        print("Valor total del inventario:", total)
        return total



def es_bisiesto(anio): ...
def dias_en_mes(mes, anio): ...
def generar_calendario(mes, anio, dia_inicio=0): ...
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_mes(mes, anio):
    if mes < 1 or mes > 12:
        raise ValueError("Mes invalido")
    dias_por_mes = [31, 29 if es_bisiesto(anio) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dias_por_mes[mes - 1]

def generar_calendario(mes, anio, dia_inicio=0):
    if dia_inicio < 0 or dia_inicio > 6:
        dia_inicio = dia_inicio % 7
    dias = dias_en_mes(mes, anio)
    encabezado = "Lu Ma Mi Ju Vi Sa Do"
    calendario = [encabezado]
    fila = "   " * dia_inicio
    for dia in range(1, dias + 1):
        fila += f"{dia:2d} "
        if (dia + dia_inicio) % 7 == 0 or dia == dias:
            calendario.append(fila.rstrip())
            fila = ""
    return "\n".join(calendario)

def ejecutar_calendario():
    try:
        mes = int(input("Ingresa el mes (1-12): "))
        anio = int(input("Ingresa el anio: "))
        dia_inicio = int(input("Ingresa el dia de inicio (0=Lunes, 6=Domingo): "))
        print()
        print("Calendario del mes solicitado:\n")
        print(generar_calendario(mes, anio, dia_inicio))
    except ValueError as e:
        print("Error:", e)

def analizar_ventas(ventas): ...
def encontrar_patrones(ventas): ...
def simular_crecimiento(ventas, porcentaje, meses): ...
def analizar_ventas(ventas):
    if not ventas:
        raise ValueError("Lista vacia")
    return {
        "promedio": round(sum(ventas) / len(ventas), 2),
        "maximo": max(ventas),
        "minimo": min(ventas),
        "total": round(sum(ventas), 2)
    }

def encontrar_patrones(ventas):
    if not ventas:
        return "sin datos"
    if all(ventas[i] < ventas[i + 1] for i in range(len(ventas) - 1)):
        return "creciente"
    if all(ventas[i] > ventas[i + 1] for i in range(len(ventas) - 1)):
        return "decreciente"
    if all(ventas[i] == ventas[0] for i in range(len(ventas))):
        return "estable"
    return "variable"

def simular_crecimiento(ventas, porcentaje, meses):
    if not ventas:
        raise ValueError("Lista vacia")
    if meses <= 0:
        return ventas
    proyeccion = ventas[:]
    valor_actual = ventas[-1]
    for _ in range(meses):
        valor_actual *= (1 + porcentaje / 100)
        proyeccion.append(round(valor_actual, 2))
    return proyeccion





    class LibroNoDisponibleError(Exception):
        pass

class UsuarioNoRegistradoError(Exception):
    pass

class SistemaBiblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []


class SistemaBiblioteca:
    class LibroNoDisponibleError(Exception):
        pass

    class UsuarioNoRegistradoError(Exception):
        pass

class SistemaBiblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    

    def registrar_libro(self, codigo, titulo, autor, cantidad):
        for l in self.libros:
            if l[0] == codigo:
                print("El libro ya existe")
                return
        self.libros.append((codigo, titulo, autor, int(cantidad)))
        print(f"Libro '{titulo}' agregado con exito")

    def registrar_usuario(self, id_usuario, nombre):
        for u in self.usuarios:
            if u[0] == id_usuario:
                print("El usuario ya existe")
                return
        self.usuarios.append((id_usuario, nombre, []))
        print(f"Usuario '{nombre}' registrado con exito")

    def buscar_libro(self, termino):
        resultados = [l for l in self.libros if termino.lower() in l[1].lower() or termino.lower() in l[2].lower()]
        if not resultados:
            print("No se encontraron libros")
        else:
            for l in resultados:
                print(f"{l[0]} - {l[1]} ({l[2]}) - Cantidad: {l[3]}")

    def mostrar_disponibles(self):
        disponibles = [l for l in self.libros if l[3] > 0]
        if not disponibles:
            print("No hay libros disponibles")
        else:
            for l in disponibles:
                print(f"{l[0]} - {l[1]} ({l[2]}) - {l[3]} disponibles")

    def prestar_libro(self, id_usuario, codigo_libro):
        usuario = next((u for u in self.usuarios if u[0] == id_usuario), None)
        if not usuario:
            raise UsuarioNoRegistradoError("El usuario no esta registrado")
        libro_index = next((i for i, l in enumerate(self.libros) if l[0] == codigo_libro), None)
        if libro_index is None:
            print("El libro no existe")
            return
        codigo, titulo, autor, cantidad = self.libros[libro_index]
        if cantidad <= 0:
            raise LibroNoDisponibleError("El libro no esta disponible")
        self.libros[libro_index] = (codigo, titulo, autor, cantidad - 1)
        for i, u in enumerate(self.usuarios):
            if u[0] == id_usuario:
                self.usuarios[i][2].append(codigo)
        print(f"Libro '{titulo}' prestado a {usuario[1]}")

    def devolver_libro(self, id_usuario, codigo_libro):
        usuario_index = next((i for i, u in enumerate(self.usuarios) if u[0] == id_usuario), None)
        if usuario_index is None:
            raise UsuarioNoRegistradoError("El usuario no esta registrado")
        libro_index = next((i for i, l in enumerate(self.libros) if l[0] == codigo_libro), None)
        if libro_index is None:
            print("El libro no existe")
            return
        codigo, titulo, autor, cantidad = self.libros[libro_index]
        self.libros[libro_index] = (codigo, titulo, autor, cantidad + 1)
        if codigo_libro in self.usuarios[usuario_index][2]:
            self.usuarios[usuario_index][2].remove(codigo_libro)
        print(f"Libro '{titulo}' devuelto por {self.usuarios[usuario_index][1]}")

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados")
        else:
            for u in self.usuarios:
                libros = ", ".join(u[2]) if u[2] else "ninguno"
                print(f"{u[0]} - {u[1]} - Libros prestados: {libros}")



    ...

def main():
    print("==== MENU PRINCIPAL ====")
    print("1. Calculadora cientifica")
    print("2. Validador de contrasenas")
    print("3. Gestor de inventario")
    print("4. Calendario")
    print("5. Analisis de ventas")
    print("6. Sistema de biblioteca")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        operacion = input("Operacion (suma, resta, multiplicacion, division, potencia, residuo): ")
        try:
            a = float(input("Ingresa el primer numero: "))
            b = float(input("Ingresa el segundo numero: "))
            print("Resultado:", calculadora_cientifica(operacion, a, b))
        except ValueError as e:
            print("Error:", e)
        except ZeroDivisionError as e:
            print("Error:", e)

    elif opcion == "2":
        validador = ValidadorPassword(min_longitud=8)
        password = input("Ingresa una contrasena: ")
        valido, errores = validador.validar(password)
        if valido:
            print("Contrasena valida")
            if validador.es_fuerte(password):
                print("La contrasena es fuerte")
            else:
                print("La contrasena no es fuerte")
        else:
            print("Contrasena invalida:")
            for e in errores:
                print("-", e)

    elif opcion == "3":
        inv = GestorInventario()
        inv.mostrar_inventario()
        inv.agregar_producto("P1", "Mouse", 45000, 8)
        inv.agregar_producto("P2", "Teclado", 80000, 3)
        inv.agregar_producto("P3", "Monitor", 250000, 2)
        print()
        inv.mostrar_inventario()
        print()
        inv.actualizar_stock("P1", -3)
        inv.mostrar_inventario()
        print()
        inv.productos_bajo_stock(5)
        print()
        inv.valor_total_inventario()

    elif opcion == "4":
        ejecutar_calendario()

    elif opcion == "5":
        ventas = [1200, 1350, 1400, 1600, 2000]
        print("Analisis de ventas:", analizar_ventas(ventas))
        print("Patron:", encontrar_patrones(ventas))
        print("Proyeccion:", simular_crecimiento(ventas, 10, 3))

    elif opcion == "6":
        sistema = SistemaBiblioteca()
        sistema.registrar_libro("L1", "1984", "George Orwell", 3)
        sistema.registrar_libro("L2", "Cien anos de soledad", "Gabriel Garcia Marquez", 2)
        sistema.registrar_libro("L3", "El principito", "Antoine de Saint-Exupery", 0)
        sistema.registrar_usuario("U1", "Camilo")
        sistema.registrar_usuario("U2", "Laura")
        print()
        print("Libros disponibles:")
        sistema.mostrar_disponibles()
        print()
        sistema.buscar_libro("soledad")
        print()
        try:
            sistema.prestar_libro("U1", "L1")
            sistema.prestar_libro("U2", "L3")
        except (LibroNoDisponibleError, UsuarioNoRegistradoError) as e:
            print("Error:", e)
        print()
        sistema.mostrar_disponibles()
        print()
        sistema.devolver_libro("U1", "L1")
        sistema.mostrar_disponibles()
        print()
        sistema.mostrar_usuarios()

    else:
        print("Opcion no valida")



if __name__ == "__main__":
    main()