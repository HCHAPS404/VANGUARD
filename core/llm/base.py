from abc import ABC, abstractmethod

class BaseLLMClient(ABC):
    """
    Base interface for LLM clients.
    Allows easy swapping between Featherless, AI/ML API, or local Ollama instances.
    """
    
    @abstractmethod
    def generate_completion(self, prompt: str, system_prompt: str = "") -> str:
        """
        Generates a text completion based on the prompt.
        
        Args:
            prompt (str): The user prompt.
            system_prompt (str, optional): The system prompt for context.
            
        Returns:
            str: The generated text response.
        """
        pass
