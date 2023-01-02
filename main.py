import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list
print(logo)


# Generate a random word
#choosen_word = ["ardvark", "baboon", "camel"]
choosen_word = word_list
random_choosen_word = random.choice(choosen_word)
print(random_choosen_word)
# Generate as many blanks as letter in word
choosen_word_length = len(random_choosen_word)
blanks = [] 
for _ in range(choosen_word_length):
  blanks += "_"

end_of_game = False
lives = 6  

while not end_of_game:
  # Ask the user to guess a letter
  user_input = input("Guess a letter: ").lower()  
  # Check gussed letter is correct
  for position in range(choosen_word_length):
    letter = random_choosen_word[position]
    #print(f"Current Position:{position},Current Letter: {letter}, Guess Letter: {user_input} ")
# Yes, replace the blank with the letter
    if user_input == letter:
      blanks[position] = letter
  if user_input not in random_choosen_word:
    lives -= 1
    print(stages[lives])
    if lives == 0:
      end_of_game = True
      print("You Loose!")
  # Are all blank filled 
  if "_" not in blanks:
    end_of_game = True
    print("You Win!")
  print(blanks)
  





