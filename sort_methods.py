# Быстрая сортировка Хоара
def hoar_sort(A):
    if len(A) <= 1:
        return A
    b = A[0] #барьерный элемент
    L, M, R = [], [], []
    for i in A:
        if i < b:
            L.append(i)
        elif i == b:
            M.append(i)
        else:
            R.append(i)
    return hoar_sort(L) + M + hoar_sort(R)

#A = ['2', '3', '9', '2', '9']
#print( hoar_sort(A) )
