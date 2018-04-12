# Will go through Peter Norvig's tutorial on writing a Lisp interpreter in Python.
# lisp interpreter in python


# syntax = arrangement of characters
# semantics = the MEANING of those characters, arranged in that way.



# first step of interpreting = parsing
# first step of parsing = lexical interpretation = tokenizing


def tokenize(chars: str) -> list:
    """
    Convert str of characters into a list of tokens
    """
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()
    # inserts a space around any round brackets.


program = "(begin (define r 10) (* pi (* r r)))"
print(tokenize(program))
# returns a bunch of tokens, split into a list.....

# now write a function to parse, which will allow us to construct a syntax tree

def parse(program: str):# -> Exp:
    """
    Returns SCHEME expression from a string. (parses it, basically)
    """
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list):# -> Exp:
    """
    Read expression from tokens sequence
    """
    if len(token) == 0:
        raise SyntaxError('the file has unexpectedly ended...pls fix me.')
    token = tokens.pop(0)

    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
            
        tokens.pop(0) #to get rid of the ')' that's left over at the end...
        return L
    elif token == ')':
        raise SyntaxError("Hey man, I think you missed a '(' ... ")
    else:
        return atom(token)


def atom(token: str):# -> Atom:
    """
    Numbers become numbers, everything else becomes a symbol...
    """
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)

parse(program)
