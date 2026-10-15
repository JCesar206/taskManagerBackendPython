from datetime import date
from app.database import SessionLocal
from app.models import User, Task
from app.security import hash_password

def run():
    with SessionLocal() as db:
        user = User(email="demo@example.com", password_hash=hash_password("Demo12345"))
        db.add(user)
        db.flush()

        db.add_all([
            Task(user_id=user.id, title="Configurar entorno",
                 description="Instalar Python y dependencias",
                 status="done", priority="high", due_date=date(2026, 10, 15)),
            Task(user_id=user.id, title="Crear la API",
                 description="Endpoints CRUD de tareas",
                 status="in_progress", priority="high", due_date=date(2026, 10, 17)),
            Task(user_id=user.id, title="Conectar el frontend",
                 description="Consumir la API desde React",
                 status="pending", priority="medium", due_date=date(2026, 10, 20)),
            Task(user_id=user.id, title="Revisar estilos",
                 status="pending", priority="low"),
        ])
        db.commit()
        print("Seed listo: demo@example.com / Demo12345")

if __name__ == "__main__":
    run()