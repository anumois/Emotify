f = open("politician.txt", "r", -1, "utf-8")
keywords = []
while 1:
    line = f.readline().strip()
    if not line:
        break
    keywords.append(line)
f.close()

for keyword in keywords:
    name = keyword.split('"')[1]
    f_name = name + ".txt"
    
    import codecs
    with codecs.open(f_name, encoding='utf-8') as f:
        data_test = [line.split('\t') for line in f.read().splitlines()]
    
    if len(data_test) == 0:
        continue
    
    for line in data_test:
        line[0] = remove_emoji(line[0])
        
    X_test = list(zip(*data_test))[0]
    e_predict = model1.predict(X_test)
    
    name_anger = name + "_anger.txt"
    name_fear = name + "_fear.txt"
    name_happy = name + "_happy.txt"
    name_sad = name + "_sad.txt"
    anger_result = open(name_anger, 'w', -1, "utf-8")
    fear_result = open(name_fear, 'w', -1, "utf-8")
    happy_result = open(name_happy, 'w', -1, "utf-8")
    sad_result = open(name_sad, 'w', -1, "utf-8")
    
    i = 0
    for line in data_test:
        if e_predict[i] == 0:
            anger_result.write(line[0] + '\t' + line[1] + '\t' + line[2] + '\n')
        elif e_predict[i] == 1:
            fear_result.write(line[0] + '\t' + line[1] + '\t' + line[2] + '\n')
        elif e_predict[i] == 2:
            happy_result.write(line[0] + '\t' + line[1] + '\t' + line[2] + '\n')
        elif e_predict[i] == 3:
            sad_result.write(line[0] + '\t' + line[1] + '\t' + line[2] + '\n')
        i = i + 1
        
    anger_result.close()
    fear_result.close()
    happy_result.close()
    sad_result.close()