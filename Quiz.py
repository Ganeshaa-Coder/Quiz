import time
import threading
import sys # Using sys to try and flush input, might not work reliably across platforms

# Flag to signal timeout
timeout_flag = [False] # Using a list as a mutable object for the thread to modify

def time_up():
    """Function called by the timer when time expires."""
    timeout_flag[0] = True
    print("\n⏳ Time's up! Press Enter to continue.")
    # Attempt to interrupt input (might not work reliably)
    # This is platform-dependent and generally difficult with standard input()
    # On Unix-like systems, one might use signals, but that's complex.
    # On Windows, libraries like msvcrt could be used.
    # For simplicity here, we rely on the user pressing Enter.

def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        timeout_flag[0] = False # Reset flag for the new question
        timer = threading.Timer(15.0, time_up) # 15-second timer

        start_time = time.time()
        timer.start() # Start the timer

        try:
            # Prompt for input
            answer = input("Your answer (A/B/C/D): ").strip().upper()

            # If we get here, the user entered something before the timer ideally finished
            # or they pressed Enter after the timeout message.
            timer.cancel() # Cancel the timer as the user responded or acknowledged timeout

            end_time = time.time()
            time_taken = end_time - start_time

            if timeout_flag[0]:
                # Time ran out before valid input was processed, or user pressed Enter after timeout
                print("❌ Marked as incorrect due to timeout.")
                # No score added for timeout
            elif time_taken > 15:
                 print(f"⏱️ Time taken: {time_taken:.2f} seconds (Over limit!)")
                 print(f"❌ Wrong! Correct answer: {q['answer']}")
                 # Optionally penalize if answering *after* timer function printed but before pressing enter took too long
            else:
                # User answered within time
                print(f"⏱️ Time taken: {time_taken:.2f} seconds")
                if answer == q["answer"]:
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ Wrong! Correct answer: {q['answer']}")

        except EOFError:
             # Handles cases where input stream might be closed unexpectedly
             timer.cancel()
             print("\nInput error. Moving to next question.")


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
