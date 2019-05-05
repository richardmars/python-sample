class Point(object):
    """定义一个数据点"""
    def __init__(self, key, x, y, value = None):
        self.key = key
        self.x = x
        self.y = y
        self.val = value

    def __str__(self):
        return 'x: ' + str(self.x) + ' y: ' + str(self.y) + ' val: ' + str(self.val)
