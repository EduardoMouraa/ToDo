# ToDo
Web lista de tarefas com Djando, Celery e Redis

# Pré-requisitos
Baixar lib's necessárias

   ```
    pip install -r requirements.txt
   ```

Criar na raíz do repositório o arquivo .env com as seguintes variáveis

   ```
    DEBUG=True
    SECRET_KEY=')4$zq0^_e)h0z7k3ytw$x%an(vu$-3v+mp)+xate_7novw^16r'

    SECURE_SSL_REDIRECT=True
    SESSION_COOKIE_SECURE=True
    CSRF_COOKIE_SECURE=True

    HOST='smtp.gmail.com'
    PORT=587
    USERNAME='EMAIL_GMAIL'
    PASSWORD='PASSWORD_APP_GMAIL'

    DATABASE_URL="postgres://postgres:postgres@postdb:5432/postgres"
   ```

 # Docker-compose
 para uma visualização rápida, baixar docker-compose e executar o seguinte comando
    
   ```
    docker-compose up
   ```
