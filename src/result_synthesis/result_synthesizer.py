class ResultSynthesizer:
    def __init__(self):
        """Initializes the ResultSynthesizer module."""
        pass

    def synthesize(self, search_results: list, query: str = "") -> str:
        """
        Synthesizes web search results into a coherent text.

        Args:
            search_results (list): A list of search result dictionaries, 
                                   where each dictionary might contain 'title', 'link', and 'snippet'.
            query (str): The original query that led to these search results.

        Returns:
            str: A synthesized text string summarizing the search results.
                 Returns a message if no results are provided.
        """
        if not search_results:
            return "No search results were provided to synthesize."

        synthesized_text = f"Synthesized Information for query: 	'{query}'\n\n"
        synthesized_text += "Based on the web search, here is a summary of the findings:\n\n"

        for i, result in enumerate(search_results):
            title = result.get("title", "No title available")
            link = result.get("link", "No link available")
            snippet = result.get("snippet", "No snippet available")
            
            synthesized_text += f"Source {i+1}:\n"
            synthesized_text += f"  Title: {title}\n"
            synthesized_text += f"  Link: {link}\n"
            synthesized_text += f"  Snippet: {snippet}\n\n"
        
        synthesized_text += "Please review the above information. This synthesized result will be passed to a verifier agent."
        
        return synthesized_text

if __name__ == '__main__':
    # Example Usage:
    mock_search_results = [
        {
            "title": "Impact of Chernobyl on European Agriculture - WHO Report",
            "link": "https://example.com/who-chernobyl-agriculture-report",
            "snippet": "The Chernobyl disaster had significant and long-lasting impacts on agriculture across Europe. Contamination of soil and water led to restrictions on farming and food consumption..."
        },
        {
            "title": "Chernobyl's Agricultural Fallout: A Two-Decade Retrospective",
            "link": "https://example.com/journal-chernobyl-fallout",
            "snippet": "A study reviewing two decades of data shows that radioactive isotopes like Caesium-137 and Strontium-90 affected crops and livestock, with varying intensity based on geographical location and weather patterns following the incident."
        },
        {
            "title": "Economic Consequences for Farmers after Chernobyl",
            "link": "https://example.com/chernobyl-economic-impact-farmers",
            "snippet": "Farmers in affected regions faced severe economic hardship due to unsalable produce and livestock, land use restrictions, and the need for costly remediation measures."
        }
    ]

    synthesizer = ResultSynthesizer()
    original_query = "What was the immediate impact of the Chernobyl disaster on European agriculture?"
    synthesized_content = synthesizer.synthesize(mock_search_results, original_query)
    
    print("Synthesized Content:\n")
    print(synthesized_content)

    # Test with empty results
    print("\nTesting with empty results:")
    empty_results_synthesis = synthesizer.synthesize([], original_query)
    print(empty_results_synthesis)

