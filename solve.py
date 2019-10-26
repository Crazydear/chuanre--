#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:李绍丰 河北工业大学-能源与环境工程学院

# ****************************************************************
# 程序功能：用于求解不同条件下肋片的散热效率
# 求解方法：有限容积法
# 网格划分：同位网格
# 模块划分：该程序包括输入模块-__init__,初始化模块-Init_temper
#                   节点方程模块-center、boundary、corner
#                   效率求解模块-eta、eta-1D,迭代求解模块-solve
#                   输出模块-outprint，画图模块-pic
# 第三方库:numpy(必需) chuanre(必需,项目已带)
#          pandas(保存数据) matplotlib(画图)
# ****************************************************************
from chuanre import *

if __name__ == '__main__':
    M = 6     # 定义网格列数量
    N = 4     # 定义网格行数量
    heat = chre(0.06, 0.02)         # 肋片高度和半个厚度
    # 定义肋根温度和初场温度
    heat.Init_temper(M, N, gen=100, other=60)
    heat.solve(100)         # 迭代次数，自定义
    heat.outprint()         # 数据保存和输出
    heat.pic()              # 画图
