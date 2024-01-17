# ------------------------------
#  Python Imports
# ------------------------------

# ------------------------------
#  External Imports
# ------------------------------
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# ------------------------------
#  Module Imports
# ------------------------------


# ------------------------------
#  Error Classes
# ------------------------------


load_dotenv()

PROMPT = """Create a conversation between a curious user and an AI chatbot with a
                focus on science. The user asks a series of questions related to various
                scientific topics, and the AI is programmed to provide concise and informative responses.
                Each answer should be kept short and to the point, maintaining a conversational tone.
                The topics should cover a range of scientific disciplines, including physics, biology,
                chemistry, and astronomy. Ensure the AI delivers accurate and simplified explanations
                for each question. The goal is to create an engaging and educational interaction."""

# Instantiate a ChatOpenAI object for managing interactions with the OpenAI API
llm = ChatOpenAI()

# Define a ChatPromptTemplate for constructing the input prompt to OpenAI
prompt = ChatPromptTemplate(
    messages=[
        # Include a system message prompt (e.g., initial instructions or context)
        SystemMessagePromptTemplate.from_template(PROMPT),

        # Use a placeholder for the chat history variable
        MessagesPlaceholder(variable_name="chat_history"),

        # Include a template for the user's question
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
)

# Create a ConversationBufferMemory to store and retrieve the chat history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


def generate_response(query: str) -> str:
    # Instantiate an LLMChain for managing the conversation flow
    conversation = LLMChain(llm=llm, prompt=prompt, verbose=False, memory=memory)

    # Generate a response by providing the user's question in the conversation context
    response = conversation({"question": query})["text"]

    # Return the generated response
    return response
