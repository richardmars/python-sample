class Point(object):
    """定义一个数据点"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x: ' + str(self.x) + ' y: ' + str(self.y)

