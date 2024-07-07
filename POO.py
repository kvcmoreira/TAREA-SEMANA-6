# Clase base Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self._nombre = nombre  # atributo encapsulado
        self._salario = salario  # atributo encapsulado

    # Método para mostrar la información del empleado
    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Salario: {self._salario}"

    # Método para calcular el bono (polimorfismo: se sobrescribirá en clases derivadas)
    def calcular_bonus(self):
        return self._salario * 0.50

# Clase derivada Desarrollador
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self._lenguaje = lenguaje  # atributo encapsulado

    # Método sobrescrito para mostrar la información del desarrollador
    def mostrar_info(self):
        info = super().mostrar_info()
        return f"{info}, Lenguaje: {self._lenguaje}"

    # Método sobrescrito para calcular el bono del desarrollador
    def calcular_bonus(self):
        return self._salario * 0.60

# Clase derivada Gerente
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self._departamento = departamento  # atributo encapsulado

    # Método sobrescrito para mostrar la información del gerente
    def mostrar_info(self):
        info = super().mostrar_info()
        return f"{info}, Departamento: {self._departamento}"

    # Método sobrescrito para calcular el bono del gerente
    def calcular_bonus(self):
        return self._salario * 0.75

# Función principal para ejecutar el programa
def main():
    # Creación de instancias y uso de métodos
    empleado1 = Empleado("ANTONIO", 4000)
    desarrollador1 = Desarrollador("ANA MARIA", 5000, "Python")
    gerente1 = Gerente("JORGE", 6000, "Ventas")

    # Mostrando información de los empleados
    print(empleado1.mostrar_info())  # Nombre: ANTONIO, Salario: 4000
    print(desarrollador1.mostrar_info())  # Nombre: ANA MARIA , Salario: 5000, Lenguaje: Python
    print(gerente1.mostrar_info())  # Nombre: JORGE, Salario: 6000, Departamento: Ventas

    # Polimorfismo: calcular_bonus para diferentes tipos de empleados
    for empleado in (empleado1, desarrollador1, gerente1):
        print(f"Bonus de {empleado._nombre}: {empleado.calcular_bonus()}")

if __name__ == "__main__":
    main()
