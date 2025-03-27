## GitHub & Wakatime Profile Scraper
### 📌 Descrição
Este projeto é um agente automatizado que analisa informações de perfis do GitHub e Wakatime para gerar um resumo técnico estruturado em JSON. Ele acessa os perfis, interage com os sites e extrai dados sobre experiências, habilidades e estatísticas de desenvolvimento.

### 🚀 Funcionalidades
Acessa perfis do GitHub e Wakatime automaticamente.

Extrai informações de experiências, projetos e habilidades técnicas.

Analisa os repositórios fixados e últimas contribuições no GitHub.

Obtém as linguagens mais usadas, editores de código e sistemas operacionais no Wakatime.

Organiza os dados coletados em um arquivo JSON.

### 🛠️ Tecnologias Utilizadas
- Python (Automação e Web Scraping)

- Langchain (Integração com IA)

- OpenAI GPT-4o (Processamento de texto)

[Browser-Use](https://github.com/browser-use/browser-use) (Interação automatizada com a web)

### 📄 Como Funciona?
O agente acessa os perfis especificados no GitHub e Wakatime.

Ele interage com as páginas, analisando README de perfil e repositórios fixados.

Extrai informações sobre contribuições recentes, habilidades e ferramentas utilizadas.

Gera um resumo técnico em JSON, estruturando os dados coletados.

Exibe o resultado no console.

### 📦 Instalação e Uso
Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure sua chave de API OpenAI no arquivo .env:
```plaintext
OPENAI_API_KEY=your-api-key-here
```
Execute o script:

```bash
python main.py
```
### 📌 Exemplo de Saída JSON
```json
{
  "name": "Welli7ngton",
  "github": {
    "pinned_repositories": ["Repo1", "Repo2", "Repo3"],
    "recent_contributions": ["Project A", "Project B"]
  },
  "wakatime": {
    "top_languages": ["Python", "JavaScript", "Go", "TypeScript", "Rust"],
    "top_editors": ["VS Code", "Neovim", "IntelliJ"],
    "top_operating_systems": ["Linux", "MacOS", "Windows"]
  },
  "skills": ["Machine Learning", "Backend Development", "Automation", "Web Scraping"]
}
```
