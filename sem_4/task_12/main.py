from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableSequence
import requests
import os

class ContextAwareChatBot:
    def __init__(self, api_key: str, api_url: str, model_name="gemini-1.5-flash", temperature=0.7):
        os.environ["GOOGLE_API_KEY"] = api_key
        self.api_url = api_url
        self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=temperature)

        # Memory for context tracking
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # Template with dynamic input
        self.prompt = PromptTemplate(
            input_variables=["chat_history", "user_input", "external_data"],
            template=(
                "You are a helpful assistant. Use the following chat history and external data.\n\n"
                "Chat History:\n{chat_history}\n\n"
                "External Data:\n{external_data}\n\n"
                "User: {user_input}\n"
                "Assistant:"
            )
        )

        # Create a RunnableSequence instead of LLMChain
        self.chain = RunnableSequence(self.prompt | self.llm)

    def fetch_external_data(self, params=None) -> str:
        if not self.api_url:
            return "No external data available"
        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            return str(response.json())
        except Exception as e:
            return f"Error fetching external data: {e}"

    def chat(self, user_input: str, params=None) -> str:
        # Fetch external data
        external_data = self.fetch_external_data(params)

        # Load chat history from memory
        chat_history = self.memory.load_memory_variables({})["chat_history"]

        # Invoke the chain with all required inputs
        response = self.chain.invoke({
            "user_input": user_input,
            "external_data": external_data,
            "chat_history": chat_history
        })

        # Save the user input and response to memory
        self.memory.save_context({"user_input": user_input}, {"output": response.content})

        return response.content

# Example usage

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/users"
    api_key = "AIzaSyDoYadqvVQWf2uEhZwLp3RiH3RGCmuDcIo"

    try:
        chatbot = ContextAwareChatBot(api_key=api_key, api_url=api_url)
        # Pass params to filter users with username="Bret"
        params = {"username": "Bret"}
        response = chatbot.chat("What data do you have", params=params)
        print(response)
    except Exception as e:
        print(f"Error: {e}")