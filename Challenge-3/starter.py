import os

os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent
from strands_tools import mem0_memory

MODEL = "us.amazon.nova-pro-v1:0"

agent = Agent(
    model=MODEL,
    tools=[mem0_memory],
    system_prompt="""
    You are AWS Campus Memory Agent.

    You help students by remembering useful details such as:
    - their name
    - learning goal
    - favorite AWS service
    - career interest

    Store and recall memories when needed.
    Give short and clear answers.
    """
)

print("🧠 AWS Campus Memory Agent Ready!")
print("Try:")
print("- Remember that my name is Thamarai")
print("- Remember that I want to become a GenAI Engineer")
print("- What is my name?")
print("- What is my career goal?")
print("\nType 'exit' to quit.\n")

while True:
    try:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit", "q"]:
            print("Bye! 👋")
            break

        print("\nAgent: ", end="")
        response = agent(user_input)
        print(response)
        print("-" * 70)

    except KeyboardInterrupt:
        print("\nBye! 👋")
        break