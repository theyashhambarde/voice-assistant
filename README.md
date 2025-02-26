# AI Virtual Agent Developer Intern Project

## Overview
This project implements a simple AI Voice Assistant backend using FastAPI. It accepts text input (simulating voice), performs basic intent recognition using keyword matching, and logs each interaction.

## Features
- **FastAPI Backend:** Provides a `/predict` endpoint that accepts text input.
- **NLP Processing:** Basic intent recognition using keyword matching (e.g., detecting "weather", "time", "joke").
- **Logging:** Logs API requests and detected intents.
- **Dockerization:** Containerized using Docker for easy deployment.
- **(Optional) Database Integration:** Placeholder code for integrating MongoDB/PostgreSQL.

## API Endpoint

- **POST /predict**  
  **Request Body:**
  ```json
  {
    "text": "What is the weather today?"
  }
