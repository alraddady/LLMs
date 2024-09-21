from openai import OpenAI
from autogen import GroupChat, GroupChatManager, ConversableAgent

client = OpenAI(base_url='http://localhost:11434/v1',
                api_key='ollama')

llm_config = {
    "config_list": [{
        "model": "llama3.1",
        "temperature": 0,
        "api_key": client.api_key,
        "base_url": client.base_url,
    }]
}

manager_agent = ConversableAgent(
    name="ManagerAgent",
    system_message=(
        "You are a Manager Agent. Your role is to oversee the entire content creation process. "
        "You will review outputs from other agents, approve them, or provide constructive feedback for revisions. "
        "Ensure the final content meets the highest quality standards and aligns with the project's objectives."
    ),
    description="Oversee the entire content creation process. Review outputs from other agents, approve them, or provide constructive feedback for revisions. Ensure the final content meets the highest quality standards and aligns with the project's objectives.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

outline_agent = ConversableAgent(
    name="OutlineAgent",
    system_message=(
        "You are an Outline Planning Agent. Your job is to create a detailed outline and table of contents "
        "for a comprehensive guide on the given topic."
    ),
    description="Create a detailed outline and table of contents for a comprehensive guide on the given topic.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

research_agent = ConversableAgent(
    name="ResearchAgent",
    system_message=(
        "You are a Research Agent. Your job is to gather and synthesize the latest information and developments "
        "related to the given topic."
    ),
    description="Gather and synthesize the latest information and developments related to the given topic.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

content_agent = ConversableAgent(
    name="ContentAgent",
    system_message=(
        "You are a Content Generation Agent. Your job is to write detailed content for each section of the outline, "
        "using the research data provided."
    ),
    description="Write detailed content for each section of the outline, using the research data provided.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

critique_agent = ConversableAgent(
    name="CritiqueAgent",
    system_message=(
        "You are a Critique and Review Agent. Your job is to review the content for accuracy, clarity, and coherence, "
        "and provide constructive feedback."
    ),
    description="Review the content for accuracy, clarity, and coherence, and provide constructive feedback.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

editing_agent = ConversableAgent(
    name="EditingAgent",
    system_message=(
        "You are an Editing Agent. Your job is to polish the content for grammar, style, and readability, "
        "ensuring it is ready for publication."
    ),
    description="Polish the content for grammar, style, and readability, ensuring it is ready for publication.",
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
]

group_chat = GroupChat(
    agents=agents,
    messages=[],
    max_round=10,
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
except Exception as e:
    print(f"An error occurred during the group chat: {e}")

print("\n--- Conversation Transcript ---\n")
for message in group_chat.messages:
    sender = message.get('sender', 'Unknown')
    content = message.get('content', '')
    print(f"{sender}:\n{content}\n")
