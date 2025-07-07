from typing import List, Dict, Any

def generate_response(tasks: List[Dict[str, Any]], user_info: Dict[str, Any]) -> str:
    """Generate a friendly response with the study plan."""
    if not tasks:
        return "I'm sorry, I couldn't generate a study plan. Could you provide more details?"
    
    response = [f"I see you're feeling {user_info.get('mood', 'ready to study')} today. "
               f"Here's a study plan for {user_info.get('subject', 'your studies')}:"]
    
    for i, task in enumerate(tasks, 1):
        response.append(f"{i}. {task['task']} ({task['duration']} min) - {task['reason']}")
    
    # Add mood-appropriate encouragement
    mood = user_info.get('mood', '').lower()
    if 'tired' in mood:
        response.append("\nRemember, it's okay to take it easy. Small progress is still progress! 💪")
    elif 'focus' in mood:
        response.append("\nYou're doing great! Keep up the focused work! 🚀")
    else:
        response.append("\nYou've got this! Happy studying! ✨")
    
    return "\n".join(response)