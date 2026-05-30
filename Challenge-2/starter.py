import os
import requests
from datetime import date, datetime

os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent, tool
from strands_tools import calculator

MODEL = "us.amazon.nova-pro-v1:0"


@tool
def weather(city: str) -> str:
    """Get current weather for a city.
    Args:
        city: City name.
    """
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=10)
        data = response.json()

        current = data["current_condition"][0]
        temp = current["temp_C"]
        condition = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]

        return (
            f"Weather in {city}: {condition}, "
            f"{temp}°C, Humidity {humidity}%"
        )

    except Exception as e:
        return f"Unable to fetch weather for {city}: {e}"


@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from birth date.
    Args:
        birth_date: Birth date in YYYY-MM-DD format.
    """
    dob = datetime.strptime(birth_date, "%Y-%m-%d").date()
    today = date.today()

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return f"Age: {age} years old"


agent = Agent(
    model=MODEL,
    tools=[
        calculator,
        weather,
        age_calculator
    ],
    system_prompt="""
    You are AWS Campus Mentor AI.

    You help students with:
    - AWS Cloud concepts
    - Amazon Bedrock and Generative AI
    - Mathematical calculations
    - Weather information
    - Age calculations

    Use tools whenever needed.
    Give short, clear, and beginner-friendly answers.
    """
)


print("=" * 70)
print("🚀 AWS Campus Mentor AI - Challenge 2")
print("=" * 70)

print("\nYou can ask questions like:")
print("- What is 42 * 17?")
print("- What is the weather in Chennai?")
print("- How old is someone born on 2006-04-15?")
print("- Explain Amazon Bedrock simply")
print("- What is the weather in Chennai and what is 125 * 87?")
print("\nType 'exit' to quit.\n")


while True:
    try:
        question = input("You: ").strip()

        if not question:
            continue

        if question.lower() in ["exit", "quit", "q"]:
            print("\n👋 Exiting AWS Campus Mentor AI. Bye!")
            break

        print("\nAI: ", end="")
        response = agent(question)
        print(response)
        print("-" * 70)

    except KeyboardInterrupt:
        print("\n\n👋 Session stopped.")
        break

    except Exception as e:
        print(f"\n❌ Error: {e}")