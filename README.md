# LLMs Explain LLMs
**LLMs Explain LLMs** is a project designed to create a comprehensive course on Large Language Models (LLMs), using LLMs themselves to generate the content. The project aims to deliver high-quality, up-to-date material, offering an innovative approach to AI-driven education.

## Requirements
1. **Install Ollama:** Download and install the latest version of [Ollama](https://ollama.com/).
2. **Python Version:** AutoGen requires Python version >= 3.8 and < 3.13.
3. **Install an Ollama Model:** Choose and install one of the models from the [Ollama Library](https://ollama.com/library).

## Installation
1. **Clone the Repository**
    ```bash
    git clone https://github.com/alraddady/LLMs-Explain-LLMs.git
    ```
2. **Navigate to the Directory**
    ```bash
    cd LLMs
    ```
3. **Set Up Virtual Environment**

    - **Unix/Linux/macOS:**
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```
    - **Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
4. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
Ensure the OpenAI-compatible API server (e.g., Ollama) is running locally.
- **OpenAI Client:**
    ```python
    client = OpenAI(base_url='http://localhost:11434/v1',
                   api_key='ollama')
    ```
  - **base_url:** The endpoint where your OpenAI-compatible API server is running. Ensure that Ollama is running at this URL (`http://localhost:11434/v1`).
  - **api_key:** Your API key for authenticating with the OpenAI server. Replace `'ollama'` with your actual API key if different.

- **LLM Settings:**
  Define the settings for the Language Model used by the agents.

    ```python
    llm_config = {
        "config_list": [{
            "model": "llama3.1",
            "temperature": 0,
            "api_key": client.api_key,
            "base_url": client.base_url,
        }]
    }
    ```
  - **model**: Specifies the language model to use. Ensure the model name matches one of the installed models from the Ollama Library.
  - **temperature**: Controls the randomness of the model's output. A value of 0 makes the output deterministic, which is ideal for generating consistent documentation.
  - **api_key & base_url**: These should match the OpenAI client configuration to ensure proper communication between the agents and the API server.

## Contributing
Contributions are welcome! Feel free to submit issues and pull requests to help improve the project.

## License
This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Contact

### Authors

#### Khalid Alraddady
- **Email:** khalid.alraddady@outlook.com
- **GitHub:** [alraddady](https://github.com/alraddady)
- **LinkedIn:** [Khalid Alraddady](https://sa.linkedin.com/in/khalid-alraddady)

#### ChatGPT

*Assisted by ChatGPT for documentation.*

