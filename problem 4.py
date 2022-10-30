import copy
import random

class Hat:
    contents = list()

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            #print("%s = %s" % (k, v))
            i = 1
            for i in range(v):
                self.contents.append(str(k))
        print(self.contents)

    def draw(self, nr):
        #random.seed(95)
        try:
            result = list()
            randomList = random.sample(range(0, len(self.contents) - 2), nr)
            for i in randomList:
                result.append(self.contents[i])
                #del self.contents[i]

            return result
        except:
            print('Too many requests')
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    i = 0
    m = 0
    for i in range(num_experiments):
        batch = hat.draw(num_balls_drawn)
        #print(batch)
        ok = True
        for k, v in expected_balls.items():
            if batch.count(k) != v:
                ok = False

        if ok:
            m += 1
            print(batch)

    prob = m / num_experiments
    print('\n\nPROB=', prob*100, '%')
    return prob


hat = Hat(blue=4, red=2, green=6)
experiment(hat=hat, expected_balls={'red':1, 'blue':2}, num_balls_drawn=4, num_experiments=3000)
