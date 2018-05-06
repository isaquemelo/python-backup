import math
form = 0
pontos = []
xs = []
ys = []

def angle_between_points( p0, p1, p2 ):
    for i in p0:
        p0[0] = int(p0[0])
        p0[1] = int(p0[1])
    for f in p1:
        p1[0] = int(p1[0])
        p1[1] = int(p1[1])
    for h in p2:
        p2[0] = int(p2[0])
        p2[1] = int(p2[1])
    a = (p1[0]-p0[0])**2 + (p1[1]-p0[1])**2
    b = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    c = (p2[0]-p0[0])**2 + (p2[1]-p0[1])**2
    angle = math.acos( (a+b-c) / math.sqrt(4*a*b) ) * 180/math.pi
    print('{:.2f}'.format(angle))
    return


while form != 3:
    form += 1
    aeb = str(input()).split()
    x = aeb[0]
    y = aeb[1]
    pontos.append(aeb)
    xs.append(int(aeb[0]))
    ys.append(int(aeb[1]))
print(pontos)

angle_between_points(pontos[0],pontos[1],pontos[2])