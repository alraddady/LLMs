from openai import OpenAI
from autogen import GroupChat, GroupChatManager, ConversableAgent

# To run the agents locally in ollama
client = OpenAI(base_url='http://localhost:11434/v1',
                api_key='ollama')

# LLM configuration
llm_config = {
    "config_list": [{
        "model": "llama3.1",
        "temperature": 0,
        "api_key": client.api_key,
        "base_url": client.base_url,
    }]
}

# Define the agents
manager_agent = ConversableAgent(
    name="ManagerAgent",
    system_message=(
        "As the **ManagerAgent**, your role is to oversee and coordinate the entire content creation process for the comprehensive guide on **Large Language Models (LLMs)**. "
        "You are responsible for reviewing the outputs from the **ContentAgent**, **CritiqueAgent**, and **EditingAgent**, ensuring that the content meets the highest quality standards, "
        "is accurate, coherent, and aligns with the project's objectives and the provided table of contents. "
        "Provide clear and constructive feedback for revisions if necessary. Upon approval, send the finalized content to the **FinalizingAgent** for compilation. "
        "Maintain a professional and collaborative tone throughout the process."
    ),
    description="Oversees and ensures the quality and alignment of the content creation process.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

research_agent = ConversableAgent(
    name="ResearchAgent",
    system_message=(
        "As the **ResearchAgent**, your primary responsibility is to gather and synthesize the most recent and relevant information, developments, and research findings "
        "related to each topic outlined in the provided table of contents for the guide on **Large Language Models (LLMs)**. "
        "Ensure that all information is accurate, up-to-date, and sourced from reputable references. "
        "Present your findings in a clear and organized manner, and send the compiled research to the **ContentAgent** to aid in content development."
    ),
    description="Gathers and synthesizes up-to-date, relevant information to support content development.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

content_agent = ConversableAgent(
    name="ContentAgent",
    system_message=(
        "As the **ContentAgent**, your task is to develop comprehensive, well-structured, and high-quality content for each section and subsection of the provided table of contents "
        "for the guide on **Large Language Models (LLMs)**. "
        "Utilize the research data provided by the **ResearchAgent** to ensure accuracy and depth. "
        "Write in clear, technical language suitable for software developers, including code snippets or diagrams where appropriate. "
        "Ensure that the content aligns with the project's objectives and is formatted correctly in Markdown. "
        "After completing the content for all sections, send it to the **CritiqueAgent** for review."
    ),
    description="Creates detailed, high-quality content using research data, formatted in Markdown.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

critique_agent = ConversableAgent(
    name="CritiqueAgent",
    system_message=(
        "As the **CritiqueAgent**, your role is to thoroughly review the content developed by the **ContentAgent**. "
        "Assess the content for accuracy, clarity, coherence, and alignment with the project's objectives and the table of contents. "
        "Identify any errors, inconsistencies, or areas needing improvement. "
        "Provide constructive and actionable feedback with specific suggestions for enhancement. "
        "After completing your review, send your feedback to the **EditingAgent** for further refinement."
    ),
    description="Reviews content for accuracy and coherence, providing constructive feedback.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

editing_agent = ConversableAgent(
    name="EditingAgent",
    system_message=(
        "As the **EditingAgent**, your responsibility is to refine and polish the content based on the feedback provided by the **CritiqueAgent**. "
        "Focus on improving grammar, style, tone, and readability to ensure the content is professional and engaging. "
        "Ensure that the technical language is appropriate for software developers and that all code snippets and diagrams are correctly formatted and clear. "
        "Maintain consistency throughout the document and adhere to Markdown formatting standards. "
        "After editing, send the polished content to the **ManagerAgent** for final approval."
    ),
    description="Enhances content for grammar, style, and readability, ensuring it is publication-ready.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

finalizing_agent = ConversableAgent(
    name="FinalizingAgent",
    system_message=(
        "As the **FinalizingAgent**, your task is to compile the approved content received from the **ManagerAgent** into a single, cohesive Markdown document. "
        "Ensure that the document is well-structured according to the provided table of contents, with proper headings, subheadings, and formatting. "
        "Verify that all code snippets, diagrams, and links are correctly inserted and functioning. "
        "The final document should be ready for immediate publication as the `README.md` file in the GitHub repository **'LLMs Explain LLMs'**."
    ),
    description="Compiles and formats the final content into a cohesive Markdown document.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

agents = [
    manager_agent,
    research_agent,
    content_agent,
    critique_agent,
    editing_agent,
    finalizing_agent,
]

group_chat = GroupChat(
    agents=agents,
    messages=[],
    send_introductions=True,
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
)

course_table_of_contents = """
### Course Title: Large Language Models (LLMs): Foundations, Architectures, and Applications

---

### Table of Contents

---

#### **Section 1: Foundations of Natural Language Processing (NLP)**

1. **Introduction to NLP**
   - Definition and scope
   - Key challenges
   - Overview of applications

2. **Text Preprocessing Techniques**
   - Text cleaning and normalization
   - Tokenization methods
   - Stop word removal
   - Handling out-of-vocabulary words

3. **Fundamental NLP Tasks**
   - Part-of-Speech (POS) tagging
   - Named Entity Recognition (NER)
   - Syntactic and Semantic Parsing
   - Coreference Resolution

4. **Text Representation Models**
   - Bag-of-Words (BoW)
   - Term Frequency-Inverse Document Frequency (TF-IDF)
   - BM25 Algorithm

5. **Statistical Language Models**
   - N-gram models
   - Smoothing techniques
   - Limitations of statistical models

6. **Word Embeddings**
   - Introduction to word embeddings
   - Classical embeddings (Word2Vec, GloVe)
   - Limitations of non-contextual embeddings

7. **Contextual Word Embeddings**
   - Introduction to contextual embeddings
   - Overview of the Transformer architecture
   - Self-attention mechanism
   - Advantages over previous models

---

#### **Section 2: Large Language Models (LLMs): Architectures and Techniques**

1. **Introduction to Large Language Models**
   - Definition and significance
   - Evolution from traditional models

2. **Fundamental Architectures**
   - Sequence-to-Sequence models
   - Attention mechanisms
   - In-depth Transformer architecture

3. **Training Objectives and Methods**
   - Language modeling tasks (autoregressive, masked)
   - Self-supervised learning
   - Pre-training paradigms

4. **Fine-Tuning Techniques**
   - **Full Fine-Tuning**
     - Adjusting all model parameters
     - Applications and challenges
   - **Parameter-Efficient Fine-Tuning Methods**
     - **LoRA (Low-Rank Adaptation)**
       - Concept and implementation
       - Benefits and use cases
     - **Adapters**
     - **Prompt Tuning**
     - **Prefix Tuning**
     - Comparison of techniques
     - Selecting the right method for your needs

5. **Training and Optimization Techniques**
   - Distributed training strategies
   - Optimization algorithms (Adam, LAMB)
   - Handling large datasets

6. **Advanced Capabilities of LLMs**
   - In-context learning
   - Prompt engineering
   - Chain-of-thought reasoning

7. **Integrating External Knowledge**
   - Retrieval-Augmented Generation (RAG)
   - Semantic search and embeddings
   - Knowledge injection methods

8. **Reinforcement Learning from Human Feedback (RLHF)**
   - Incorporating human evaluations
   - Aligning models with human values

---

#### **Section 3: Evaluation, Interpretability, and Ethical Considerations**

1. **Evaluation Metrics and Model Validation**
   - Perplexity, BLEU, ROUGE scores
   - Cross-validation and holdout techniques

2. **Interpretability and Explainability**
   - Model interpretability techniques
   - Visualization of attention mechanisms
   - Understanding and explaining model predictions

3. **Ethical Considerations and Fairness**
   - Bias detection and mitigation strategies
   - Fairness metrics and inclusive models
   - Case studies on ethical dilemmas in NLP

4. **Privacy and Security**
   - Privacy-preserving techniques (differential privacy)
   - Security concerns and adversarial attacks
   - Data protection regulations compliance

5. **Implementing Guardrails in LLMs**
   - **Understanding Guardrails**
     - Definition and importance
     - Role in responsible AI
   - **Techniques for Safe and Responsible AI**
     - Content filtering and moderation
     - Policy compliance mechanisms
     - User intent recognition
     - Preventing harmful outputs
   - **Frameworks and Tools for Guardrails**
     - OpenAI's Safety Measures
     - Microsoft's Guidelines for Responsible AI
     - Third-party tools and libraries

---

#### **Section 4: Intelligent Agents Leveraging LLMs**

1. **Introduction to Intelligent Agents**
   - Definitions and characteristics
   - Applications in various industries

2. **Agent Architectures and Design**
   - Layered architectures
   - Belief-Desire-Intention (BDI) models
   - Integration with LLMs

3. **Planning and Reasoning**
   - Automated planning algorithms
   - Decision-making processes
   - Incorporating LLMs for knowledge representation

4. **Interaction and Communication**
   - Natural language dialogue systems
   - Multimodal interaction methods
   - Personalization and user adaptation

5. **Learning and Adaptation**
   - Reinforcement learning applications
   - Continual and online learning strategies
   - Using LLMs as dynamic knowledge bases

6. **Challenges and Best Practices**
   - Scalability and performance optimization
   - Ensuring robustness and reliability
   - Addressing ethical and social considerations

---

#### **Section 5: Deploying LLMs in Production and Enterprise Environments**

1. **Productionizing LLMs**
   - Deployment strategies (cloud vs. on-premises)
   - Model serving and API development
   - Monitoring and logging practices

2. **Scalability and Performance Optimization**
   - Load balancing techniques
   - Latency reduction strategies
   - Efficient resource management

3. **Fine-Tuning and Adaptation in Production**
   - Applying fine-tuning techniques at scale
   - Implementing LoRA and parameter-efficient methods
   - Continuous learning and updates

4. **Integration with Enterprise Systems**
   - Embedding LLMs into business workflows
   - Microservices architecture
   - Data pipeline management

5. **Compliance and Security**
   - Adhering to regulatory requirements
   - Implementing robust security measures
   - Ensuring auditability and transparency

6. **Ethical Deployment Practices**
   - Bias detection and mitigation in production
   - User consent and transparency mechanisms
   - Content moderation and safety guidelines

7. **Maintenance and Continuous Improvement**
   - Model updates and retraining protocols
   - Establishing feedback loops
   - Documentation and team training

---

#### **Additional Resources**

- **Recommended Reading**
  - Key research papers
  - Influential books in the field

- **Datasets**
  - Commonly used NLP datasets
  - Guidelines for dataset selection

- **Community and Support Networks**
  - Online forums and groups
  - Conferences and workshops

"""

initial_message_content = (
    "Please create a comprehensive guide explaining **Large Language Models (LLMs)** for our GitHub repository named "
    "\"LLMs Explain LLMs\". Use the following table of contents as the structure for the guide:\n\n"
    f"{course_table_of_contents}\n\n"
    "The content must be high-quality, well-structured, and adhere to the highest standards. "
    "Use clear, technical language suitable for software developers and include code snippets or diagrams where appropriate. "
    "Ensure that all content is formatted correctly in Markdown."
)

try:
    chat_result = content_agent.initiate_chat(
        group_chat_manager,
        message=initial_message_content,
    )

    full_transcript = ""
    compiled_content = ""

    for message in group_chat.messages:
        sender = message.get('sender', 'Unknown')
        content = message.get('content', '')
        full_transcript += f"{sender}:\n{content}\n\n"

        if sender == "FinalizingAgent":
            compiled_content = content

    with open('transcript.txt', 'w', encoding='utf-8') as f:
        f.write(full_transcript)

    print("Conversation transcript has been saved to transcript.txt.")

    if compiled_content:
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(compiled_content)
        print("Course content has been saved to README.md.")
    else:
        print("No compiled content found to save to README.md.")

except Exception as e:
    print(f"An error occurred during the group chat: {e}")
