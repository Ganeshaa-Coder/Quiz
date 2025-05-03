
def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
    print(f"\nYour final score: {score} out of {len(questions)}")

questions = [
    {
        "question": "In which village sant tukaram was born?",
        "options": ["A. Solapur", "B. Dharashiv", "C. Mumbai", "D. Dehu"],
        "answer": "D"
    },
    {
        "question": "What is capital of india?",
        "options": ["A. Mumbai", "B. Delhi", "C. Nagpur", "D. Pune"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"],
        "answer": "C"
    }
]

run_quiz(questions)
