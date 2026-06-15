import os
from openai import OpenAI
from core.llm.base import BaseLLMClient

class FeatherlessClient(BaseLLMClient):
    """
    LLM Client implementation for Featherless AI.
    Uses the OpenAI-compatible SDK.
    """
    def __init__(self, api_key: str = None, base_url: str = None, model: str = None):
        self.api_key = api_key or os.getenv("FEATHERLESS_API_KEY")
        self.base_url = base_url or os.getenv("FEATHERLESS_BASE_URL", "https://api.featherless.ai/v1")
        self.model = model or os.getenv("FEATHERLESS_MODEL", "deepseek-ai/DeepSeek-V4-Flash")
        
        if not self.api_key:
            raise ValueError("FEATHERLESS_API_KEY must be provided or set in environment variables.")
        
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
        )

    def generate_completion(self, prompt: str, system_prompt: str = "") -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.0
        )
        return response.choices[0].message.content
