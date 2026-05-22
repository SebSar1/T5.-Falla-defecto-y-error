# <center> **ESCUELA POLITÉCNICA NACIONAL** </center>

**Integrantes**

* ANRANGO STALIN
* ARÍZAGA SAMIRA
* BETANCOURT ALISON
* DÁVILA PAÚL
* RAMOS SEBASTIÁN
* SARASTI SEBASTIAN

# T5: Falla, defecto y error - Módulo de Autenticación

*Institución:* Escuela Politécnica Nacional (EPN)

Este repositorio contiene la resolución del problema propuesto para el desarrollo de un módulo de registro e inicio de sesión. El proyecto está estructurado en múltiples capas para separar responsabilidades y demuestra de forma práctica los conceptos fundamentales de control de calidad y pruebas de software.

## Problema Planteado
Se propone desarrollar el módulo de registro e inicio de sesión a un sistema en cualquier lenguaje.

* **RF1:** Como visitante del sistema, quiero registrarme creando una cuenta con mi correo y contraseña, para acceder a las funciones exclusivas de la plataforma.
* **RF2:** Como usuario quiero tener tres intentos para iniciar sesión con mis credenciales de usuario para acceder al sistema.

## Introducción de Fallos, Defectos y Errores
El módulo introduce a propósito los conceptos solicitados, implementando dos fallas principales en la capa de servicios (`services.py`):

### Falla 1: Sobrescritura de cuenta (Registro)
* **Error (Causa raíz):** El desarrollador omitió en el análisis la regla de negocio implícita que impide registrar correos duplicados.
* **Defecto (Bug):** Falta una condición de validación en el código para verificar si el usuario ya existe antes de guardarlo en el repositorio.
* **Fallo (Comportamiento visible):** El sistema permite que un visitante secuestre la cuenta de otro usuario sobrescribiendo su registro y contraseña.

### Falla 2: Exceso de intentos permitidos (Login)
* **Error (Causa raíz):** Error de lógica matemática "off-by-one" (desfasado por uno) al plantear los límites del bucle de intentos.
* **Defecto (Bug):** El operador relacional en el bucle `while` es incorrecto (`<=` en lugar de `<`), permitiendo una iteración adicional.
* **Fallo (Comportamiento visible):** El sistema otorga 4 intentos de acceso al usuario, incumpliendo directamente el RF2 que exige un máximo de 3.
