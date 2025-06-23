# Expense Management System

Sistema de Gerenciamento de gastos

## Criar a virtualenv
```code
python -m venv .venv
OU
python3 -m venv .venv
``` 

## Acessar a virtualenv
```code
.venv\Scripts\activate
OU
source .venv\bin\activate
```

## Instalar as libs:
```code
pip install -r requirements.txt
```

## Criar o file .env
```bash
python contrib/env_gen.py
```

## Rode as migrations
```bash
  python manage.py migrate
```

## Criar um superuser
```bash
  python manage.py createsuperuser
```

## Rodar o app
```bash
  python manage.py runserver
```

### Será criado o **user** principal do sistema

Como início de sua aplicação são esses os passos.

![img](https://i.imgur.com/voalXAV.jpg)

![img](https://i.imgur.com/jqgeU9X.jpg)

Qualquer dúvida/críticas/melhorias crie uma issues no github
ou envie pelo e-mail: *contato@luxu.com.br*

That's all folks!