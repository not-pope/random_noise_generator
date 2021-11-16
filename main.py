from random import seed, randint
import sys
from typing import List, Tuple

def parse_args (args: List[str]) -> Tuple[int, int, int, str]:
    width = 100
    height = 100
    block_size = 1
    outfile = 'out.ppm'
    args = args[1:]
    if len(args)%2!=0 :
        print("Proper flags format is not registered. Read README.md .")
        exit(1)
    else:
        index=0
        while index < len(args):
            value = args[index]
            if (value=='-w' or value=='-width'):
                if (args[index+1].isdecimal()):
                    width = int(args[index+1])
                else:
                    print("You need to provide width with -w")
                    exit(1)
                index+=2
            elif (value=='-h' or value=='-height'):
                if (args[index+1].isdecimal()):
                    height = int(args[index+1])
                else:
                    print("You need to provide height with -h")
                    exit(1)
                index+=2
            elif (value=='-b' or value=='-block_size'):
                if (args[index+1].isdecimal()):
                    block_size = int(args[index+1])
                    if (width%block_size!=0 or height%block_size!=0):
                        print("Width and height should be divisible by block size")
                        exit(1) 
                else:
                    print("You need to provide block size with -b")
                    exit(1)
                index+=2
            elif (value=='-o' or value=='-output'):
                if (args[index+1].isalpha()):
                    outfile = args[index+1]+'.ppm'
                else:
                    print("You need to provide filename with -o")
                    exit(1)
                index+=2
            else:
                print("Proper flags format is not registered. Read README.md .")
                exit(1)
    return (width,height,block_size,outfile)

def generate_image (width: int, height: int, block_size: int) -> List[List[int]] :
    image = [[(x,y) for y in range(width)] for x in range(height)]
    # super unoptimized way of doing this :((
    for i in range(height//block_size):
        for j in range(width//block_size):  
            color = str(randint(0,255))
            for row in image[i*block_size:i*block_size+block_size]:
                for el in row[j*block_size:j*block_size+block_size]:
                    image[el[0]][el[1]]=color
    return image

def save_image (image: List[List[int]], outfile: str):
    with open(outfile,"wt") as f:
        f.write("P2 "+str(len(image[0]))+" "+str(len(image))+" 255\n")
        for row in image:
            for el in row:
                f.write(str(el)+" ")

def main():
    width, height, block_size, outfile = parse_args(sys.argv)
    image = generate_image(width, height, block_size)
    save_image(image, outfile)

if __name__ == "__main__":
    main()