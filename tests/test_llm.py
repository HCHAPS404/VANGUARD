import pytest
from unittest.mock import patch, MagicMock
from core.llm.featherless_client import FeatherlessClient

@patch('core.llm.featherless_client.OpenAI')
def test_featherless_client_completion(mock_openai):
    # Setup mock
    mock_client_instance = MagicMock()
    mock_response = MagicMock()
    mock_message = MagicMock()
    mock_message.content = "Mocked response"
    mock_choice = MagicMock()
    mock_choice.message = mock_message
    mock_response.choices = [mock_choice]
    
    mock_client_instance.chat.completions.create.return_value = mock_response
    mock_openai.return_value = mock_client_instance
    
    # Init client
    client = FeatherlessClient(api_key="test_key", model="test-model")
    
    # Execute
    result = client.generate_completion(prompt="Hello", system_prompt="You are helpful")
    
    # Assert
    assert result == "Mocked response"
    mock_client_instance.chat.completions.create.assert_called_once_with(
        model="test-model",
        messages=[
            {"role": "system", "content": "You are helpful"},
            {"role": "user", "content": "Hello"}
        ],
        temperature=0.0
    )

def test_featherless_client_missing_key(monkeypatch):
    monkeypatch.delenv("FEATHERLESS_API_KEY", raising=False)
    with pytest.raises(ValueError, match="FEATHERLESS_API_KEY must be provided"):
        FeatherlessClient(api_key=None)
