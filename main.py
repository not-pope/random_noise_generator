from random import seed, randint

seed(420)


def echo (*some):
    for s in some:
        print(s,end="")

def ppp (some):
    for s in some:
        print(s,end="\n")
        

f = open("thump.ppm","wt")

width = 500
height = 500


image = [[(x,y) for y in range(width)] for x in range(height)]
# ppp(image)

f.write("P2 "+str(width)+" "+str(height)+" 255\n")

# for i in range(0,width*height,10):
#     color=str(randint(0,255))
#     for j in range(10):
#         image[i+j]=color
#         image[i+width+j]=color
#     # f.write(str(randint(0,255))+"\n")

block_size=10

for i in range(height//block_size):
    for j in range(width//block_size):  
        color = str(randint(0,255))
        for row in image[i*block_size:i*block_size+block_size]:
            for el in row[j*block_size:j*block_size+block_size]:
                image[el[0]][el[1]]=color

for row in image:
    for el in row:
        f.write(str(el)+" ")




# ppp(image)

f.close()
