from typing import List, Dict, Any

def plan_tasks(extracted_info: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Generate study tasks based on user's mood and preferences."""
    try:
        mood = extracted_info.get("mood", "neutral")
        subject = extracted_info.get("subject", "your studies")
        time_min = extracted_info.get("time_minutes", 30)
        
        # Mood-based task planning
        if mood == "tired":
            return [
                {
                    "task": f"Watch a short video lecture about {subject}",
                    "duration": min(15, time_min),
                    "reason": "Video content is less demanding when you're feeling tired."
                },
                {
                    "task": f"Review your notes on {subject} for key concepts",
                    "duration": min(20, time_min),
                    "reason": "Passive review is effective when energy is low."
                }
            ]
        else:  # focused or neutral
            return [
                {
                    "task": f"Solve practice problems on {subject}",
                    "duration": min(25, time_min),
                    "reason": "Active recall is great when you're feeling focused."
                },
                {
                    "task": f"Create flashcards for {subject}",
                    "duration": min(20, time_min),
                    "reason": "Creating study aids helps reinforce learning."
                }
            ]
    except Exception as e:
        # In a real application, you'd want more sophisticated error handling
        print(f"Error in task planning: {e}")
        return []