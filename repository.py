from models import Usuario
from typing import Optional

class UserRepository:
   """Clase encargada de guardar y buscar usuarios (Persistencia)."""
    
   def _init_(self):
      self._db = {}

   def guardar(self, usuario: Usuario) -> None:
      self._db[usuario.correo] = usuario
        
   def buscar_por_correo(self, correo: str) -> Optional[Usuario]:
      return self._db.get(correo)