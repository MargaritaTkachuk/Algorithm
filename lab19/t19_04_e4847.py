class Heap:
    def __init__(self):
        self._items = [None]
        self._size = 0
        self.pos = {}

    def insert(self, id, priority):
        self._items.append([id, priority])
        self._size += 1
        self.pos[id] = self._size
        self.sift_up(self._size)

    def replace(self, id, priority):
        if id not in self.pos:
            return
        i = self.pos[id]
        old = self._items[i][1]
        self._items[i][1] = priority
        if priority > old:
            self.sift_up(i)
        else:
            self.sift_down(i)

    def extract(self):
        self.swap(1, self._size)
        item = self._items.pop()
        self.pos.pop(item[0])
        self._size -= 1
        if self._size > 0:
            self.sift_down(1)
        return item

    def swap(self, i, j):
        self.pos[self._items[i][0]] = j
        self.pos[self._items[j][0]] = i
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def _max_child(self, left, right):
        if right > self._size:
            return left
        if self._items[left][1] > self._items[right][1]:
            return left
        return right

    def sift_down(self, i):
        while 2 * i <= self._size:
            left = 2 * i
            right = 2 * i + 1
            max_child = self._max_child(left, right)
            if self._items[i][1] < self._items[max_child][1]:
                self.swap(i, max_child)
                i = max_child
            else:
                break

    def sift_up(self, i):
        while i > 1:
            parent = i // 2
            if self._items[i][1] > self._items[parent][1]:
                self.swap(i, parent)
                i = parent
            else:
                break


if __name__ == '__main__':
    heap = Heap()
    with open("input.txt") as f:
        for line in f:
            parts = line.split()
            cmd = parts[0]
            if cmd == "ADD":
                heap.insert(parts[1], int(parts[2]))
            elif cmd == "POP":
                id, pr = heap.extract()
                print(id, pr)
            elif cmd == "CHANGE":
                heap.replace(parts[1], int(parts[2]))
