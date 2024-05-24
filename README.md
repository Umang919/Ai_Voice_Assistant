# AI Voice Assistant

This project is an AI voice assistant that utilizes OpenAI's API for natural language processing. It can execute various commands such as opening applications like YouTube and Visual Studio Code, and it can also interact with the user by answering questions or generating Python scripts on request, which are saved as text files.

## Features

- **Voice Recognition:** The assistant can recognize and process voice commands.
- **Open Applications:** It can open applications like YouTube and Visual Studio Code based on user commands.
- **Natural Language Interaction:** Using OpenAI's API, the assistant can answer questions posed by the user.
- **Text File Generation:** When asked, the assistant can generate Python code, saving the code and the corresponding question in a text file.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/AI-Voice-Assistant.git
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd AI-Voice-Assistant
    ```

3. **Install Required Packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up API Keys:**
    - Ensure you have your OpenAI API key ready.
    - Create a `.env` file in the project directory and add your API key:
      ```
      OPENAI_API_KEY=your_openai_api_key
      ```

## Usage

1. **Run the Main Script:**
    ```bash
    python main.py
    ```

2. **Give Voice Commands:**
    - **Open Applications:** Say commands like "open YouTube" or "open Visual Studio Code".
    - **Ask Questions:** Ask any question you have, and the assistant will respond using OpenAI's API.
    - **Generate Python Code:** Ask the assistant to "write a Python program for the sum of two numbers," and it will create a text file with the question and the generated Python code.

## Example Commands

- "Open YouTube"
- "Open Visual Studio Code"
- "Write a Python program to calculate the sum of two numbers"

## Project Structure

```
AI-Voice-Assistant/
│
├── .gitignore
├── .env
├── README.md
├── requirements.txt
├── main.py
├── utils.py
└── generated_code/
    ├── example.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to OpenAI for providing the API used in this project.
```

### Summary of Features and Commands

- **Voice Commands:**
  - Open applications like YouTube and Visual Studio Code.
  - Interact with the user via natural language processing.
  - Generate Python code and save it to a text file.

### Commands Overview

- **Open Applications:**
  - "Open YouTube"
  - "Open Visual Studio Code"
- **Interact with AI:**
  - "What is the capital of France?"
  - "How do you make a cake?"
- **Generate Python Code:**
  - "Write a Python program for the sum of two numbers."
