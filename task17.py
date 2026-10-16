name = input("Enter student's name: ")
table = int(input("Enter multiplication table number (e.g., 5): "))
num_questions = int(input("Enter number of questions (e.g., 10): "))

if num_questions <= 0 or table <= 0:
  print(
      "Invalid input. Table and number of questions must be positive integers."
  )
else:
  correct_count = 0
  incorrect_count = 0

  print(
      f"\nStarting practice for {name}: Table of {table} ({num_questions}"
      " questions)\n"
  )

  for i in range(1, num_questions + 1):
    correct_answer = table * i
    user_answer = int(input(f"{table} x {i} = "))

    if user_answer == correct_answer:
      print("Correct! 👍")
      correct_count += 1
    else:
      print(f"Incorrect. The correct answer is {correct_answer}.")
      incorrect_count += 1

  percentage = (correct_count / num_questions) * 100

  print("\n--- Performance Report ---")
  print(f"Student Name: {name}")
  print(f"Total Questions: {num_questions}")
  print(f"Correct Answers: {correct_count}")
  print(f"Incorrect Answers: {incorrect_count}")
  print(f"Percentage Score: {percentage:.2f}%")

  if percentage >= 80:
    print("Performance Message: Excellent job! Keep it up! 🌟")
  elif percentage >= 50:
    print("Performance Message: Good effort! Room for improvement. 👍")
  else:
    print("Performance Message: Needs more practice. Don't give up! 💪")