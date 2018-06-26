import math

def calc(inname,outname):
    with open(inname, 'r') as infile, open(outname, 'w') as outfile:
        for l in infile:
            ls = l.split()
            E = float(ls[1])+float(ls[3])
            p = float(ls[0])+float(ls[2])
            m = math.sqrt(E**2-p**2)
            outfile.write(str(m)+'\n')

if __name__ == "__main__":
    calc()
