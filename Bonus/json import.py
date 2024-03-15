import json

# Function to load data from JSON file
def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Function to interactively ask questions and get answers
def ask_questions(data):
    print("Welcome to the Q&A system!")
    print("Type 'exit' to quit.")
    while True:
        question = input("Ask a question: ").strip()
        if question.lower() == 'exit':
            print("Exiting...")
            break
        answer = get_answer(data, question)
        if answer:
            print("Answer:", answer)
        else:
            print("Sorry, the answer to that question is not available.")

# Function to get answer for a question from the loaded data
def get_answer(data, question):
    for qa_pair in data:
        if qa_pair['question'].lower() == question.lower():
            return qa_pair['answer']
    return None

# Main function
def main():
    filename = '../files/questions.json'
    data = load_data(filename)
    ask_questions(data)

if __name__ == "__main__":
    main()
