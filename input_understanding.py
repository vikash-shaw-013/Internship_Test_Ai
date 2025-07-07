from typing import Dict, Any, Callable
import json
import logging
import re

def understand_input(user_message: str, llm_response_func: Callable[[list[dict]], str]) -> Dict[str, Any]:
    """
    Extracts user's mood, subject, time, and goal from the message using an LLM.

    Args:
        user_message: The raw input message from the user.
        llm_response_func: A function that takes a list of message dictionaries
                           and returns a string response from the LLM.

    Returns:
        A dictionary containing the extracted information.
    """
    system_prompt = (
        "You are a user assistant. Your task is to extract specific information "
        "from the user's message and output it as a JSON object. "
        "Identify the following:\n"
        "- 'mood': (e.g., 'tired', 'focused', 'distracted', 'energetic', 'neutral') - if stated or implied.\n"
        "- 'subject': (e.g., 'math', 'physics', 'history', 'programming') - if mentioned.\n"
        "- 'time_minutes': (integer) - time available for study in minutes, if specified. Default to 30 if not found.\n"
        "- 'goal': (e.g., 'revise', 'practice', 'read', 'learn', 'study') - if stated or implied. Default to 'study'.\n"
        "Ensure the output is a valid JSON object with these keys. If a field is not found, use the default or an empty string/appropriate default value.\n"
        "Your response MUST be ONLY the JSON object, enclosed in a markdown code block like this: ```json\n{...}\n```\n"
        "Example:\n"
        "User: 'I'm feeling really tired but I need to study math for 30 minutes'\n"
        "Output: ```json\n{\"mood\": \"tired\", \"subject\": \"math\", \"time_minutes\": 30, \"goal\": \"study\"}\n```\n"
        "User: 'I want to review physics'\n"
        "Output: ```json\n{\"mood\": \"neutral\", \"subject\": \"physics\", \"time_minutes\": 30, \"goal\": \"review\"}\n```\n"
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    try:
        llm_raw_response = llm_response_func(messages)
        # Extract JSON string using regex
        json_match = re.search(r'```json\n([\s\S]*?)\n```', llm_raw_response)
        if json_match:
            json_string = json_match.group(1)
        else:
            # Fallback if markdown code block is not found, try to parse the whole response
            json_string = llm_raw_response

        extracted_info = json.loads(json_string)
        # Validate keys
        default_info = {
            "mood": "neutral",
            "subject": "your studies",
            "time_minutes": 30,
            "goal": "study"
        }
        for key, default_val in default_info.items():
            if key not in extracted_info:
                extracted_info[key] = default_val
        return extracted_info
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse LLM response as JSON: {e}. Raw response: {llm_raw_response}")
        # Fallback to a simpler extraction or default values if LLM fails to output valid JSON
        return {
            "mood": "neutral",
            "subject": "your studies",
            "time_minutes": 30,
            "goal": "study"
        }
    except Exception as e:
        logging.error(f"Error in understand_input: {e}")
        return {
            "mood": "neutral",
            "subject": "your studies",
            "time_minutes": 30,
            "goal": "study"
        }