class Sorting:

    def bubble_sort(self, list_to_sort=[]):
        if len(list_to_sort) <= 1:
            return list_to_sort

        for n in range(0, len(list_to_sort)):
            for m in range(n+1, len(list_to_sort)):
                if list_to_sort[n] > list_to_sort[m]:
                    tmp = list_to_sort[m]
                    list_to_sort[m] = list_to_sort[n]
                    list_to_sort[n] = tmp

        return list_to_sort
