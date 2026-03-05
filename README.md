# 🤖 AI Sales Agent – Conversational Quoting & Order Management System

Production-ready conversational AI agent designed to automate customer interactions, generate personalized quotes, provide intelligent recommendations, and manage order workflows within a real business process.

This project demonstrates how to build a structured LLM-powered backend system using clean architecture principles and contextual conversation processing.

---

## 🎯 Project Purpose

This is not a simple chatbot.

It is a business-oriented AI system capable of:

- Processing multi-message conversations
- Preserving chronological context
- Detecting user intent
- Generating structured commercial responses
- Managing order workflows
- Integrating into automated backend pipelines

The agent simulates a real-world sales assistant operating through messaging platforms such as WhatsApp.

---

## 🚀 Core Capabilities

### 1️⃣ Contextual Conversation Handling
- Receives multiple user messages
- Orders them chronologically
- Constructs structured conversation history
- Preserves semantic meaning across messages

### 2️⃣ Personalized Quote Generation
- Extracts quantities and constraints
- Interprets implicit requirements
- Generates dynamic quotes
- Suggests appropriate product configurations

### 3️⃣ Intelligent Recommendations
- Detects missing information
- Asks strategic follow-up questions
- Suggests optimal or popular options
- Adapts responses dynamically

### 4️⃣ Order Management
- Confirms customer details
- Summarizes order information
- Prepares structured output for downstream systems
- Ready for payment integration

---

## 🧠 System Architecture

The project follows Clean Architecture principles:

- Separation of concerns
- Service layer orchestration
- Repository abstraction
- Domain-driven logic
- Infrastructure decoupled from business rules

Conversation flow:

1. Messages received from external source
2. Messages sorted chronologically
3. Structured chat history constructed
4. Agent analyzes intent
5. Business rules applied
6. Structured response generated

---

## 🏗️ Tech Stack

- Python
- FastAPI
- LLM-based agent
- n8n (workflow orchestration)
- Docker
- Clean Architecture pattern

---

## 📈 What This Project Demonstrates

- Real-world LLM backend integration
- Context management in conversational systems
- AI-driven business automation
- Structured agent engineering
- Scalable system design

---

## 🔮 Future Improvements

- Persistent memory per customer
- Product database integration
- Payment gateway integration
- Multi-agent role separation (Sales / Support / Operations)
- Observability and logging improvements

---

## 👨‍💻 Author

Adrián Páez  
Backend Developer | AI Systems Builder
