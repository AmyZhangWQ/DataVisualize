from random import choice
class RandomWalk :
    def __init__(self,mum_points=5000):
        self.num_points=mum_points #初始化随机漫步的属性
        self.x_values=[0]   #所有的漫步起始于0
        self.y_values=[0]

    def fill_walk(self):  #计算随机漫步所有点
        while len(self.x_values)<self.num_points:  #决定前进方向以及言这个方向前进的距离
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #拒绝原地踏步
            if x_step==0 and y_step==0:
                continue

            #计算下一个点的x数值和y数值
            x=self.x_values[-1]+x_step
            y=self.y_values[-1]+y_step
            self.x_values.append(x)
            self.y_values.append(y)

