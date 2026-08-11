import random

def generate_ai_response(topic: str) -> str:
    """
    Simulates an AI agent generating a response based on a given topic.
    This represents the 'student AI' doing its 'homework'.
    """
    templates = {
        "cat": [
            "A fluffy cat is sleeping peacefully on the couch.",
            "The cat chased a laser pointer across the room.",
            "Cats are known for their independence and agility.",
            "A black cat sat on the fence, watching the birds."
        ],
        "dog": [
            "The happy dog wagged its tail enthusiastically.",
            "Dogs are loyal companions and love to play fetch.",
            "A golden retriever barked at the mailman.",
            "Puppies are incredibly cute and playful."
        ],
        "sun": [
            "The sun rose majestically over the mountains.",
            "Sunlight streamed through the window, warming the room.",
            "The sun is a star at the center of our solar system.",
            "We enjoyed a sunny day at the beach."
        ]
    }
    
    # Simulate a potential 'mistake' or less relevant response
    if random.random() < 0.2: # 20% chance of a less relevant or slightly off response
        return f"I am thinking about {topic} and other related things, but not specifically about {topic}."
    
    return random.choice(templates.get(topic.lower(), [f"I don't have enough information about {topic}."])) # AI's generated output

def autonomous_evaluator(topic: str, generated_text: str) -> dict:
    """
    Simulates an autonomous AI system evaluating the generated response.
    This is the 'AI grading its own homework' or another AI's homework.
    """
    feedback = {
        "score": 0,
        "comments": []
    }

    # --- Evaluation Criteria (simplified) ---

    # 1. Relevance Check: Does the response contain the core topic?
    if topic.lower() in generated_text.lower():
        feedback["score"] += 40
        feedback["comments"].append("Response is relevant to the topic.")
    else:
        feedback["comments"].append("Response lacks direct relevance to the topic.")

    # 2. Length/Completeness Check: Is the response a reasonable length?
    # (Simplified: just check if it's not too short)
    if len(generated_text.split()) > 5:
        feedback["score"] += 30
        feedback["comments"].append("Response is sufficiently detailed.")
    else:
        feedback["comments"].append("Response might be too brief.")

    # 3. Quality/Engagement Check: (Very simplified, e.g., check for common descriptive words)
    descriptive_words = ["fluffy", "peacefully", "happy", "loyal", "majestically", "streamed", "cute", "playful"]
    if any(word in generated_text.lower() for word in descriptive_words):
        feedback["score"] += 30
        feedback["comments"].append("Response contains descriptive elements.")
    else:
        feedback["comments"].append("Response could be more descriptive.")
    
    # Cap score at 100
    feedback["score"] = min(feedback["score"], 100)

    # Final grade based on score
    if feedback["score"] >= 80:
        feedback["grade"] = "Excellent"
    elif feedback["score"] >= 60:
        feedback["grade"] = "Good"
    elif feedback["score"] >= 40:
        feedback["grade"] = "Fair"
    else:
        feedback["grade"] = "Needs Improvement"

    return feedback # Autonomous evaluation result

if __name__ == "__main__":
    print("--- Autonomous AI Evaluation System Demo ---")
    print("This script simulates an AI generating a response and then autonomously evaluating it.")
    print("-" * 50)

    topics_to_test = ["cat", "dog", "sun", "moon"] # 'moon' is intentionally not in templates to show evaluation of unknown topics

    for i, topic in enumerate(topics_to_test):
        print(f"\nScenario {i+1}: Topic = '{topic}'")
        
        # Step 1: AI generates its "homework"
        generated_output = generate_ai_response(topic)
        print(f"  AI Generated Response: '{generated_output}'")
        
        # Step 2: Autonomous system evaluates the generated "homework"
        evaluation_result = autonomous_evaluator(topic, generated_output)
        
        print(f"  Autonomous Evaluation:")
        print(f"    Score: {evaluation_result['score']}/100")
        print(f"    Grade: {evaluation_result['grade']}")
        print(f"    Comments: {'; '.join(evaluation_result['comments'])}")
        print("-" * 50)
