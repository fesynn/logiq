import random
from datetime import datetime


def generate_logs(n):
    levels = ["ERROR", "WARNING", "INFO"]
    services = ["auth-service", "user-service", "db-service"]
    messages = [
        "Usuário não encontrado",
        "Timeout na conexão com banco",
        "Token expirado"
    ]

    logs = []
    for i in range(n):
        log = {
            "id": i,
            "level": random.choice(levels),
            "service": random.choice(services),
            "message": random.choice(messages),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        logs.append(log)

    return logs

