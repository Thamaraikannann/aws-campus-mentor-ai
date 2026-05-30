import os
from datetime import datetime

os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent
from strands_tools import calculator, mem0_memory
from strands import tool


@tool
def weather(city: str) -> str:
    weather_data = {
        "chennai": "Sunny, 31°C",
        "coimbatore": "Cloudy, 28°C",
        "madurai": "Hot, 33°C",
    }

    return weather_data.get(city.lower(), f"Weather data not found for {city}")


@tool
def age_calculator(dob: str) -> str:
    birth = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()

    age = (
        today.year
        - birth.year
        - ((today.month, today.day) < (birth.month, birth.day))
    )

    return f"Age is {age} years"


MODEL = "us.amazon.nova-pro-v1:0"

agent = Agent(
    model=MODEL,
    tools=[
        calculator,
        weather,
        age_calculator,
        mem0_memory,
    ],
)

print("=" * 60)
print("🚀 AWS Campus Smart Agent - Challenge 4")
print("=" * 60)

print("\nTools Available:")
print("✅ Calculator")
print("✅ Weather")
print("✅ Age Calculator")
print("✅ Memory")
print("✅ Streaming Responses")

print("\nType 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("Bye 👋")
        break

    print("\nAI: ", end="")

    response = agent(question)

    print(response)
    print("\n" + "-" * 60)