from operator import attrgetter


class Vheap:
    def __init__(self, key_func):
        self.__q = []
        self.key_func = key_func

    def push(self, item):
        self.__q.append(item)
        item.pos = len(self.__q) - 1
        self.heapify_up(item.pos)

    def pop(self):
        self.__q[0], self.__q[len(self.__q) - 1] = self.__q[len(self.__q) - 1], self.__q[0]
        self.__q[0].pos = 0
        item = self.__q.pop()
        self.heapify(0)
        return item

    def delete(self, item):
        self.__q[item.pos], self.__q[len(self.__q) - 1] = self.__q[len(self.__q) - 1], self.__q[item.pos]
        self.__q[item.pos].pos = item.pos
        self.__q.pop()
        if item.pos != len(self.__q):
            if self.key_func(self.__q[item.pos]) < self.key_func(self.__q[self.parent(item.pos)]):
                self.heapify_up(item.pos)
            else:
                self.heapify(item.pos)

    def heapify_up(self, index):
        while self.key_func(self.__q[index]) < self.key_func(self.__q[self.parent(index)]):
            self.__q[self.parent(index)], self.__q[index] = self.__q[index], self.__q[self.parent(index)]
            self.__q[self.parent(index)].pos, self.__q[index].pos = self.__q[index].pos, self.__q[self.parent(index)].pos
            index = self.parent(index)

    def heapify(self, vio_index):
        min_child = self.get_min_child(vio_index)
        if min_child is None:
            return
        while self.key_func(self.__q[vio_index]) > self.key_func(min_child):
            child_pos = min_child.pos
            self.__q[child_pos], self.__q[vio_index] = self.__q[vio_index], self.__q[child_pos]
            self.__q[vio_index].pos, self.__q[child_pos].pos = vio_index, child_pos
            vio_index = child_pos
            min_child = self.get_min_child(vio_index)
            if min_child is None:
                break

    def get_min_child(self, vio_index):
        if self.right(vio_index) < len(self.__q):
            return min(self.__q[self.left(vio_index)], self.__q[self.right(vio_index)], key=self.key_func)
        elif self.left(vio_index) < len(self.__q):
            return self.__q[self.left(vio_index)]
        else:
            return None

    def left(self, pos):
        return pos * 2 + 1

    def right(self, pos):
        return pos * 2 + 2

    def parent(self, pos):
        return int((pos - 1) / 2)

    def __contains__(self, item):
        return item in self.__q

    def __len__(self):
        return len(self.__q)

    def delete_pos(self, index):
        self.delete(self.__q[index])

# class Tester:
#     def __init__(self, rank):
#         self.rank = rank
#
#
# a = Vheap(attrgetter('rank'))
# for i in [-7642, -7472, -7435, -7281, -7277, -7213, -7206, -7120, -7008, -6950, -6930, -6876, -6736, -6735, -6699, -6696, -6651, -6638, -6637, -6620, -6582, -6561, -6430, -6425, -6390, -6345, -6331, -6327, -6276, -6273, -6267, -6235, -6230, -6120, -6093, -6073, -6059, -6059, -6017, -5992, -5987, -5961, -5912, -5911, -5901, -5855, -5821, -5814, -5778, -5731, -5706, -5704, -5683, -5668, -5652, -5624, -5611, -5566, -5521, -5503, -5474, -5463, -5456, -5448, -5445, -5427, -5362, -5349, -5305, -5174, -5160, -5125, -5118, -5091, -5069, -5059, -5058, -5050, -4929, -4926, -4924, -4892, -4886, -4884, -4873, -4854, -4827, -4823, -4667, -4660, -4649, -4613, -4607, -4579, -4544, -4490, -4458, -4449, -4429, -4370, -4343, -4330, -4294, -4246, -4213, -4071, -4059, -4010, -4003, -3934, -3905, -3859, -3854, -3820, -3812, -3743, -3667, -3653, -3644, -3618, -3532, -3500, -3337, -3253, -2987, -2951, -2763, -2736, -2604, -2548, -2445, -2436, -2315, -2266, -2202, -1972, -1847, -1734, -1572, -1467, -1127, -952, -606, -526, -403, -378]:
#     a.push(Tester(i))
#
# for i in range(146):
#     print(a.pop().rank)
