import re

def find_events(t):
    events = re.findall("(<event>)(.*?)(</event>)",t,re.DOTALL)
    return events

def pull_numbers(events):
    for event in events:
        l = str(event).split()
        print(l[55],l[56],[68],[69])


def io():
    inname = input("LHE file(after converting to txt): ")
    outnama = input("Output file(four-vector): ")
    outnamb = input("Output file(m_{mu+,mu-}): ")
    outnamc = input("Output graph: ")
    with open(inname, 'r') as infile, open(outnama, 'w') as outfile:
        events = find_events(infile.read())
        for event in events:
            l = str(event).split()
            # 5 particles; 13 elements/particle
            outfile.write('{} {} {} {}\n'.format(l[len(l)-32],l[len(l)-31],l[len(l)-19],l[len(l)-18]))
    return outnama, outnamb, outnamc

if __name__ == "__main__":
    io()
