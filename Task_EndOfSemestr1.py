'''
Дан файл с пунктами меню (id, название, id родителя).
Если id родителя равно 0, то родителя не существует. Показать полное меню с отступами.
Пользователь вводит id пункта. Показать цепочку из пунктов меню до этого пункта.
Уровней вложенности в меню может быть любое количество.

Для примера я сделала файл с таким содержимым:
1 ВершинаОдин 2
2 ВершинаДва 0
3 ВершинаТри 0
4 ВершинаЧетыре 1
5 ВершинаПять 3
6 ВершинаШесть 4

Для вершины 6 будет путь
ВершинаДва
	ВершинаОдин
		ВершинаЧетыре
			ВершинаШесть
'''


class Point:
    ID = int
    Name = str
    ParentID = int

array = []
res = []
tab = 0

#разделяем каждую строку на элементы, создаем объект класса и заносим элементы в соответствующие поля класса
try:
    with open('task.txt') as my_file:
        for line in my_file:
            args = line.split()
            p = Point()
            p.ID = int(args[0])
            p.Name = args[1]
            p.ParentID = int(args[2])
            array.append(p)
except FileNotFoundError:
    print("Упс! А файла-то нет такого")

#ищем объект класса, id которого совпадает с введенным пользователем
def GetPointByID(id):
    for item in array:
        if item.ID == id:
            return item

def GetTree(item, tree):
    if tree == "":
        tree = item.Name
    else:
        tree = item.Name + '\n' + tree
    #проверяем наличие родителя у объекта и строим дерево до объекта
    parent = GetPointByID(item.ParentID)
    if (parent != None):
        return GetTree(parent, tree)
    return tree

id = int(input())
res.append(str(GetTree(GetPointByID(id), "")).split('\n'))

try:
    with open('output.txt','w') as output:
        for a in range(len(res)):
            for j in range(len(res[a])):
                output.write(tab * '\t'+ res[0][j]+'\n')
                tab+=1
except FileNotFoundError:
    print("Упс! А файла-то нет такого")
