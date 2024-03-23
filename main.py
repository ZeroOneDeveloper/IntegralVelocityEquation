import openpyxl
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Any
from sklearn.linear_model import LinearRegression

# filename = input('Please enter the file name to test.\n(ex. sample.xlsx) : ')

# workbook = openpyxl.load_workbook(f'./datasets/{filename}')
workbook = openpyxl.load_workbook(f'./datasets/sample.xlsx')
sheet = workbook.active

data: List[Any] = []

for row in sheet.iter_rows():
    for cell in row:
        if len(data) == 0 or len(data[-1]) == 2:
            data.append([cell.value])
        else:
            data[-1].append(cell.value)


def reaction(n: int, inputData: List[List[Any]]) -> Tuple[np.array, np.array, np.ndarray, float]:
    t = np.array(list(map(lambda x: x[0], inputData)))
    if n == 0:
        A = np.array(list(map(lambda x: x[1], inputData)))
    elif n == 1:
        A = np.log(np.array(list(map(lambda x: x[1], inputData))))
    elif n >= 2:
        A = np.array(list(map(lambda x: 1 / x[1] ** (n-1), inputData)))

    model = LinearRegression()
    model.fit(X=t.reshape(-1, 1), y=A)

    data = t.reshape(-1, 1), A
    pred = model.predict(data)

    r2 = model.score(t.reshape(-1, 1), A)

    return t, A, pred, r2


def test():
    for n in range(0, 11):
        t, A, pred = reaction(n, data)
        plt.scatter(t, A)
        plt.plot(t, pred, color='red')
        plt.savefig(f'./results/{n}.png')
        plt.close()


test()
