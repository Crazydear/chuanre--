from chuanre import *

if __name__ == '__main__':
    M = 6     # 定义网格列数量
    N = 4     # 定义网格行数量
    heat = chre(0.06, 0.02)         # 肋片高度和半个厚度
    # 定义肋根温度和初场温度
    heat.Init_temper(M, N, other=60)
    heat.solve(100)         # 迭代次数，自定义
    heat.outprint()         # 数据保存和输出
    heat.pic()              # 画图
