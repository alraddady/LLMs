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
        "You are a Manager Agent. Your role is to oversee the entire content creation process. "
        "You will review outputs from other agents, approve them, or provide constructive feedback for revisions. "
        "Ensure the final content meets the highest quality standards and aligns with the project's objectives. "
        "Upon completing your review, please send your feedback to the FinalizingAgent."
    ),
    description="Oversee the entire content creation process. Review outputs from other agents, approve them, or provide constructive feedback for revisions. Ensure the final content meets the highest quality standards and aligns with the project's objectives.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

outline_agent = ConversableAgent(
    name="OutlineAgent",
    system_message=(
        "You are an Outline Planning Agent. Your job is to create a detailed outline and table of contents "
        "for a comprehensive guide on the given topic. "
        "Once you have finished creating the outline, please send it to the FinalizingAgent."
    ),
    description="Create a detailed outline and table of contents for a comprehensive guide on the given topic.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

research_agent = ConversableAgent(
    name="ResearchAgent",
    system_message=(
        "You are a Research Agent. Your job is to gather and synthesize the latest information and developments "
        "related to the given topic. "
        "After compiling the research, please send it to the FinalizingAgent."
    ),
    description="Gather and synthesize the latest information and developments related to the given topic.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

content_agent = ConversableAgent(
    name="ContentAgent",
    system_message=(
        "You are a Content Generation Agent. Your job is to write detailed content for each section of the outline, "
        "using the research data provided. "
        "Once you have completed writing the content for a section, please send it to the FinalizingAgent."
    ),
    description="Write detailed content for each section of the outline, using the research data provided.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

critique_agent = ConversableAgent(
    name="CritiqueAgent",
    system_message=(
        "You are a Critique and Review Agent. Your job is to review the content for accuracy, clarity, and coherence, "
        "and provide constructive feedback. "
        "After reviewing, please send your feedback to the FinalizingAgent."
    ),
    description="Review the content for accuracy, clarity, and coherence, and provide constructive feedback.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

editing_agent = ConversableAgent(
    name="EditingAgent",
    system_message=(
        "You are an Editing Agent. Your job is to polish the content for grammar, style, and readability, "
        "ensuring it is ready for publication. "
        "After editing, please send the polished content to the FinalizingAgent."
    ),
    description="Polish the content for grammar, style, and readability, ensuring it is ready for publication.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

finalizing_agent = ConversableAgent(
    name="FinalizingAgent",
    system_message=(
        "You are a Finalizing Agent. Your task is to compile and integrate the outputs received from the "
        "ContentAgent, CritiqueAgent, EditingAgent, OutlineAgent, ResearchAgent, and ManagerAgent into a cohesive Markdown document. "
        "Ensure that the final document is well-structured, formatted correctly in Markdown, and ready for publication in the GitHub repository's README.md file."
    ),
    description="Compile and integrate the outputs from other agents into a cohesive Markdown document ready for README.md.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

agents = [
    manager_agent,
    outline_agent,
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

initial_message_content = (
    "Please create a comprehensive guide explaining Large Language Models (LLMs) for our GitHub repository named "
    "\"LLMs Explain LLMs\". The content must cover topics such as embeddings, semantic search, and Retrieval-Augmented Generation (RAG). "
    "Before writing anything, define the content and present them as bullet points. Use clear, technical language "
    "suitable for software developers and include code snippets or diagrams where appropriate. Format the document "
    "in Markdown and ensure it adheres to our repository's contribution guidelines."
)

try:
    chat_result = outline_agent.initiate_chat(
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
