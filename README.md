## AI Research Agent

This project implements an AI research agent that uses a primary agent (GPT-4o) to process user queries, search the web for relevant information, synthesize the findings, and then uses a verifier agent (Claude) to enhance the accuracy and reliability of the results.

### Project Structure

The project is organized as follows:

```
.
├── src/
│   ├── agent/              # Contains the core agent logic
│   │   ├── __init__.py
│   │   ├── primary_agent.py  # Main agent logic (GPT-4o)
│   │   └── verifier_agent.py # Verification agent (Claude)
│   ├── web_search/         # Module for web searching capabilities
│   │   └── __init__.py
│   ├── result_synthesis/   # Module for synthesizing search results
│   │   └── __init__.py
│   └── utils/              # Utility functions and classes
│       └── __init__.py
├── config/
│   └── api_keys.json.template # Template for API keys
├── main.py                 # Main script to run the agent
└── README.md               # This file
```

### Setup and Configuration

1.  **Clone the repository:**
    ```bash
    git clone https://your-repository-url.git
    cd ai-research-agent
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Keys:**
    *   Rename the `config/api_keys.json.template` file to `config/api_keys.json`.
    *   Open `config/api_keys.json` and replace the placeholder values with your actual API keys for OpenAI and Anthropic.
    ```json
    {
        "openai_api_key": "YOUR_OPENAI_API_KEY",
        "anthropic_api_key": "YOUR_ANTHROPIC_API_KEY"
    }
    ```
    *   **Security Note:** It's crucial to keep your API keys confidential. Consider using environment variables for production deployments.

### Running the Agent

To start the AI research agent, run the following command from the project's root directory:

```bash
python main.py
```

### How it Works

1.  **User Query:** The user provides a query to the system.
2.  **Primary Agent (GPT-4o):** The primary agent processes the query and determines the best course of action. This may involve breaking down the query, identifying keywords, or formulating a search strategy.
3.  **Web Search:** The agent uses its web search capabilities to find relevant information from the internet. This might involve using search engines or accessing specific websites.
4.  **Result Synthesis:** The gathered information is synthesized and compiled into a coherent response.
5.  **Verifier Agent (Claude):** The synthesized response is then passed to the verifier agent, which uses the Claude model to check for accuracy, consistency, and potential biases. The verifier may suggest improvements or flag any issues.
6.  **Final Response:** The refined and verified response is presented to the user.

### Customization

*   **LLM Models:** You can easily swap out the GPT-4o and Claude models with other compatible language models by modifying the respective agent files in the `src/agent/` directory.
*   **Search Functionality:** The web search module can be extended to use different search APIs or techniques based on your requirements.
*   **User Interface:** Currently, the agent operates through a command-line interface. You can build a graphical user interface (GUI) or integrate it into other applications as needed.

### Disclaimer

This project is for research and educational purposes. The accuracy and reliability of the information provided by the AI agent depend on various factors, including the quality of the language models and the data sources used. Always critically evaluate the output and consult multiple sources for important decisions.
