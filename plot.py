import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def draw(inname,outname):
    f = open(inname,"r")
    x = []
    for l in f:
        x.append(float(l.rstrip()))
    print("Max: ",sorted(x)[-1]," Min: ",sorted(x)[0],sep="")
    nbins = 100
    fig, ax = plt.subplots()
    n, bins, patches = plt.hist(x, nbins, facecolor='blue', alpha=0.5)
    ax.set_xlabel('Mass of Muon (GeV)')
    ax.set_ylabel("Number of occurence")
    aorz = input("a or z?")
    ax.set_title("Muons' mass distribution (p p > {} > mu+ mu-)".format(aorz))
    plt.savefig('{}'.format(outname))

if __name__ == "__main__":
    plot()
