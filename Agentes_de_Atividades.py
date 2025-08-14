# --- AGENTE 11: TECNOLOGIAS DE SITE FULL STACK ---
meus_agentes["Tecnologias Full Stack"] = Agente(
    nome="Tecnologias Full Stack",
    system_instruction="""
        Você é um especialista em desenvolvimento web full stack. Gere uma lista das principais tecnologias usadas para criar um site completo (front-end, back-end, banco de dados, autenticação, hospedagem, testes, etc). Para cada tecnologia, explique de forma simples o que ela faz e por que é importante no contexto de um projeto moderno.
        Formate como uma lista com nome da tecnologia, breve explicação e exemplos de uso.
    """
)
# --- AGENTE 7: EXEMPLOS PRÁTICOS ---
meus_agentes["Exemplos Práticos"] = Agente(
    nome="Exemplos Práticos",
    system_instruction="""
        Você é um especialista em exemplos práticos. Receba o conceito do site e gere 2 ou 3 exemplos reais de como usuários utilizam esse site ou tecnologia no dia a dia. Explique cada exemplo de forma clara e conecte com situações comuns do cotidiano.
    """
)

# --- AGENTE 8: DICAS DE CARREIRA ---
meus_agentes["Dicas de Carreira"] = Agente(
    nome="Dicas de Carreira",
    system_instruction="""
        Você é um orientador de carreira em tecnologia. Receba o desafio proposto e relacione com oportunidades de carreira, áreas de atuação ou habilidades valorizadas no mercado. Dê dicas para o aluno sobre como esse conhecimento pode ser útil profissionalmente.
    """
)

# --- AGENTE 9: TESTES AUTOMATIZADOS ---
meus_agentes["Testes Automatizados"] = Agente(
    nome="Testes Automatizados",
    system_instruction="""
        Você é um engenheiro de testes. Receba o desafio de programação e sugira 3 a 5 testes automatizados que podem ser implementados para validar as soluções dos alunos. Explique o objetivo de cada teste e como ele contribui para a qualidade do código.
    """
)

# --- AGENTE 10: CURIOSIDADES TECNOLÓGICAS ---
meus_agentes["Curiosidades Tecnológicas"] = Agente(
    nome="Curiosidades Tecnológicas",
    system_instruction="""
        Você é um divulgador científico em tecnologia. Receba o conceito do site ou tema do desafio e compartilhe 2 curiosidades ou fatos históricos interessantes sobre o assunto, para inspirar e engajar o aluno.
    """
)
# ==============================================================================
# PROJETO: GERADOR DE ATIVIDADES DE PROGRAMAÇÃO v2.0
# DESCRIÇÃO: Um sistema com 5 agentes de IA especialistas que colaboram
#            em uma linha de montagem para criar um exercício de programação.
# ==============================================================================

# ==============================================================================
# PARTE 1: ESTRUTURA E CONFIGURAÇÃO DO FRAMEWORK
# ==============================================================================
import os
import google.generativeai as genai
import textwrap
import time
from dotenv import load_dotenv

# --- Configuração da Chave de API ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    print("✅ Chave de API configurada com sucesso!")
else:
    print("⚠️ Atenção: Chave de API não encontrada no arquivo .env.")
    print("   Crie um arquivo .env e adicione sua chave para o programa funcionar.")

# --- Função Auxiliar de Formatação de Texto ---
def formatar_texto(text: str) -> str:
    """Formata o texto para uma melhor exibição no terminal."""
    if not isinstance(text, str): text = str(text)
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# ==============================================================================
# PARTE 2: O MOLDE DO AGENTE (A CLASSE 'AGENTE')
# (Esta é a base do framework, não precisa ser alterada)
# ==============================================================================
class Agente:
    """Define a estrutura base para um agente de IA."""
    def __init__(self, nome: str, system_instruction: str, model_name: str = "gemini-1.5-flash"):
        self.nome = nome
        self.system_instruction = textwrap.dedent(system_instruction)
        self.model = genai.GenerativeModel(model_name=model_name, system_instruction=self.system_instruction)
        print(f"🤖 Agente '{self.nome}' contratado e pronto para o trabalho!")

    def executar(self, tarefa: str, contexto: str = None) -> str:
        """Executa uma tarefa, opcionalmente usando um contexto."""
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
# PARTE 3: A FÁBRICA DE AGENTES - A NOVA EQUIPE DE ESPECIALISTAS
# ==============================================================================
print("\n" + "="*80 + "\nINICIANDO A FÁBRICA DE AGENTES...\n" + "="*80)

meus_agentes = {}

# --- AGENTE 1: O ESTRATEGISTA ---
meus_agentes["Analisador de Negócios"] = Agente(
    nome="Analisador de Negócios",
    system_instruction="""
        Você é um analista de negócios sênior e didático. Ao receber uma URL, explique de forma clara e acessível:
        1. Qual é o modelo de negócio do site? (Explique com exemplos práticos)
        2. Quem é o público-alvo principal? (Descreva personas e situações de uso)
        3. Qual o propósito central ou problema que ele resolve? (Mostre o impacto para o usuário)
        Use linguagem simples, evite jargões e sempre conclua com uma frase que resuma o valor do site para o usuário comum.
    """
)

# --- AGENTE 2: O ENGENHEIRO DE FRONT-END ---
meus_agentes["Engenheiro de UI/UX"] = Agente(
    nome="Engenheiro de UI/UX",
    system_instruction="""
        Você é um engenheiro de Front-end e especialista em UI/UX, com foco em clareza e didática. Com base no conceito de negócio (contexto),
        liste de 5 a 7 componentes de interface e funcionalidades essenciais, explicando brevemente para que serve cada um e como o usuário interage.
        Formate como lista de tópicos, usando frases curtas e exemplos práticos. Ao final, destaque qual componente é mais importante para a experiência do usuário.
    """
)

# --- AGENTE 3: O ARQUITETO DE BACK-END ---
meus_agentes["Arquiteto de Back-End"] = Agente(
    nome="Arquiteto de Back-End",
    system_instruction="""
        Você é um arquiteto de software especializado em Back-end, com perfil explicativo. Com base nas funcionalidades de front-end (contexto),
        projete os recursos de back-end necessários, detalhando:
        1. Os principais modelos de dados (tabelas de banco de dados), explicando o papel de cada campo.
        2. Os 3 ou 4 endpoints de API mais importantes, mostrando exemplos de uso e o que cada um retorna.
        Use linguagem acessível, explique cada decisão e conclua com uma dica para quem está começando a programar APIs.
    """
)

# --- AGENTE 4: O CRIADOR DO DESAFIO ---
meus_agentes["Desenvolvedor de Conteúdo Didático"] = Agente(
    nome="Desenvolvedor de Conteúdo Didático",
    system_instruction="""
        Você é um educador de programação, focado em tornar o aprendizado envolvente e acessível. Receba as especificações de front-end e back-end (contexto)
        e transforme em um desafio de programação claro, motivador e estruturado.
        Organize em "Parte 1: Front-End" e "Parte 2: Back-End", detalhando cada tarefa com explicações, dicas e exemplos para facilitar o entendimento do aluno.
        Ao final de cada parte, inclua uma breve motivação sobre o que será aprendido e por que é útil.
    """
)

# --- AGENTE 5: O REVISOR FINAL ---
meus_agentes["Revisor Pedagógico"] = Agente(
    nome="Revisor Pedagógico",
    system_instruction="""
        Você é um professor experiente, com didática impecável e foco em motivação. Receba o rascunho de uma atividade de programação (contexto)
        e aprimore-o para que fique claro, envolvente e fácil de seguir.
        1. Simplifique a linguagem, tornando-a acessível e motivadora para todos os níveis.
        2. Formate o texto para PDF, usando títulos, listas, negrito e exemplos visuais.
        3. Adicione uma seção "Conselho do Mestre" ao final de cada parte (Front-end e Back-end) com uma dica útil, encorajando o aluno a pensar e explorar, sem entregar a resposta.
        4. Finalize com uma mensagem inspiradora para o aluno se sentir confiante ao realizar a atividade.
    """
)

# --- AGENTE 6: O EXPLORADOR WEB ALEATÓRIO ---
meus_agentes["Explorador Web Aleatório"] = Agente(
    nome="Explorador Web Aleatório",
    system_instruction="""
        Você é um explorador web curioso e didático. Sua função é escolher uma URL de um site popular, educativo ou interessante de forma aleatória.
        Escolha sites que possam gerar atividades úteis e inspiradoras. Retorne a URL escolhida e explique em uma frase por que esse site pode ser interessante para aprender programação ou tecnologia. Evite sites impróprios ou de conteúdo sensível.
    """
)

print("\n" + "="*80 + f"\nFÁBRICA CONCLUÍDA: {len(meus_agentes)} agentes contratados.\n" + "="*80)

# --- AGENTE 11: TECNOLOGIAS DE SITE FULL STACK ---
meus_agentes["Tecnologias Full Stack"] = Agente(
    nome="Tecnologias Full Stack",
    system_instruction="""
        Você é um especialista em desenvolvimento web full stack. Gere uma lista das principais tecnologias usadas para criar um site completo (front-end, back-end, banco de dados, autenticação, hospedagem, testes, etc). Para cada tecnologia, explique de forma simples o que ela faz e por que é importante no contexto de um projeto moderno.
        Formate como uma lista com nome da tecnologia, breve explicação e exemplos de uso.
    """
)

# --- AGENTE 7: EXEMPLOS PRÁTICOS ---
meus_agentes["Exemplos Práticos"] = Agente(
    nome="Exemplos Práticos",
    system_instruction="""
        Você é um especialista em exemplos práticos. Receba o conceito do site e gere 2 ou 3 exemplos reais de como usuários utilizam esse site ou tecnologia no dia a dia. Explique cada exemplo de forma clara e conecte com situações comuns do cotidiano.
    """
)

# --- AGENTE 8: DICAS DE CARREIRA ---
meus_agentes["Dicas de Carreira"] = Agente(
    nome="Dicas de Carreira",
    system_instruction="""
        Você é um orientador de carreira em tecnologia. Receba o desafio proposto e relacione com oportunidades de carreira, áreas de atuação ou habilidades valorizadas no mercado. Dê dicas para o aluno sobre como esse conhecimento pode ser útil profissionalmente.
    """
)

# --- AGENTE 9: TESTES AUTOMATIZADOS ---
meus_agentes["Testes Automatizados"] = Agente(
    nome="Testes Automatizados",
    system_instruction="""
        Você é um engenheiro de testes. Receba o desafio de programação e sugira 3 a 5 testes automatizados que podem ser implementados para validar as soluções dos alunos. Explique o objetivo de cada teste e como ele contribui para a qualidade do código.
    """
)

# --- AGENTE 10: CURIOSIDADES TECNOLÓGICAS ---
meus_agentes["Curiosidades Tecnológicas"] = Agente(
    nome="Curiosidades Tecnológicas",
    system_instruction="""
        Você é um divulgador científico em tecnologia. Receba o conceito do site ou tema do desafio e compartilhe 2 curiosidades ou fatos históricos interessantes sobre o assunto, para inspirar e engajar o aluno.
    """
)

# ==============================================================================
# PARTE 4: A ORQUESTRA - A NOVA LINHA DE MONTAGEM
# ==============================================================================

def main():
    """Função principal que executa o fluxo de trabalho dos agentes."""

    print("\n--- INICIANDO ORQUESTRADOR DE AGENTES v2.1 ---")
    escolha = input("❓ Deseja informar uma URL ou deixar o agente escolher um site aleatório? (digite 'manual' ou 'aleatorio')\n> ").strip().lower()
    print("-" * 80)

    # Pausa entre agentes para não sobrecarregar a API e facilitar a leitura.
    PAUSA_ENTRE_AGENTES = 10

    try:
        if escolha == "aleatorio":
            tarefa_inicial = meus_agentes["Explorador Web Aleatório"].executar(tarefa="Escolha uma URL aleatória.")
            print(f"\n🌐 URL escolhida pelo agente: {tarefa_inicial}")
        else:
            tarefa_inicial = input("❓ Qual a URL do site que vamos usar como base para a atividade? (ex: https://www.airbnb.com)\n> ")

        # ETAPA 1: O Analisador de Negócios define o conceito.
        contexto_conceito = meus_agentes["Analisador de Negócios"].executar(tarefa=f"Analise a URL: {tarefa_inicial}")
        print("\n---  концепт ETAPA 1: CONCEITO DE NEGÓCIO ---")
        print(formatar_texto(contexto_conceito))
        time.sleep(PAUSA_ENTRE_AGENTES)

        # ETAPA 2: O Engenheiro de UI/UX lista as funcionalidades.
        contexto_frontend = meus_agentes["Engenheiro de UI/UX"].executar(tarefa="Liste os componentes de UI/UX.", contexto=contexto_conceito)
        print("\n--- 🎨 ETAPA 2: ESPECIFICAÇÕES DE FRONT-END ---")
        print(formatar_texto(contexto_frontend))
        time.sleep(PAUSA_ENTRE_AGENTES)

        # ETAPA 3: O Arquiteto de Back-End projeta a API e o DB.
        contexto_backend = meus_agentes["Arquiteto de Back-End"].executar(tarefa="Projete a API e os modelos de dados.", contexto=contexto_frontend)
        print("\n--- ⚙️ ETAPA 3: ESPECIFICAÇÕES DE BACK-END ---")
        print(formatar_texto(contexto_backend))
        time.sleep(PAUSA_ENTRE_AGENTES)

        # ETAPA 4: O Desenvolvedor Didático monta o rascunho da atividade.
        contexto_para_desafio = f"Especificações de Front-End:\n{contexto_frontend}\n\nEspecificações de Back-End:\n{contexto_backend}"
        contexto_rascunho = meus_agentes["Desenvolvedor de Conteúdo Didático"].executar(tarefa="Crie o desafio de programação.", contexto=contexto_para_desafio)
        print("\n--- 📝 ETAPA 4: RASCUNHO DA ATIVIDADE ---")
        print(formatar_texto(contexto_rascunho))
        time.sleep(PAUSA_ENTRE_AGENTES)

        # ETAPA 5: O Revisor Pedagógico dá o toque final.
        atividade_final = meus_agentes["Revisor Pedagógico"].executar(tarefa="Revise e formate esta atividade.", contexto=contexto_rascunho)
        print("\n" + "="*80)
        print("✨🎉 ATIVIDADE FINAL REVISADA (Pronta para os Alunos!) 🎉✨")
        print("="*80)
        print(formatar_texto(atividade_final))

    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado durante a orquestração: {e}")

# ==============================================================================
# PARTE 5: PONTO DE PARTIDA DO PROGRAMA
# ==============================================================================
if __name__ == "__main__":
    main()