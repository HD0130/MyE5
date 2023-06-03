import numpy as np
import pandas as pd

def convert_raw_to_xlsx(raw_file, xlsx_file):
    # 读取.RAW文件
    data = np.loadtxt(raw_file, skiprows=32)  # 跳过文件头部的32行

    # 提取数据列
    angles = data[:, 0]
    intensities = data[:, 1]

    # 创建数据框
    df = pd.DataFrame({'Angle': angles, 'Intensity': intensities})

    # 保存为.xlsx文件
    df.to_excel(xlsx_file, index=False)

    print('转换完成！')

# 主函数
def main():
    raw_file = 'input.raw'
    xlsx_file = 'output.xlsx'
    convert_raw_to_xlsx(raw_file, xlsx_file)

if __name__ == '__main__':
    main()
