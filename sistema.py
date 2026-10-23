import sqlite3
import os

# ==========================================
# MÓDULO 1. CREACIÓN DE LA BASE DE DATOS
# ==========================================

def crear_bd():
    os.makedirs("database", exist_ok=True)

    conexion = sqlite3.connect("database/empleados.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleado (
            curp TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            calle TEXT,
            colonia TEXT,
            tel_empleado TEXT
        )
    """)

    conexion.commit()
    conexion.close()

    print("Base de datos creada correctamente.")
    print("Base de datos creada con exito")


# ==========================================
# MÓDULO 2. ALTAS DE EMPLEADOS
# ==========================================

def alta_empleado():
    conexion = sqlite3.connect("database/empleados.db")
    cursor = conexion.cursor()

    print("\n===== ALTA DE EMPLEADO =====")

    curp = input("curp: ").strip()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    calle = input("Calle: ").strip()
    colonia = input("Colonia: ").strip()
    tel_empleado = input("Teléfono del empleado: ").strip()

    if not curp or not nombre or not apellido:
        print("Error: curp, nombre y apellido son obligatorios.")
        conexion.close()
        return

    try:
        cursor.execute("""
            INSERT INTO empleado (
                curp,
                nombre,
                apellido,
                calle,
                colonia,
                tel_empleado
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            curp,
            nombre,
            apellido,
            calle,
            colonia,
            tel_empleado
        ))

        conexion.commit()
        print("empleado registrado correctamente.")

    except sqlite3.IntegrityError:
        print("Error: la curp ya existe.")

    except sqlite3.Error as error:
        print(f"Error al registrar al empleado: {error}")

    finally:
        conexion.close()


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

if __name__ == "__main__":
    crear_bd()
    alta_empleado()