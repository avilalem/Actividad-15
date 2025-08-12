def pedir_entero(mensaje, minimo=None, maximo=None, permitir_cancelar=True):
    while True:
        entrada = input(mensaje).strip()
        if permitir_cancelar and entrada.lower() in ("salir", "cancelar"):
            return None
        try:
            valor = int(entrada)
            if minimo is not None and valor < minimo:
                print(f"Por favor ingrese un número mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Por favor ingrese un número menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida, por favor ingrese un número válido.")

def pedir_float(mensaje, minimo=None, maximo=None, permitir_cancelar=True):
    while True:
        entrada = input(mensaje).strip()
        if permitir_cancelar and entrada.lower() in ("salir", "cancelar"):
            return None
        try:
            valor = float(entrada)
            if minimo is not None and valor < minimo:
                print(f"Por favor ingrese un número mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Por favor ingrese un número menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida, por favor ingrese un número válido.")

def pedir_texto(mensaje, permitir_cancelar=True):
    while True:
        entrada = input(mensaje).strip()
        if permitir_cancelar and entrada.lower() in ("salir", "cancelar"):
            return None
        if entrada == "":
            print("Este campo no puede estar vacío.")
            continue
        return entrada

def registrar_estudiantes(estudiantes):
    print("\n--- Registrar Estudiantes ---")
    cantida = pedir_entero("Cuántos estudiantes desea ingresar? (escriba 'salir' para cancelar): ", minimo=1)
    if cantida is None:
        print("Registro cancelado. Regresando al menú principal.")
        return

    for _ in range(cantida):
        carnet = pedir_texto("Carnet: ")
        if carnet is None:
            print("Registro cancelado. Regresando al menú principal.")
            return
        if carnet in estudiantes:
            print("El carnet ingresado ya existe. Intente nuevamente")
            continue

        nombre = pedir_texto("Nombre: ")
        if nombre is None:
            print("Registro cancelado. Regresando al menú principal.")
            return

        edad = pedir_entero("Edad: ", minimo=1)
        if edad is None:
            print("Registro cancelado. Regresando al menú principal.")
            return

        carrera = pedir_texto("Carrera: ")
        if carrera is None:
            print("Registro cancelado. Regresando al menú principal.")
            return

        num_cursos = pedir_entero("Cantidad de cursos: ", minimo=0)
        if num_cursos is None:
            print("Registro cancelado. Regresando al menú principal.")
            return

        cursos = {}
        for i in range(num_cursos):
            print(f"\nCurso {i+1}:")
            nombre_curso = pedir_texto("Nombre Curso: ")
            if nombre_curso is None:
                print("Registro cancelado. Regresando al menú principal.")
                return

            tarea = pedir_float("Nota de tarea (0-100): ", minimo=0, maximo=100)
            if tarea is None:
                print("Registro cancelado. Regresando al menú principal.")
                return

            parcial = pedir_float("Nota de parcial (0-100): ", minimo=0, maximo=100)
            if parcial is None:
                print("Registro cancelado. Regresando al menú principal.")
                return

            proyecto = pedir_float("Nota de proyecto (0-100): ", minimo=0, maximo=100)
            if proyecto is None:
                print("Registro cancelado. Regresando al menú principal.")
                return

            cursos[nombre_curso] = {
                "tarea": tarea,
                "parcial": parcial,
                "proyecto": proyecto
            }

        estudiantes[carnet] = {
            "nombre": nombre,
            "edad": edad,
            "carrera": carrera,
            "cursos": cursos
        }
        print(f"Estudiante '{nombre}' registrado correctamente.\n")

def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("\nLista de estudiantes:")
    for carnet, datos in estudiantes.items():
        print(f"\nCarnet: {carnet} - Nombre: {datos['nombre']} - Edad: {datos['edad']} - Carrera: {datos['carrera']}")
        cursos = datos.get("cursos", {})
        if cursos:
            for curso, notas in cursos.items():
                print(f"Curso: {curso}")
                print(f"  Nota de tarea: {notas['tarea']}")
                print(f"  Nota de parcial: {notas['parcial']}")
                print(f"  Nota de proyecto: {notas['proyecto']}")
        else:
            print("No tiene cursos registrados.")

def buscar_carnet(estudiantes):
    carnet = pedir_texto("Ingrese el número de carnet que desea buscar (o 'salir' para cancelar): ")
    if carnet is None:
        print("Búsqueda cancelada. Regresando al menú principal.")
        return
    estudiante = estudiantes.get(carnet)
    if estudiante:
        print(f"\nNombre: {estudiante['nombre']} - Edad: {estudiante['edad']} - Carrera: {estudiante['carrera']}")
        cursos = estudiante.get("cursos", {})
        if cursos:
            for curso, notas in cursos.items():
                promedio = (notas['tarea'] + notas['parcial'] + notas['proyecto']) / 3
                print(f"Curso: {curso}")
                print(f"  Nota de tarea: {notas['tarea']}")
                print(f"  Nota de parcial: {notas['parcial']}")
                print(f"  Nota de proyecto: {notas['proyecto']}")
                print(f"  Promedio: {promedio:.2f}")
        else:
            print("No tiene cursos registrados.")
    else:
        print("No se encontró ningún estudiante con ese carnet.")

def menu():
    estudiantes = {}
    while True:
        print("\n ___ Menú Principal ___")
        print("1. Registrar Estudiantes")
        print("2. Mostrar Estudiantes y Cursos")
        print("3. Buscar Estudiante por Carnet")
        print("4. Salir (o escriba 'salir' en cualquier momento)")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_estudiantes(estudiantes)
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        elif opcion == "3":
            buscar_carnet(estudiantes)
        elif opcion == "4":
            print("Gracias por usar el programa!")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")

menu()
