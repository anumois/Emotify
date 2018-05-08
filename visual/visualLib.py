
def copyJson2Context(jsonInput):
    Context = {}
    if jsonInput['result'] == 'success':
        try:
            Context['result'] = True
            Context['Location'] = jsonInput['Location']
            Context['Happy'] = jsonInput['Happy']
            Context['Sad'] = jsonInput['Sad']
            Context['Surprise'] = jsonInput['Surprise']
            Context['Anger'] = jsonInput['Anger']
            Context['HaKeyword'] = jsonInput['HaKeyword']
            Context['SaKeyword'] = jsonInput['SaKeyword']
            Context['SuKeyword'] = jsonInput['SuKeyword']
            Context['AnKeyword'] = jsonInput['AnKeyword']
            return Context
        except KeyError:
            FailContext = {}
            FailContext['result'] = False
            return FailContext
    else:
        FailContext = {}
        FailContext['result'] = False
        return FailContext
