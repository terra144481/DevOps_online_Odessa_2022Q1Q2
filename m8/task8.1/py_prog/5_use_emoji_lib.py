import emoji
text = input ('Please enter someting sentences with consists a words dog, cat , bird, book, sun : ')
word_replace = {'bird': ':bird:',
                   'cat': ':cat_face:',
                   'dog': ':dog_face:',
                   'book': ':open_book:',
                   'sun': ':sun:'}
# Iterate over all key-value pairs in dictionary
for key, value in word_replace.items():
    # Replace key character with value character in string
    text = text.replace(key, value)
print (emoji.emojize(text))