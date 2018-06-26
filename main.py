import parser
import calcmass
import plot


if __name__ == "__main__":
    fourv, mass, graph = parser.io()
    calcmass.calc(fourv, mass)
    plot.draw(mass,graph)

