from dataclasses import dataclass

@dataclass
class Usuario:
    """Entidad principal del dominio."""
    correo: str
    password: str