# mcqs = [
#     {
#         'question': "Python ka founder kaun hai?",
#         'options': ["A) Elon Musk", "B) Guido van Rossum", "C) Bill Gates", "D) Mark Zuckerberg"],
#         'answer': "B"
#     },
#     {
#         'question': "Python kis year me launch hua?",
#         'options': ["A) 1991", "B) 2000", "C) 1989", "D) 1995"],
#         'answer': "A"
#     },
#     {
#         'question': "Kaunsa data type immutable hai?",
#         'options': ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
#         'answer': "C"
#     },
#     {
#         'question': "Python me function define karne ka keyword kya hai?",
#         'options': ["A) func", "B) def", "C) function", "D) define"],
#         'answer': "B"
#     },
#     {
#         'question': "What is a function of Python?",
#         'options': ["A) reusable block", "B) list", "C) task", "D) None"],
#         'answer': "A"
#     }
# ]
# Update = 0
# for i, mcq in enumerate(mcqs, 1):
#     print(f"\n Q{i} ,{mcq['question']}")
#     for option in mcq['options']:
#         print(option)
#     user_input = input("Enter the correct answer : ").strip().upper()
# # Sprip function space katam k  arta he  e.g {"     hello "}=> (hello)
#     if user_input == mcq["answer"]:
#         print('Correct')
#         Update += 1

#     else:
#         print(f" Wrong! Correct answer is {mcq['answer']}")

# print(f"\n Your finall score is : {Update}/{len(mcqs)}")


# mcc = [
#     {
#         'question': "1) What is a dictionary in Python?",
#         'options': [
#             "A) An ordered collection of elements",
#             "B) An unordered collection of key-value pairs",
#             "C) A list of items in sequence",
#             "D) A tuple with fixed values"
#         ],
#         'answer': "B"
#     },
#     {
#         'question': "2) How do you create an empty dictionary?",
#         'options': [
#             "A) dict = {}",
#             "B) dict = []",
#             "C) dict = ()",
#             "D) dict = ''"
#         ],
#         'answer': "A"
#     },
#     {
#         'question': "3) What will `my_dict['name']` do?",
#         'options': [
#             "A) Add a new key",
#             "B) Delete a key",
#             "C) Get the value for key 'name'",
#             "D) Change the dictionary type"
#         ],
#         'answer': "C"
#     },
#     {
#         'question': "4) Which method is used to get all keys from a dictionary?",
#         'options': [
#             "A) values()",
#             "B) keys()",
#             "C) items()",
#             "D) get()"
#         ],
#         'answer': "B"
#     },
#     {
#         'question': "5) What is the output of `len({'a':1,'b':2,'c':3})`?",
#         'options': [
#             "A) 3",
#             "B) 6",
#             "C) 2",
#             "D) Error"
#         ],
#         'answer': "A"
#     },
#     {
#         'question': "6) Which method removes a key from a dictionary?",
#         'options': [
#             "A) delete()",
#             "B) pop()",
#             "C) remove()",
#             "D) discard()"
#         ],
#         'answer': "B"
#     },
#     {
#         'question': "7) What will happen if you access a non-existent key using `my_dict['key']`?",
#         'options': [
#             "A) Returns None",
#             "B) Returns False",
#             "C) Raises KeyError",
#             "D) Creates the key automatically"
#         ],
#         'answer': "C"
#     },
#     {
#         'question': "8) What does `my_dict.get('key', 'default')` do?",
#         'options': [
#             "A) Removes the key",
#             "B) Returns value if key exists, else 'default'",
#             "C) Always returns 'default'",
#             "D) Updates the key"
#         ],
#         'answer': "B"
#     },
#     {
#         'question': "9) Which of these can be used as dictionary keys?",
#         'options': [
#             "A) Lists",
#             "B) Dictionaries",
#             "C) Tuples",
#             "D) Sets"
#         ],
#         'answer': "C"
#     },
#     {
#         'question': "10) What does `my_dict.clear()` do?",
#         'options': [
#             "A) Deletes the dictionary",
#             "B) Removes all items from dictionary",
#             "C) Creates a copy of dictionary",
#             "D) Sorts the dictionary"
#         ],
#         'answer': "B"
#     }
# ]


# socre = 0
# for i, mcq1 in enumerate(mcc, 1):
#     print(f"\n Q{i} {mcq1['question']} ")

#     for option in mcq1['options']:
#         print(option)

#     user_input = input("Enter the correct answer : ").strip().upper()

#     if user_input == mcq1['answer']:
#         print("Correct")
#         socre += 1
#     else:
#         print(f"Wrong ❌ The correct answer was: {mcq1['answer']}")


# print(f"\n Your finall score is : {socre}/{len(mcc)} ")

info = {
    "Ariz": 23,
    "Hamza": 29,
    "Ali": 19,
    "Umer": 27,

}
infoC = {
    "Ariz": 'Yellow',
    "Hamza": 'White',
    "Ali": 'Snow',
    "Umer": 'blue',

}
print(f' Ali Age Find And Ali as key to info ..: {info["Ali"]}')
print(
    f' info  Find And Total Dictionary Name in List : {list(info.keys())}')
print(f'infoColour get() student color :{infoC.get("Ali")}')
info.update({'Aashir': 29, 'gress': 32})
print(f'Add a New Student :{info}')
{info.pop("gress")}
print(f'Remove a gress  Student  in Method pop:{info}')
infoC["Ali"] = 'YellowWhite'
print(f'Update the Value of Ali:{infoC}')
