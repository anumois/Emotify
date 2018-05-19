def regContext(location, sOut):
    context = sOut
    try:
        Happy = sOut['Happy']
        Sad = sOut['Sad']
        Surprise = sOut['Surprise']
        Anger = sOut['Anger']
        sumEmo = Happy + Sad + Surprise + Anger
        if sumEmo == 0:
            return context
        Happy = int((float(Happy) / float(sumEmo)) * 100)
        Sad = int((float(Sad) / float(sumEmo)) * 100)
        Surprise = int((float(Surprise) / float(sumEmo)) * 100)
        Anger = int((float(Anger) / float(sumEmo)) * 100)

        context['Happy'] = Happy
        context['Sad'] = Sad
        context['Surprise'] = Surprise
        context['Anger'] = Anger
        context['Location1'] = location[0]
        context['Location2'] = location[1]
        return context
    except KeyError:
        return False
