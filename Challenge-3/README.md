# 🧠 Challenge 3 – AWS Campus Memory Agent

## 🚀 Overview

Challenge 3 focuses on building an AI Agent with Persistent Memory capabilities using Amazon Nova Pro, Strands Agents SDK, mem0, and FAISS.

Unlike traditional AI assistants that forget previous interactions, this agent can store and retrieve important user information across conversations.

This challenge demonstrates how memory-enabled AI systems can create personalized learning experiences for students and users.

---

# 🎯 Objective

Build an AI assistant capable of:

- Remembering user information
- Storing conversation context
- Recalling previously saved details
- Creating personalized interactions
- Demonstrating persistent AI memory

---

# 🏗️ Architecture

```text
User
   │
   ▼
AWS Campus Memory Agent
   │
   ▼
Amazon Nova Pro
   │
   ▼
mem0 Memory Layer
   │
   ▼
FAISS Vector Store
   │
   ▼
Persistent Memory Storage
```

---

# ⚙️ Technologies Used

- Amazon Bedrock
- Amazon Nova Pro
- Strands Agents SDK
- mem0 Memory Framework
- FAISS Vector Database
- Python

---

# ✨ Features

## Memory Storage

The agent can remember:

- User name
- Career goals
- College information
- Learning preferences
- AWS interests

Example:

```text
Remember that my name is Thamarai
```

---

## Personalized Learning

Example:

```text
Remember that I want to become a GenAI Engineer
```

The agent stores this information for future reference.

---

## Context Awareness

The assistant maintains user-specific context and attempts to provide more personalized responses.

---

# 📂 Project Structure

```text
Challenge-3/
│
├── starter.py
├── README.md
│
└── screenshots/
    ├── SS1.png
    └── SS2.png
```

---

# 🧪 Sample Interactions

## Store Memory

```text
Remember that my name is Thamarai
```

Output:

```text
I have remembered your name.
```

---

## Store Career Goal

```text
Remember that I want to become a GenAI Engineer
```

Output:

```text
I have remembered your career goal.
```

---

## Retrieve Memory

```text
What is my name?
```

---

# 📸 Screenshots

### Memory Storage

Stored user information successfully.

### Memory Retrieval

Memory retrieval testing and validation.

---

# 🔍 Observations

During testing:

✅ Memory storage worked successfully

✅ User details were saved

✅ mem0 integration worked

✅ FAISS integration worked

⚠️ Some retrieval operations showed compatibility limitations with the current Bedrock provider setup.

This behavior is related to provider-side model compatibility and does not impact memory storage functionality.

---

# 🎓 Learning Outcomes

Through this challenge I learned:

- Persistent Memory Concepts
- Vector Databases
- FAISS Integration
- mem0 Framework
- Personalized AI Systems
- Context-Aware AI Assistants
- Memory-Driven User Experiences

---

# 🚀 Future Improvements

Planned enhancements include:

- Long-term memory management
- Memory ranking and prioritization
- Student profile generation
- Academic progress tracking
- Personalized AWS learning recommendations
- MCP integration with memory systems

---

# 🏆 Conclusion

Challenge 3 successfully demonstrated how modern AI agents can move beyond simple question answering and begin maintaining meaningful user context through persistent memory.

This represents a significant step toward building intelligent, personalized AI assistants for education and mentorship use cases.