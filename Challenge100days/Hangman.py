import random
import hangman_art

print (hangman_art.logo)
word_list=[
  'Acquiesce', 'Acronym', 'Ambiguity', 'Analogy', 'Anachronism', 'Andragogy', 'Antithesis', 'Antonym', 'Articulate', 'Assonance', 
'Benchmarking', 'Brainstorming', 
'Circumspect', 'Clandestine', 'Cognition', 'Collaborate', 'Colloquial', 'Connotation', 'Contrived', 'Conundrum', 'Correlation', 'Criterion', 'Cumulative', 'Curriculum', 
'Deference', 'Developmental', 'Dialect', 'Diction', 'Didactic', 'Dissertation', 'Divergent', 
'Egregious', 'Eloquence', 'Emergent', 'Empathy', 'Enigma', 'Epitome', 'Epiphany', 'Epitaph', 'Erudite', 'Existential', 'Exponential', 
'Formative', 
'Holistic', 'Homonym', 'Hubris', 'Hyperbole', 
'Incongruous', 'Infamy', 'Initiation', 'Innate', 'Intellectual', 'Interactive', 'Irony', 
'Jargon', 'Juxtaposition', 
'Malapropism', 'Magnanimous', 'Mentor', 'Metaphor', 'Meticulous', 'Mnemonic', 'Monologue', 'Motif', 'Myriad', 
'Nemesis', 'Nominal', 'Norms', 
'Obfuscate', 'Obtuse', 'Onomatopoeia', 'Ostentatious', 'Oxymoron', 
'Paradox', 'Paraphrase', 'Pedantic', 'Pedagogy', 'Perusal', 'Phonemes', 'Phonological', 'Plagiarism', 'Plethora', 'Posthumously', 'Preposition', 'Pretentious', 'Pseudonym', 
'References', 'Reflection', 'Rubric', 
'Sardonic', 'Satire', 'Simile', 'Soliloquy', 'Superfluous', 'Syntax', 
'Thesis', 
'Validity', 'Vernacular', 'Virtual', 'Vocational']

stages = hangman_art.stages

word_list=[x.lower() for x in word_list]
new_word = word_list[random.randint(0, len(word_list))]
#print (len(new_word))

code_word=[]
code_list=[]
for char in new_word:
  code_word.append("_")
  code_list.append(char)
  
print (' '.join(code_word))
#print (code_list)
end_of_game=False

lives=6
print (stages[lives])
while not end_of_game:
  guess = input("Your letter: ").lower()
  #print (f"Your letter: {guess}")
  i=0
  if guess in code_word:
    print (f"You already have guessed {guess}")
  elif guess in code_list:
    for char in new_word:
      if guess==char:
        code_word[i]=guess
        i+=1

      else:
        i+=1


    print (' '.join(code_word))
  else:
    
    lives-=1
    print (f"Wrong! Now you have {lives} lives")
    print (stages[lives])
    print (' '.join(code_word))
    if lives ==0:
      end_of_game=True
      print ("You lost!")
      print (f"Word was {new_word}")
  
  
  if '_' not in code_word:
    end_of_game=True
    print ("You win!")




