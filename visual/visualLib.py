
def copyJson2Context(jsonInput):
    Context = {}
    if jsonInput['result'] == 'success':
        Context['result'] = True
        Context['Location'] = jsonInput['Location']
        Context['Happy'] = jsonInput['Happy']
        Context['Sad'] = jsonInput['Sad']
        Context['Surprise'] = jsonInput['Surprise']
        Context['Anger'] = jsonInput['Anger']
        return Context
    else:
        Context['result'] = False
        return Context
