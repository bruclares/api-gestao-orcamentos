# run.py
from src import create_app

# Cria a instância da aplicação usando a factory
app = create_app()

if __name__ == "__main__":
    # Roda o servidor de desenvolvimento do Flask (não usado pelo Gunicorn)
    app.run(host="0.0.0.0", port=5000)
