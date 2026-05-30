from strands import Agent
from strands.models.ollama import OllamaModel

ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.2:3b"
)

agent = Agent(
    model=ollama_model,
    system_prompt="""
    You are AWS Campus Mentor AI.
    Help students learn AWS and GenAI.
    """
)

while True:
    question = input("\nAsk Me: ")

    if question.lower() == "exit":
        break

    response = agent(question)

    print("\nAnswer:")
    print(response)