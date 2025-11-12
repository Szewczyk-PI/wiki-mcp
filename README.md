# Wiki Agent - Inteligentny Asystent do Wiki.js

## Co to jest?

Wiki Agent to inteligentny system AI oparty na CrewAI, który automatycznie wyszukuje i przetwarza informacje z bazy danych Wiki.js. Agent potrafi:

- Wyszukiwać artykuły w Wiki.js na podstawie zapytań
- Analizować i podsumowywać treści
- Czyścić tekst z formatowania Markdown
- Zwracać gotowe podsumowania wraz z linkami

## Jak to działa?

System składa się z trzech głównych elementów:

### 1. Wiki Agent (AI)

Agent AI z rolą "Wiki Knowledge Expert", który:

- Komunikuje się z Wiki.js przez protokół MCP (Model Context Protocol)
- Wykorzystuje zaawansowane możliwości wyszukiwania
- Przetwarza i analizuje znalezione treści

### 2. MCP Server (wiki-js-mcp)

Serwer pośredniczący między agentem AI a Wiki.js:

- Dostarcza 21 narzędzi do zarządzania dokumentacją
- Obsługuje hierarchiczną strukturę dokumentów
- Integruje się z GraphQL API Wiki.js

### 3. Custom Tools

Dodatkowe narzędzia Pythonowe:

- `clear_markd` - czyści tekst z formatowania Markdown (\*, \*\*, #, |, itp.)

## Wymagania systemowe

- Python >= 3.10 i < 3.14
- Wiki.js (lokalny lub zdalny)
- UV - menedżer pakietów Python
- PostgreSQL (dla Wiki.js)

## Instalacja

### Krok 1: Przygotowanie środowiska

```bash
# Zainstaluj UV (jeśli nie masz)
pip install uv

# Przejdź do katalogu projektu
cd /wiki/
```

### Krok 2: Konfiguracja Wiki.js MCP Server

```bash
# Przejdź do katalogu MCP
cd src/wiki/wiki-js-mcp

# Skopiuj plik konfiguracyjny
cp config/example.env .env

# Uruchom skrypt instalacyjny
./setup.sh
```

### Krok 3: Konfiguracja zmiennych środowiskowych

Edytuj plik `.env` w katalogu `wiki-js-mcp`:

```bash
# Konfiguracja Wiki.js
WIKIJS_API_URL=http://localhost:3000
WIKIJS_TOKEN=twoj_token_api_z_wikijs

# Alternatywnie: login i hasło
WIKIJS_USERNAME=twoj_username
WIKIJS_PASSWORD=twoje_haslo

# Baza danych mapowań
WIKIJS_MCP_DB=./wikijs_mappings.db
LOG_LEVEL=INFO
LOG_FILE=wikijs_mcp.log
```

**Jak uzyskać token API z Wiki.js:**

1. Zaloguj się do Wiki.js jako administrator
2. Przejdź do Admin Panel → API Access
3. Utwórz nowy klucz API
4. Skopiuj token do pliku `.env`

### Krok 4: Instalacja zależności projektu głównego

```bash
# Wróć do głównego katalogu
# Zainstaluj zależności
crewai install
```

### Krok 5: Konfiguracja API dla AI

Utwórz plik `.env` w głównym katalogu projektu:

```bash
# Klucz API do Google Gemini
GOOGLE_API_KEY=twoj_klucz_api_google

# Lub dla OpenAI (jeśli wolisz)
OPENAI_API_KEY=twoj_klucz_openai
```

## Uruchomienie

### Opcja 1: Uruchomienie podstawowe

```bash
# Z głównego katalogu projektu
crewai run
```

### Opcja 2: Uruchomienie z własnym zapytaniem

Edytuj plik `src/wiki/main.py` i zmień parametr `inputs`:

```python
def run():
    inputs = {
        'topic': 'Twoje zapytanie tutaj',
        'current_year': str(datetime.now().year)
    }
    Wiki().crew().kickoff(inputs=inputs)
```

Następnie uruchom:

```bash
crewai run
```

## Struktura Projektu

```
wiki/
├── src/wiki/
│   ├── config/
│   │   ├── agents.yaml          # Definicje agentów AI
│   │   └── tasks.yaml           # Definicje zadań
│   ├── tools/
│   │   └── custom_tool.py       # Narzędzie do czyszczenia Markdown
│   ├── wiki-js-mcp/             # Serwer MCP dla Wiki.js
│   │   ├── src/
│   │   │   └── wiki_mcp_server.py
│   │   ├── setup.sh
│   │   ├── start-server.sh
│   │   └── .env                 # Konfiguracja MCP
│   ├── crew.py                  # Definicja crew i agentów
│   └── main.py                  # Punkt wejścia aplikacji
├── .env                         # Klucze API (Google/OpenAI)
├── pyproject.toml              # Zależności projektu
└── README.md                   # Ten plik
```

## Narzędzia MCP dostępne dla agenta

Agent ma dostęp do 21 narzędzi Wiki.js, m.in.:

- `wikijs_search_pages` - wyszukiwanie stron
- `wikijs_get_page` - pobieranie treści strony
- `wikijs_create_page` - tworzenie nowej strony
- `wikijs_update_page` - aktualizacja strony
- `wikijs_create_nested_page` - tworzenie hierarchii
- `wikijs_delete_page` - usuwanie stron
- i wiele innych...

Pełna lista w: `src/wiki/wiki-js-mcp/README.md`
