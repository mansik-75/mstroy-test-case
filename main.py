# Нужно написать класс, который принимает в конструктор массив этих объектов и реализует 4 метода:
#  - getAll() Должен возвращать изначальный массив элементов.
#  - getItem(id) Принимает id элемента и возвращает сам объект элемента;
#  - getChildren(id) Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,
# чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;
#  - getAllParents(id) Принимает id элемента и возвращает массив из цепочки родительских элементов,
# начиная от самого элемента, чей id был передан в аргументе и до корневого элемента,
# т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!

# Требования: максимальное быстродействие, следовательно, минимальное количество обходов массива при операциях,
# в идеале, прямой доступ к элементам без поиска их в массиве.
#

# Исходные данные:
class TreeStore:
    def __init__(self, items):
        self.items = items
        self._id_map = {}
        self._children_map = {}

        for item in self.items:
            item_id = item['id']
            self._id_map[item_id] = item
            self._children_map[item_id] = []

        for item in self.items:
            parent_id = item['parent']
            if parent_id in self._children_map:
                self._children_map[parent_id].append(item)

    def getAll(self):
        """Сложность O(1)"""
        return self.items

    def getItem(self, id):
        """Сложность O(1)"""
        return self._id_map[id]

    def getChildren(self, id):
        """Сложность O(1)"""
        return self._children_map.get(id, [])

    def getAllParents(self, id):
        """Сложность O(k), где k -- глубина поиска и k <= n"""
        answer = []
        item = self.getItem(id)
        answer.append(item)  # здесь по условию задачи написано, что список должен включать САМ элемент,
        # но в тестовом ответе НЕТ элемента, я по условию задачи сделал, поэтому добавил элемент
        parent_id = item['parent']
        while parent_id in self._id_map:
            parent = self.getItem(parent_id)
            answer.append(parent)
            parent_id = parent['parent']

        return answer


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)

# Примеры использования:
#  - ts.getAll() // [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},{"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},{"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#
#  - ts.getItem(7) // {"id":7,"parent":4,"type":None}
#
#  - ts.getChildren(4) // [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#  - ts.getChildren(5) // []
#
#  - ts.getAllParents(7) // [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]

print(ts.getAll())
print(ts.getItem(7))
print(ts.getChildren(4))
print(ts.getChildren(5))
print(ts.getAllParents(7))
