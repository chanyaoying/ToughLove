import unicodedata
import re
import html
from nltk.tokenize import word_tokenize
import contractions

def preprocess_sentence(sentence):
  # convert to Ascii
  sentence = ''.join(c for c in unicodedata.normalize('NFD', sentence) if unicodedata.category(c) != 'Mn')

  sentence = sentence.lower().strip()

  wordlist = word_tokenize(sentence)
  expanded_words = []   
  for word in wordlist:
    # using contractions.fix to expand the shortened words
    expanded_words.append(contractions.fix(word))
  
  #remove http/https/www and special entities like <br> and \n
  sentence = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$#-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', sentence, flags=re.MULTILINE)
  sentence = re.sub('www.(?:[a-zA-Z]|[0-9]|[$#-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', sentence, flags=re.MULTILINE)
  sentence = html.unescape(sentence)
  sentence = re.sub('\n', '', sentence)

  sentence = ' '.join(expanded_words)

  #separate specific punctuation as a token
  sentence = re.sub(r"([?.!])", r" \1 ", sentence)

  # keep only a-z, A-Z, ".", "?", "!"
  sentence = re.sub(r"[^a-zA-Z?.!]+", " ", sentence)

  return sentence