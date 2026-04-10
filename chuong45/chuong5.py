def bai_1():
    import matplotlib.pyplot as plt
    muc_hoc_luc = ['Xuất sắc', 'Giỏi', 'Trung bình', 'Yếu', 'Kém']
    so_hoc_sinh = [6, 10, 12, 4, 1]
    plt.bar(muc_hoc_luc, so_hoc_sinh)
    plt.title('Kết quả học tập của lớp')
    plt.xlabel('Mức học lực')
    plt.ylabel('Số học sinh')
    plt.show()

def bai_2():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(-5, 5, 100)
    y1 = x ** 2
    y2 = x ** 3
    plt.plot(x, y1, color='blue', label='y = x^2')
    plt.plot(x, y2, color='red', label='y = x^3')
    plt.title('Đồ thị y = x^2 và y = x^3')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def bai_3():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(-5, 5, 100)
    y1 = x ** 2
    y2 = x ** 3
    plt.plot(x, y1, color='blue', label='y = x^2')
    plt.plot(x, y2, color='red', label='y = x^3')
    plt.title('Đồ thị y = x^2 và y = x^3')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def bai_4():
    import matplotlib.pyplot as plt
    import pandas as pd
    data = pd.read_csv("C:\\california_cities.csv")
    df = pd.DataFrame(data)
    top10_cities = df.sort_values(by='area_total_km2', ascending=False).head(10)
    top10_cities = top10_cities.sort_values(by='area_total_km2', ascending=True)
    plt.barh(top10_cities['city'], top10_cities['area_total_km2'], color='mediumseagreen')
    plt.title('Top 10 thành phố lớn nhất theo diện tích ở California', fontsize=14)
    plt.xlabel('Diện tích (km²)', fontsize=12)
    plt.ylabel('Thành phố', fontsize=12)
    plt.tight_layout()
    plt.show()
