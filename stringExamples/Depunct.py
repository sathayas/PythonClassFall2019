def depunct(inText, punctChars=',.?!;:/'):
    outText = inText
    for iChar in punctChars:
        outText = outText.replace(iChar,'')
    return outText

sampleText = '''This is a multi-line text.
This includes multiple sentences on multiple lines.
Some lines may be short.
However, other lines may be longer, containing a larger number of words.
You can split this text, line by line, using the split() method.
'''

print(depunct(sampleText))
