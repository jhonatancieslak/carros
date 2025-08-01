# 🚗 Catálogo de Carros

Um sistema web completo desenvolvido com **Django**, ideal para gerenciar e divulgar carros disponíveis para venda em revendas ou lojas. Com foco no backend, o projeto oferece uma solução robusta, moderna e eficiente para exibir o inventário de veículos.

---

## ✨ Funcionalidades Principais

- **🔐 Autenticação de Usuários:** Cadastro e login seguros para gerenciamento de acesso.
- **🛠️ CRUD de Veículos:** Criação, leitura, atualização e exclusão de veículos com interface intuitiva.
- **📦 Gestão de Inventário com Signals:** Uso de *signals* do Django para atualizar automaticamente o status e a quantidade dos veículos.
- **📋 Listagem e Detalhes dos Veículos:** Catálogo responsivo com fotos, marca, modelo, ano, valor e página de detalhes para cada carro.
- **🔎 Sistema de Busca:** Pesquisa eficiente com múltiplos filtros para facilitar a navegação.
- **🧠 Geração Automática de Descrição com OpenAI:** Se o usuário não preencher a descrição do veículo, o sistema pode gerar uma bio automática e criativa usando a API da OpenAI.
- **📱 Design Responsivo:** Layout adaptado para desktop, tablet e smartphone.

---

## 🛠️ Tecnologias Utilizadas

### Backend
- Python
- Django

### Frontend
- HTML5
- CSS3
- JavaScript

### Banco de Dados
- PostgreSQL (produção)
- SQLite (desenvolvimento local)

### Integrações
- API da OpenAI

---

## 🚀 Como Executar o Projeto Localmente

### 🔧 Pré-requisitos
- Python 3.9 ou superior
- Pip (gerenciador de pacotes do Python)

### 1. Clonar o Repositório

```bash
git clone https://github.com/jhonatancieslak/catalogo-de-carros.git
cd catalogo-de-carros

2. Criar e Ativar Ambiente Virtual

python -m venv venv
# Ativar:
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

3. Instalar Dependências
pip install -r requirements.txt

4. Configurar Variáveis de Ambiente
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


API da OpenAI (em openai_api/client.py):
api_key = "SUA_API_KEY_DA_OPENAI_AQUI"

5. Aplicar Migrações
python manage.py migrate


☁️ Deploy na AWS (Sugestões)
Este projeto pode ser facilmente implantado em serviços AWS com boas práticas:

Variáveis de Ambiente: Nunca inclua senhas no código. Use ferramentas como AWS Secrets Manager ou arquivos .env.

Arquivos Estáticos: Configure o Django para servir arquivos estáticos via Amazon S3.

Banco de Dados: Use o Amazon RDS com PostgreSQL.

Serviços de Deploy: AWS Elastic Beanstalk, ECS (Docker), EC2 ou plataformas como Heroku e Railway também são compatíveis.

📄 Licença
Este projeto está licenciado sob a Licença MIT.

👤 Autor
Desenvolvido por Jhonatan Cieslak

