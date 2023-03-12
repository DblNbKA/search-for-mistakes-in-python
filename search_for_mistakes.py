import enchant
from enchant.checker import SpellChecker
from enchant.tokenize import EmailFilter, URLFilter

print(enchant.list_languages())
binput = input('choice language:')
ainput = input('Enter the sentences or words, and I will look and show the errors:')

checker_with_filters = SpellChecker('en_US', filters=[EmailFilter, URLFilter])
checker_with_filters.set_text(ainput)

ab = [i.word for i in checker_with_filters]
a1b = str(" ".join(ab))

aa = len(ab)
print('amount mistakes: ' + str(aa))

print('mistakes:' + a1b)

dictionary = enchant.Dict('en_US')
for i in range(aa):
    a2b = str(" ".join(dictionary.suggest(str(ab.pop(0)))))
    print(a2b)
