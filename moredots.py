import matplotlib.pyplot as plt
from randam_walk import RandomWalk
while True:
    rw=RandomWalk(50_0000)
    rw.fill_walk()
    plt.style.use('classic')
    fig,ax=plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    ax.scatter(0,0,c='green',edgecolor='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)
#突出起点和终点
    plt.show()
    keep_running=input("Make another walk(y/n):")
    if keep_running=='n':
        break