import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph,src):
    if graph ==None:
        return None
    # 定点集合
    nodes = [i for i in range(len(graph))] # 获取顶点列表，用邻接矩阵存储图
    # 顶点是否被访问
    visited = []
    visited.append(src)
    # 初始化dis
    dis = {src:0}# 源点到自身的距离为0
    for i in nodes:
        dis[i] = graph[src][i]
    path={src:{src:[]}} # 记录源节点到每个节点的路径
    k=pre=src
    while nodes:
        temp_k = k
        mid_distance=float('inf') # 设置中间距离无穷大
        for v in visited:
            for d in nodes:
                if graph[src][v] != float('inf') and graph[v][d] != float('inf'):# 有边
                    new_distance = graph[src][v]+graph[v][d]
                    if new_distance <= mid_distance:
                        mid_distance=new_distance
                        graph[src][d]=new_distance # 进行距离更新
                        k=d
                        pre=v
        if k!=src and temp_k==k:
            break
        dis[k]=mid_distance # 最短路径
        path[src][k]=[i for i in path[src][pre]]
        path[src][k].append(k)
 
        visited.append(k)
        nodes.remove(k)
    return dis,path


Inf = float('inf')

df = pd.read_excel(r"C:\Users\Siyuehang\Desktop\附件：任务表、道路数据表及结果格式.xlsx",sheet_name="表2 交通线路表")
start = df["起点"]
end = df["终点"]
licheng = df["里程（km）"]
disdis = [[Inf] * 29 for i in range(29)]
for temp_i in range(len(start)):
    if temp_i < 29:
        disdis[temp_i][temp_i] = 0
    disdis[start[temp_i]-1][end[temp_i]-1] = licheng[temp_i]
    
#print(disdis)
Src, N = 0, 29
# Src表示起点的编号，Dst表示终点的编号，N表示结点个数.


dis,path= dijkstra(disdis, 0) # 查找从源点0开始带其他节点的最短路径
print(dis,'\n')
print(path)