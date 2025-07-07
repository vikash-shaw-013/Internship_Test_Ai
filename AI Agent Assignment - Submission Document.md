Absolutely! Here's a template + completed example for your AI Agent Assignment, filled out using a simple and meaningful use case:

# AI Agent Assignment – Submission Document

## 🧾 SECTION 1: BASIC DETAILS
- **Name**: [Your Name]
- **AI Agent Title**: "AI Study Planner"
- **Use Case**: AI Agent to help college students plan effective study sessions based on their current mood and energy levels

## 🧠 SECTION 2: PROBLEM FRAMING

### 2.1 What problem does your AI Agent solve?
College students often struggle to match their study tasks with their current energy levels and mood, leading to inefficient study sessions and burnout. This agent helps students make the most of their study time by suggesting appropriate study activities based on their current state of mind.

### 2.2 Why is this agent useful?
- Provides personalized study suggestions based on real-time mood and energy levels
- Helps students stay productive even when not feeling 100%
- Reduces decision fatigue by providing clear, actionable study tasks
- Encourages better study habits through adaptive recommendations

### 2.3 Who is the target user?
- University and college students
- Self-learners managing multiple subjects
- Students preparing for exams or working on projects
- Anyone looking to optimize their study sessions based on their mental state

### 2.4 What not to include?
- Subject-specific tutoring or academic help
- Mental health diagnosis or therapy
- Rigid scheduling or time management
- Detailed subject matter explanations
- Account creation or personal data storage

## 🧱 SECTION 3: 4-LAYER PROMPT DESIGN
🔹 3.1 INPUT UNDERSTANDING
Prompt:

"You are a user assistant. Given a user message, identify the following:

Mood (if stated) – e.g., tired, focused, distracted

Subject preferences (e.g., 'math', 'history')

Time available (if given)

Study goal (e.g., revise, practice, read)

Output a structured summary with these fields."

What is this prompt responsible for?
Extract user’s mood, goals, and constraints so the agent can personalize its suggestion.

Example Input + Output:

Input: "I'm feeling really tired but need to study math for 30 minutes"
Output: `{'mood': 'tired', 'subject': 'math', 'time_minutes': 30, 'goal': 'study'}`




🔹 3.2 STATE TRACKER


How does this help the agent "remember"?
- Maintains conversation context across interactions
- Tracks mood history to identify patterns
- Remembers recent suggestions to avoid repetition
- Stores the last subject studied for continuity

Example State After Several Interactions:


🔹 3.3 TASK PLANNER


Key Features:
- **Mood-Adaptive**: Suggests different study techniques based on energy levels
- **Time-Aware**: Adjusts task duration based on available time
- **Subject-Specific**: Personalizes suggestions based on the subject being studied
- **Balanced Workload**: Mixes different types of cognitive load

Example Output for Tired Mood:


🔹 3.4 OUTPUT GENERATOR


Key Features:
- **Personalized Greeting**: Acknowledges the user's current state
- **Structured Format**: Clear numbering and organization of tasks
- **Contextual Encouragement**: Changes closing message based on mood
- **Readable Output**: Clean formatting with emojis for better engagement

Example Output for Tired Mood:
```
Here's a study plan for math:

1. Watch a short video lecture about math (15 min) - Video content is less demanding when you're feeling tired.
2. Review your notes on math for key concepts (15 min) - Passive review is effective when energy is low.
```

Example Output for Focused Mood:
```
Here's a study plan for physics:

1. Solve practice problems on physics (25 min) - Active recall is great when you're feeling focused.
2. Create flashcards for physics (20 min) - Creating study aids helps reinforce learning.
```

## 🔍 SECTION 4: CHATGPT EXPLORATION LOG

| Attempt | Prompt Variant | What Happened | What You Changed | Why |
|---------|----------------|----------------|------------------|-----|
| 1 | Basic mood-based study suggestions | Generic recommendations, no personalization | Added subject and time parameters | Needed more context for relevant suggestions |
| 2 | Added time constraints | Tasks weren't properly time-boxed | Implemented duration-based task selection | To ensure tasks fit available study time |
| 3 | Complex state tracking | State became inconsistent | Simplified to track only essential variables | To improve reliability and maintainability |
| 4 | Final implementation | Working as intended | Added error handling and edge cases | For robustness in real-world usage |

## 🧪 SECTION 5: OUTPUT TESTS

### Test 1: Normal input with tired mood
**Input**: "I'm feeling really tired but need to study math for 30 minutes"

**Output**:
```
Here's a study plan for math:

1. Watch a short video lecture about math (15 min) - Video content is less demanding when you're feeling tired.
2. Review your notes on math for key concepts (15 min) - Passive review is effective when energy is low.
```

### Test 2: Focused with subject but no time specified
**Input**: "I'm feeling focused and want to review physics"

**Output**:
```
Here's a study plan for physics:

1. Solve practice problems on physics (25 min) - Active recall is great when you're feeling focused.
2. Create flashcards for physics (20 min) - Creating study aids helps reinforce learning.
```

### Test 3: Vague input
**Input**: "I don't know what to study"

**Output**:
```
I'm here to help you plan your study session! Could you tell me:
1. How are you feeling right now? (e.g., tired, focused, distracted)
2. Any particular subject you'd like to work on?
3. How much time do you have available?

This will help me suggest the best study activities for you! 😊
```

## 🔄 SECTION 6: REFLECTION

### 6.1 What was the hardest part of this assignment?
The most challenging aspect was designing the state management system to maintain context across multiple interactions while keeping the implementation simple and maintainable. Balancing functionality with simplicity required several iterations.

### 6.2 What part did you enjoy the most?
I particularly enjoyed designing the task planning logic that adapts to different moods and energy levels. Seeing how small adjustments in the prompts could significantly impact the quality and relevance of study suggestions was fascinating.

### 6.3 If given more time, what would you improve or add?
- Implement a more sophisticated natural language understanding system
- Add progress tracking for study sessions
- Include more detailed feedback mechanisms
- Develop a simple web interface for better accessibility
- Add support for multiple study subjects and sessions

### 6.4 What did you learn about ChatGPT or prompt design?
- Clear, specific prompts yield better results than vague ones
- Breaking down complex tasks into smaller, focused prompts improves reliability
- The importance of context windows and how to manage them effectively
- How to structure stateful conversations with clear transitions

### 6.5 Did you ever feel stuck? How did you handle it?
Yes, particularly when trying to balance flexibility with structure in the task planning. I handled it by:
1. Breaking the problem into smaller, testable components
2. Creating specific test cases for different scenarios
3. Iterating on the prompt design based on test results
4. Consulting documentation and examples for inspiration

## 🧠 SECTION 7: HACK VALUE

### Key Innovations:
1. **Adaptive Task Planning**
   - Considers time constraints to suggest realistic, achievable tasks

2. **Context-Aware Responses**
   - Maintains conversation context across multiple turns
   - Adapts tone and encouragement based on user's mood

3. **Modular Architecture**
   - Clear separation of concerns between input processing, state management, task planning, and response generation
   - Makes the system more maintainable and extensible

4. **Progressive Enhancement**
   - Graceful degradation when information is missing
   - Helps guide users to provide better input

5. **State Persistence**
   - Maintains session state to provide continuity in conversations
   - Tracks mood history to identify patterns over time

Let me know if you'd like this as a downloadable document or want to build your own version from this format!