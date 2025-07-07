import os
import logging
from dotenv import load_dotenv
import os

from huggingface_hub import HfFolder, InferenceClient

from config import SYSTEM_PROMPT
from state_manager import UserState
from input_understanding import understand_input
from task_planner import plan_tasks
from output_generator import generate_response

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    logging.error("Error: HF_TOKEN not found in .env file.")
    logging.error("Please make sure you have a .env file with HF_TOKEN=YOUR_API_KEY")
    exit()

# Save the token for transformers to use
HfFolder.save_token(HF_TOKEN)

# Initialize different model interaction methods
try:

    # Option 3: Using InferenceClient for API-based interaction
    client = InferenceClient(
        provider="fireworks-ai",
        api_key=os.environ["HF_TOKEN"],
    )
except Exception as e:
    logging.error(f"Error initializing model: {e}")
    logging.error("Please ensure the model 'deepseek-ai/DeepSeek-R1-0528' is accessible and your HF_TOKEN is valid.")
    exit()


def get_chatbot_response(messages: list[dict]) -> str:
    """
    Generates a response using the Hugging Face InferenceClient.
    """
    try:
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1-0528",
            messages=messages,
        )
        return completion.choices[0].message.content
    except Exception as e:
        logging.error(f"Error generating response with InferenceClient: {e}")
        return "An error occurred while generating the response. Please try again."


def main():
    """
    Main function to run the AI Study Planner Chatbot.
    Handles user input, conversation history, and chatbot responses.
    """
    user_state = UserState()
    messages: list[dict] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    logging.info("Welcome to the AI Study Planner Chatbot! Type 'quit' to exit.")

    while True:
        user_input: str = _get_user_input()
        if user_input.lower() == 'quit':
            logging.info("Exiting chatbot.")
            break

        _handle_user_message(messages, user_input)
        
        # Step 1: Input Understanding
        extracted_info = understand_input(user_input, lambda messages: get_chatbot_response(messages))

        # Step 2: State Tracking
        user_state.add_mood(extracted_info.get("mood", "neutral"))
        user_state.last_subject = extracted_info.get("subject", user_state.last_subject)

        # Step 3: Task Planning
        tasks = plan_tasks(extracted_info)

        # Step 4: Output Generation
        response_text = generate_response(tasks, extracted_info)
        
        # Use the LLM for conversational aspects if needed, or just rely on generated_response
        # For now, we'll just use the generated_response directly
        # If you want the LLM to refine the response, you'd pass response_text to get_chatbot_response
        # and then display that.
        
        _display_chatbot_response(messages, response_text)
        
        # Add the generated response to user_state for history
        user_state.add_suggestion(response_text)

def _get_user_input() -> str:
    """
    Gets input from the user.
    """
    return input("You: ")

def _handle_user_message(messages: list[dict], user_input: str) -> None:
    """
    Appends the user's message to the conversation history.
    """
    messages.append({"role": "user", "content": user_input})

def _display_chatbot_response(messages: list[dict], response: str) -> None:
    """
    Displays the chatbot's response and appends it to the conversation history.
    """
    logging.info(f"Chatbot: {response}")
    messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()

