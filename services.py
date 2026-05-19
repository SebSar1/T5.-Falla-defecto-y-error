from models import Usuario
from typing import List

class RegistrationService:
    """Caso de uso: Registro de usuarios (RF1)."""
    
    def __init__(self, repository):
        # Inyectamos el repositorio directamente
        self.repository = repository

    def registrar(self, correo: str, password: str) -> None:
        # ==========================================
        # FALLA 1: SOBRESCRITURA DE CUENTA
        # ==========================================
        # -> ERROR (Causa raíz/Humano): El desarrollador omitió en el análisis la regla de
        #    negocio que impide registrar correos duplicados.
        # -> DEFECTO (Bug en el código): Falta una condición `if self.repository.buscar_por_correo(correo):`
        #    para abortar el registro si el usuario ya existe.
        # -> FALLA (Comportamiento visible): Durante la ejecución, el sistema permite que un visitante 
        #    secuestre la cuenta de otro usuario sobrescribiendo su registro y contraseña.
        # ==========================================
        nuevo_usuario = Usuario(correo, password)
        self.repository.guardar(nuevo_usuario)
        print(f"[*] Registro: Usuario '{correo}' registrado exitosamente.")


class AuthenticationService:
    """Caso de uso: Inicio de sesión (RF2)."""
    
    def __init__(self, repository):
        self.repository = repository
        self.max_intentos = 3

    def iniciar_sesion(self, correo: str, contrasenas_simuladas: List[str] = None) -> bool:
        usuario = self.repository.buscar_por_correo(correo)
        if not usuario:
            print("[!] Auth: El correo no está registrado.")
            return False

        intentos = 0
        idx_simulacion = 0
        
        # ==========================================
        # FALLA 2: EXCESO DE INTENTOS PERMITIDOS
        # ==========================================
        # -> ERROR (Causa raíz/Humano): Error de lógica matemática "off-by-one" (desfasado por uno) 
        #    al pensar en los límites del bucle.
        # -> DEFECTO (Bug en el código): El operador relacional es incorrecto: `intentos <= self.max_intentos`
        #    permite una iteración adicional (0, 1, 2, 3). Debería ser estricto `<`.
        # -> FALLA (Comportamiento visible): Al ejecutar, el sistema otorga 4 intentos de acceso 
        #    al usuario, lo cual incumple directamente el RF2 que exige un máximo de 3.
        # ==========================================
        while intentos <= self.max_intentos:
            if contrasenas_simuladas:
                password_intento = contrasenas_simuladas[idx_simulacion]
                idx_simulacion += 1
            else:
                password_intento = input("Ingrese su contraseña: ")

            if usuario.password == password_intento:
                print("[*] Auth: Inicio de sesión exitoso. ¡Bienvenido a las funciones exclusivas!")
                return True
            else:
                intentos += 1
                print(f"[!] Auth: Credenciales incorrectas. Intento {intentos} fallido.")
        
        print("[-] Auth: Cuenta bloqueada temporalmente por exceder los intentos.")
        return False
