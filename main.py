import argparse
import json
import os
from src.agent.primary_agent import PrimaryAgent
from src.agent.verifier_agent import VerifierAgent
from src.web_search.web_search import WebSearch
from src.result_synthesis.result_synthesizer import ResultSynthesizer

def load_api_keys():
    """Load API keys from config file."""
    config_path = os.path.join(os.path.dirname(__file__), "config", "api_keys.json")
    try:
        with open(config_path, 'r') as file:
            keys = json.load(file)
            return keys.get("openai_api_key"), keys.get("anthropic_api_key")
    except FileNotFoundError:
        print(f"Error: Could not find API keys file at {config_path}")
        print("Please ensure you've created the config/api_keys.json file with your API keys.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON in the API keys file.")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description="AI Research Agent Pipeline")
    parser.add_argument("--query", type=str, help="User query for the AI research agent")
    args = parser.parse_args()
    
    # Get query from command line or prompt the user
    query = args.query
    if not query:
        query = input("Enter your research query: ")
    
    print(f"Received query: {query}")
    
    # Load API keys
    openai_api_key, anthropic_api_key = load_api_keys()
    
    # Initialize components
    primary_agent = PrimaryAgent(api_key=openai_api_key)
    verifier_agent = VerifierAgent(api_key=anthropic_api_key)
    search_module = WebSearch()
    synthesis_module = ResultSynthesizer()
    
    # Primary agent processing
    print("Processing with primary agent (GPT-4o)...")
    prompt = f"I'm researching the following question: '{query}'. Please break this down into key search terms and concepts that would help me find relevant information. Also provide any context or background knowledge that would be helpful."
    primary_agent_output = primary_agent.generate_response(prompt)
    print("\nPrimary Agent Output:")
    print(primary_agent_output)
    
    # Web search
    print("\nPerforming web search...")
    search_results = search_module.search(query)
    print(f"Found {len(search_results)} search results")
    
    # Result synthesis
    print("\nSynthesizing results...")
    synthesized_output = synthesis_module.synthesize(search_results, query)
    print("\nSynthesized Output:")
    print(synthesized_output)
    
    # Verifier agent processing
    print("\nVerifying with Claude...")
    verification_prompt = f"""
    Please verify the following synthesized research results for accuracy, completeness, and logical coherence:
    
    ORIGINAL QUERY: {query}
    
    PRIMARY AGENT ANALYSIS:
    {primary_agent_output}
    
    SYNTHESIZED SEARCH RESULTS:
    {synthesized_output}
    
    Please identify any:
    1. Factual errors or inconsistencies
    2. Incomplete or missing information
    3. Logical fallacies or biased reasoning
    4. Additional context that would be helpful
    
    Then provide an improved, verified version of the response.
    """
    verified_output = verifier_agent.verify_synthesis(verification_prompt)
    
    print("\nFinal Verified Response:")
    print(verified_output)

if __name__ == "__main__":
    main()
