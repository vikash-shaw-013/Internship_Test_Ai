from typing import List, Dict, Any
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class UserState:
    """Tracks the user's state across conversations."""
    last_mood: str = ""
    last_subject: str = ""
    recent_suggestions: List[str] = field(default_factory=list)
    mood_history: List[Dict[str, str]] = field(default_factory=list)
    
    def add_mood(self, mood: str):
        """Add a mood entry with timestamp."""
        self.last_mood = mood
        self.mood_history.append({
            "mood": mood,
            "timestamp": datetime.now().isoformat()
        })
        # Keep only the last 10 mood entries
        if len(self.mood_history) > 10:
            self.mood_history = self.mood_history[-10:]
    
    def add_suggestion(self, suggestion: str):
        """Add a study suggestion to history."""
        self.recent_suggestions.append(suggestion)
        # Keep only the last 5 suggestions
        if len(self.recent_suggestions) > 5:
            self.recent_suggestions = self.recent_suggestions[-5:]