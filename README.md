# AI Chatbot

This is a fastAPI microservice for a chatbot powered by AI using a open source LLM

## 🤖 Overview
This project aims to simulate a text mesagge chatbot experience with one agent. The project utilizes FastAPI and you can deploy it locally.

## 👌 Features
- **LLM Usage:** Integration of Large Language Model (LLM) with a conversation
- **Open Source Model:** It use a huggingface model

### ✍️ Prerequisites
Before you begin, make sure you have the following prerequisites:
- Python 3.9 or later installed
- Docker installed
- Do not forget to set the `.env` file it is not ignored on the repo

## 🧤 Getting Started
Follow these steps to set up and run the project:

1. **Clone the Repository:**
   ```
   git clone git@github.com:DLesmes/ai_chatbot.git
   cd ai_chatbot
   ```
   
2. Set Up Python Virtual Environment with the [requirements.txt](https://github.com/DLesmes/ai_chatbot/blob/main/requirements.txt):

    ```
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install -r requirements.txt
    ```
3. Run the Server:

* Using uvicorn:
    ```
    uvicorn main:app --reload
    ```
* Alternatively:
    ```
    python3 main.py
    ```
You can also debug it in your preferred IDE.


## 🤝 Contributing

Feel free to contribute and make this chatbot project even better!
We welcome contributions from the community! If you'd like to contribute, please follow these steps:

* Fork this repository
* Create a new branch: `git checkout -b feature/YourFeatureName`
* Make your changes and commit them: `git commit -am 'Add some feature'`
* Push to the branch: `git push origin feature/YourFeatureName`
* Create a pull request
We look forward to your contributions!

## 💬 Contact

For any questions or suggestions, feel free to reach out here is [my profile](https://github.com/DLesmes)
