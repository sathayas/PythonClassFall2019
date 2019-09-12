remTokens = 40  # initial tokes
while True:
    print('Tokens left: ' + str(remTokens))
    useTokens = int(input('How many tokens do you want to use?'))
    remTokens = remTokens - useTokens
    if remTokens<0:
        break

print('Not enough tokens left!')
