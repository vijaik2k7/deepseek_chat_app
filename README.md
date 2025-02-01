# DeepSeek R1 Chatbot with Streamlit and Ollama

This project provides a simple and user-friendly chat interface powered by the DeepSeek R1 (1.5B) language model, running locally using Ollama. It's built using Streamlit for the UI and Ollama to serve the DeepSeek R1 model.

![Streamlit Chat App Screenshot](streamlit_deepseek_ui.png) <!-- Replace with a screenshot if you have one -->

## Features

*   **Local LLM Chat:**  Interact with the DeepSeek R1 model directly on your machine without relying on external APIs.
*   **Streamlit UI:**  Intuitive and easy-to-use chat interface built with Streamlit.
*   **Chat History:**  Maintains chat history within the session for a continuous conversation.
*   **Typing Effect:**  Simulates a typing effect for the assistant's responses, enhancing user experience.
*   **Easy Setup:**  Quick to set up and run with minimal dependencies.

## Prerequisites

Before you begin, ensure you have the following installed and set up:

1.  **Ollama:**
    *   Follow the installation instructions for your operating system on the [Ollama website](https://ollama.com/).
    *   Verify Ollama is running and accessible.

2.  **DeepSeek R1 Model in Ollama (check other model options on [Ollama website]((https://ollama.com/library/deepseek-r1))):**
    *   Pull the `deepseek-r1:1.5B` model using Ollama:
        ```bash
        ollama pull deepseek-r1:1.5B
        ```

3.  **Python 3.8+:**
    *   Ensure you have Python 3.8 or later installed.

4.  **Python Libraries:**
    *   Install the required Python libraries using pip:
        ```bash
        pip install streamlit ollama
        ```

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/vijaik2k7/deepseek_chat_app.git
    ```

2.  **Navigate to the Project Directory:**
    ```bash
    cd deepseek_chat_app
    ```

3.  **Run the Streamlit App:**
    ```bash
    streamlit run deepseek_chat_app.py
    ```

    This command will start the Streamlit application, and it will automatically open in your default web browser (usually at `http://localhost:8501`).

## Usage

1.  **Access the App:** Open your web browser and go to the address displayed in the terminal (typically `http://localhost:8501`).

2.  **Start Chatting:**  Type your messages in the "What's up?" input box at the bottom of the screen and press Enter or click the send button.

3.  **View Responses:** The app will display your messages and the responses from the DeepSeek R1 model in a chat-like format. The assistant's responses will appear with a typing effect.

4.  **Continue the Conversation:**  Keep typing messages to continue the conversation. The chat history is maintained within the current session.

## Customization

You can easily customize and enhance this chat application:

*   **Model Selection:** Modify the code to allow users to choose from different models available in Ollama through a dropdown menu.
*   **System Prompt:**  Add an input field to set a custom system prompt or initial context for the conversation to guide the model's behavior.
*   **Model Parameters:** Expose parameters like `temperature`, `top_p`, etc., from the `ollama.chat()` function as sliders or input fields in the Streamlit app to control the model's generation style.
*   **Styling:**  Customize the look and feel of the Streamlit app using Streamlit's theming options or custom CSS.
*   **Clear History Button:** Implement a button to clear the chat history and start a fresh conversation.
*   **Error Handling:**  Enhance error handling to gracefully manage potential issues with Ollama or network connections.

## License

[MIT License](LICENSE)  

## Author

[vijaik2k7]

---

Feel free to contribute to this project or use it as a starting point for your own local LLM applications!
