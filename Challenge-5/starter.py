from strands import Agent

MODEL = "us.amazon.nova-pro-v1:0"

# Load Knowledge Base
with open("training_data/aws_knowledge.txt", "r", encoding="utf-8") as file:
    knowledge_base = file.read()

# Create Agent
agent = Agent(
    model=MODEL,
    system_prompt=f"""
You are AWS Campus Mentor AI.

Use the knowledge below when answering:

{knowledge_base}

If the answer exists in the knowledge base, answer from it.
If not, use your general AWS knowledge.
Always answer clearly and professionally.
"""
)

print("=" * 60)
print("🚀 AWS Campus Mentor AI - Challenge 5")
print("=" * 60)

print("\nKnowledge Base Loaded Successfully!")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    try:
        response = agent(user_input)

        print("\nAI:", response)
        print("\n" + "-" * 60)

    except Exception as e:
        print("\nError:", e)