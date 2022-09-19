a = """<Function ID="1" Type="Sequence" Name="New Sequence 1" 
   <Step Number="0" FadeIn="0" Hold="0" FadeOut="0" Values="6">1:2,255:3:3,255</Step>
   <Step Number="1" FadeIn="0" Hold="0" FadeOut="0" Values="6">2:3,255:4:3,255</Step>
   <Step Number="2" FadeIn="0" Hold="0" FadeOut="0" Values="6">0:3,255:2:3,255</Step>
   <Step Number="3" FadeIn="0" Hold="0" FadeOut="0" Values="6">3:3,255:5:3,255</Step>
  </Function>
  <Function ID="3" Type="Sequence" Name="New Sequence 2" BoundScene="2">
   <Step Number="0" FadeIn="0" Hold="0" FadeOut="0" Values="6">0:3,255</Step>
   <Step Number="1" FadeIn="0" Hold="0" FadeOut="0" Values="6">1:3,255</Step>
   <Step Number="2" FadeIn="0" Hold="0" FadeOut="0" Values="6">2:3,255</Step>
  </Function>"""

def findStartSequence(data, name_seq):      # возвращает указатель на место после имени секвенции
    name = 'Type="Sequence" Name="' + name_seq + '"'
    i = 0   # индекс
    i = data.find(name, i, -1)  # находим Sequence....
    if i < 0:                   # если не находим
        return -1
    else:
        return i + len(name)

def findEndSequence(data,i):
    i = data.find('</Function>', i, -1)   # возвращает указатель на конец последнего шага
    if i < 0:
        return -1
    else:
        return i

def findNextStep(data, i, i_end):        # возвращает указатель следующий шаг
    i = data.find('<Step Number=', i, i_end)
    if i < 0:
        return -1
    else:
        return i

def getStepData(data, i, i_end):
    i = data.find('Values="', i, i_end)
    if i < 0:
        return -1
    i = data.find('">', i, i_end)
    if i < 0:
        return -1
    i += 2
    i_end = data.find('</Step>', i, i_end)
    if i < 0:
        return -1
    return data[i:i_end]

def getNextNamberOrZnak(data, i):           # получает строку и указатель выдаёт число на которое указывает указатель
    if data[i:i+3].isdigit():
        c = 3
        num = int(data[i:i+3])
    else:
        if data[i:i + 2].isdigit():
            c = 2
            num = int(data[i:i + 2])
        else:
            if data[i:i + 1].isdigit():
                c = 1
                num = int(data[i:i + 1])
            else:
                return [-1, 0]
    print(num, '----getNextNamberOrZnak')
    return [num, c+i]

def stepDataToList(data):
    new_data = []
    d = [0, -1]
    while True:
        d = getNextNamberOrZnak(data, d[1] + 1)
        print(d[0], d[1], '---stepDataToList')
        print(new_data, '---stepDataToList')
        new_data.append(d[0])
        new_data.append(data[d[1]])

        if d[0] < 0:
            break
    print(new_data)

    # change = 0
    # new_data = []
    # for i in data:
    #     if i==':':
    #         if change:
    #             new_data.append('+')
    #             change = 0
    #             continue
    #         else:
    #             change += 1
    #     new_data.append(i)
    # print(new_data, '--stepDataToList')
    # return data



fixtur_index = []  # 18 шагов по 12 приборов
index_curr = 0
indexEndSequence = 0
step_curr = 0
endOfSteps = 0

i = findStartSequence(a, 'New Sequence 1')
if i:
    index_curr = i
indexEndSequence = findEndSequence(a,i)


while endOfSteps == 0:
    i = findNextStep(a,index_curr,indexEndSequence)
    if i:
        index_curr = i
    else:
        break
    step_data = getStepData(a, index_curr, indexEndSequence)

    listData = stepDataToList(step_data)

    print(step_data)
    print(index_curr)
    print(a[i:indexEndSequence])

    endOfSteps = 1