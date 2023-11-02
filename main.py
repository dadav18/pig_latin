def translate_to_pig_latin(sentence):
  words = sentence.split()
  pig_latin_words = []

  for word in words:
      if len(word) == 1:
          # For one-letter words, just add 'ay'
          pig_latin_words.append(word + "ay")
      else:
          # For words with more than one letter, change the order and add 'ay'
          pig_latin_words.append(word[1:] + word[0] + "ay")
  # Join the translated words back into a sentence
  pig_latin_sentence = " ".join(pig_latin_words)
  return pig_latin_sentence

# Get user input and call the function
sentence = input("Enter a sentence: ")
result = translate_to_pig_latin(sentence)
print("Pig Latin translation:", result)