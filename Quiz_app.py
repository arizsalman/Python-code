mcqs = [
    {
        'question': "Python ka founder kaun hai?",
        'options': ["A) Elon Musk", "B) Guido van Rossum", "C) Bill Gates", "D) Mark Zuckerberg"],
        'answer': "B"
    },
    {
        'question': "Python kis year me launch hua?",
        'options': ["A) 1991", "B) 2000", "C) 1989", "D) 1995"],
        'answer': "A"
    },
    {
        'question': "Kaunsa data type immutable hai?",
        'options': ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
        'answer': "C"
    },
    {
        'question': "Python me function define karne ka keyword kya hai?",
        'options': ["A) func", "B) def", "C) function", "D) define"],
        'answer': "B"
    },
    {
        'question': "What is a function of Python?",
        'options': ["A) reusable block", "B) list", "C) task", "D) None"],
        'answer': "A"
    }
]
Update = 0
for i, mcq in enumerate(mcqs, 1):
    print(f"\n Q{i} ,{mcq['question']}")
    for option in mcq['options']:
        print(option)
    user_input = input("Enter the correct answer : ").strip().upper()
# Sprip function space katam k  arta he  e.g {"     hello "}=> (hello)
    if user_input == mcq["answer"]:
        print('Correct')
        Update += 1
       
    else:
        print(f" Wrong! Correct answer is {mcq['answer']}")

print(f"\n Your finall score is : {Update}/{len(mcqs)}")
