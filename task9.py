message = input("Enter a message: ")

total_chars = len(message)

start = 0
while start < len(message) and message[start] == " ":
    start = start + 1

end = len(message) - 1
while end >= 0 and message[end] == " ":
    end = end - 1

if start > end:
    trimmed_length = 0
else:
    trimmed_length = end - start + 1

vowels = 0
digits = 0
spaces = 0
for ch in message:
    if ch in "aeiouAEIOU":
        vowels = vowels + 1
    elif ch in "0123456789":
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1

search = input("Enter the word/phrase to search for: ")
text = message.lower()
word = search.lower()

found = False
if len(word) > 0:
    for i in range(len(text) - len(word) + 1):
        match = True
        for j in range(len(word)):
            if text[i + j] != word[j]:
                match = False
                break
        if match:
            found = True
            break

print("Original message:", message)
print("Total characters:", total_chars)
print("Length (excluding leading/trailing spaces):", trimmed_length)
print("Vowels:", vowels)
print("Digits:", digits)
print("Spaces:", spaces)
if found:
    print("Word found.")
else:
    print("Word not found.")
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())