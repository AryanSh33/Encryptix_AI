import re
# Predefined keywords 
keywords = {
    'greet': [r'\bhello\b', r'\bhi\b', r'\bhey\b', r'\bgreetings\b'],
    'timings': [r'\btimings\b', r'\bhours\b', r'\bopen\b', r'\bclose\b'],
    'courses': [r'\bcourses\b', r'\bsubjects\b', r'\bprograms\b', r'\bdegrees\b',
                r'\bcse\b', r'\baiml\b', r'\bds\b', r'\bit\b',
                r'\bbtech\b', r'\bmtech\b', r'\bmba\b',r'\bcourse\b'],
    'fees': [r'\bfees\b'],            
    'aiml': [r'\baiml\b', r'\bartificial intelligence\b', r'\bmachine learning\b'],
    'ds': [r'\bds\b', r'\bdata science\b'],
    'cse': [r'\bcse\b', r'\bcomputer science\b', r'\bengineering\b'],
    'syllabus_aiml': [r'\bsyllabus\b.*\baiml\b', r'\baiml syllabus\b'],
    'syllabus_ds': [r'\bsyllabus\b.*\bds\b', r'\bds syllabus\b'],
    'syllabus_cse': [r'\bsyllabus\b.*\bcse\b', r'\bcse syllabus\b'],
    'goodbye': [r'\bbye\b', r'\bfarewell\b', r'\bsee you\b', r'\bgoodbye\b']
    
}
# Predefined responses
responses = {
    'greet': 'Hello!',
    'fees': 'The fees structure differs on the program and branch',
    'goodbye': 'Goodbye! Have a great day!',
    'fallback': 'I apologize, but I didn\'t quite catch that. Could you please repeat or rephrase?',
    'timings': 'Our college is open from 8am to 6pm, Monday to Saturday',
    'courses': 'Our college offer a variety of courses including B.Tech, M.Tech, MBA, Computer Science and Engineering (CSE), Artificial Intelligence and Machine Learning (AIML), Data Science (DS), and Information Technology (IT). How can I assist you further?',
    'aiml': 'Artificial Intelligence and Machine Learning',
    'ds': 'Data Science',
    'cse': 'Computer Science and Engineering',
    'syllabus_aiml': 'The syllabus for AIML includes machine learning algorithms, neural networks and deep learning',
    'syllabus_ds': 'The syllabus for DS covers data analysis,machine learning models and data visualization',
    'syllabus_cse': 'The syllabus for CSE covers programming languages and data structures',
    'goodbye': 'Goodbye!',
    'invalid': 'Please repeat or rephrase?'
}
# Compile patterns
compiled_patterns = {intent: re.compile('|'.join(patterns)) for intent, patterns in keywords.items()}

def get_intent(user_input):
    for intent, pattern in compiled_patterns.items():
        if pattern.search(user_input):
            return intent
    return 'invalid'

def chatbot_response(user_input):
    intent = get_intent(user_input)
    return responses[intent]

print("Welcome to Our College. How may I assist you today? (Type '0' to exit)")

while True:
    user_input = input().lower()
    if user_input == '0':
        print("Thank you for visiting our college. Bbyeee!")
        break
    response = chatbot_response(user_input)
    print(response)
