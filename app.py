# Este é o conteúdo para o arquivo app.py

import os
import google.generativeai as genai
import textwrap
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

# --- PARTE 1: CONFIGURAÇÃO INICIAL ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    print("✅ Chave de API configurada com sucesso!")
else:
    print("⚠️ Atenção: Chave de API não encontrada no arquivo .env.")

# --- Inicializa o servidor Flask ---
app = Flask(__name__, template_folder='.')

# ==============================================================================
# PARTE 2: A CLASSE 'AGENTE'
# ==============================================================================
class Agente:
    def __init__(self, nome: str, system_instruction: str, model_name: str = "gemini-1.5-flash"):
        self.nome = nome
        self.system_instruction = textwrap.dedent(system_instruction)
        self.model = genai.GenerativeModel(model_name=model_name, system_instruction=self.system_instruction)
        print(f"🤖 Agente '{self.nome}' contratado e pronto para o trabalho!")

    def executar(self, tarefa: str, contexto: str = None) -> str:
        print(f"⏳ Agente '{self.nome}' iniciando tarefa...")
        prompt = f"TAREFA: {tarefa}"
        if contexto:
            prompt = f"CONTEXTO PARA REALIZAR A TAREFA:\n---\n{contexto}\n---\n\n{prompt}"
        try:
            response = self.model.generate_content(prompt)
            print(f"✅ Agente '{self.nome}' concluiu a tarefa!")
            return response.text
        except Exception as e:
            print(f"❌ Erro ao executar o agente '{self.nome}': {e}")
            return f"Erro: Não foi possível completar a tarefa. Motivo: {e}"

# ==============================================================================
# PARTE 3: A FÁBRICA DE AGENTES
# ==============================================================================
print("\n" + "="*80 + "\nINICIANDO A FÁBRICA DE AGENTES...\n" + "="*80)
meus_agentes = {
    "Analisador de Negócios": Agente(
        nome="Analisador de Negócios",
        system_instruction="""Você é um analista de negócios sênior. Sua única função é receber uma URL e descrever em um parágrafo conciso: 1. O modelo de negócio do site. 2. O público-alvo principal. 3. O propósito central ou o problema que ele resolve. Sua resposta deve ser apenas este parágrafo de análise."""
    ),
    "Engenheiro de UI/UX": Agente(
        nome="Engenheiro de UI/UX",
        system_instruction="""Você é um engenheiro de Front-end e especialista em UI/UX. Com base em um conceito de negócio (contexto), sua tarefa é listar os 5 a 7 componentes de interface e funcionalidades essenciais que um usuário veria e com os quais interagiria no site. Formate a resposta como uma lista de tópicos (bullet points)."""
    ),
    "Arquiteto de Back-End": Agente(
        nome="Arquiteto de Back-End",
        system_instruction="""Você é um arquiteto de software especializado em Back-end. Com base em uma lista de funcionalidades de front-end (contexto), sua tarefa é projetar os recursos de back-end necessários. Descreva: 1. Os principais modelos de dados (tabelas de banco de dados). 2. Os 3 ou 4 endpoints de API mais importantes (ex: GET /users, POST /items). Seja técnico e direto."""
    ),
    "Desenvolvedor de Conteúdo Didático": Agente(
        nome="Desenvolvedor de Conteúdo Didático",
        system_instruction="""Você é um educador de programação. Sua função é receber especificações de front-end e back-end (contexto) e transformá-las em um desafio de programação claro e estruturado. Organize a atividade em "Parte 1: Front-End" e "Parte 2: Back-End", detalhando as tarefas de forma lógica para um aluno. Sua resposta deve ser o rascunho da atividade."""
    ),
    "Revisor Pedagógico": Agente(
        nome="Revisor Pedagógico",
        system_instruction="""Você é um professor experiente com uma didática impecável. Sua tarefa é receber um rascunho de uma atividade de programação (contexto) e aprimorá-la. Seu trabalho é: 1. Simplificar a linguagem para torná-la mais clara e motivadora. 2. Formatar o texto perfeitamente usando títulos, listas e negrito para fácil leitura. 3. Adicionar uma seção "Conselho do Mestre" ao final de cada parte (Front-end e Back-end) com uma dica útil que não entregue a resposta."""
    )
}
print("\n" + "="*80 + f"\nFÁBRICA CONCLUÍDA: {len(meus_agentes)} agentes contratados.\n" + "="*80)

# ==============================================================================
# PARTE 4: ROTA DA API QUE ORQUESTRA OS AGENTES
# ==============================================================================
@app.route('/gerar-atividade', methods=['POST'])
def orquestrar_agentes():
    data = request.get_json()
    tarefa_inicial = data.get('url')
    if not tarefa_inicial:
        return jsonify({"erro": "URL não fornecida"}), 400
    print(f"\n🚀 Orquestração iniciada para a URL: {tarefa_inicial}")
    try:
        contexto_conceito = meus_agentes["Analisador de Negócios"].executar(tarefa=f"Analise a URL: {tarefa_inicial}")
        contexto_frontend = meus_agentes["Engenheiro de UI/UX"].executar(tarefa="Liste os componentes de UI/UX.", contexto=contexto_conceito)
        contexto_backend = meus_agentes["Arquiteto de Back-End"].executar(tarefa="Projete a API e os modelos de dados.", contexto=contexto_frontend)
        contexto_para_desafio = f"Especificações de Front-End:\n{contexto_frontend}\n\nEspecificações de Back-End:\n{contexto_backend}"
        contexto_rascunho = meus_agentes["Desenvolvedor de Conteúdo Didático"].executar(tarefa="Crie o desafio de programação.", contexto=contexto_para_desafio)
        atividade_final = meus_agentes["Revisor Pedagógico"].executar(tarefa="Revise e formate esta atividade.", contexto=contexto_rascunho)
        print("✅ Orquestração concluída com sucesso!")
        return jsonify({"resultado": atividade_final})
    except Exception as e:
        print(f"❌ Erro fatal durante a orquestração: {e}")
        return jsonify({"erro": str(e)}), 500

# ==============================================================================
# PARTE 5: ROTA PRINCIPAL QUE SERVE A PÁGINA WEB
# ==============================================================================
@app.route('/')
def index():
    return render_template('static/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)