grammar = {
    'singular': ['boy', 'girl'],
    'plural': ['boys', 'girls'],
    'singular_verb': ['eats'],
    'plural_verb': ['eat']
}

def check_agreement(sentence):
    words = sentence.split()
    subject = words[1]
    verb = words[2]

    if subject in grammar['singular'] and verb in grammar['singular_verb']:
        return True
    if subject in grammar['plural'] and verb in grammar['plural_verb']:
        return True
    return False

sentence = "the boy eats"
print("Agreement Correct:", check_agreement(sentence))
