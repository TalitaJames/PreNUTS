import networkx as nx
import matplotlib.pyplot as plt
from enum import Enum
import json

global classJson

def readJson(filename):
    with open(filename) as f:
        return json.load(f)


def findIndex(subjectCode):
    for index, subject in enumerate(classJson):
        if int(subject["code"]) == subjectCode:
            return index
    print(f"Subject {subjectCode} not found")


def plotSingleSubject(subjetDict,colour="lightblue"):

    preReq=subjetDict["preReq"]
    subject=subjetDict["code"]
    tooPre=subjetDict["tooPer"]
    
    preReqEdges=[[x,subject] for x in preReq] # all preReqs need to point to subject
    tooPreEdges=[[subject,x] for x in tooPre] # vice versa for tooPres

    # FIXME in future, show codependencies & AND/OR preReqs better
    class Type(Enum):
        subject = 1
        preReq = 2
        tooPre = 3

    G = nx.DiGraph()

    G.add_node(subject, type = Type.subject)
    G.add_nodes_from(preReq, type = Type.preReq)
    G.add_nodes_from(tooPre, type = Type.tooPre)

    G.add_edges_from(preReqEdges)
    G.add_edges_from(tooPreEdges)


    preReqPos={val:(num+1,1) for num,val in enumerate(preReq)}
    tooPrePos={val:(num+1,-1) for num,val in enumerate(tooPre)}
    subMidPos=(max(len(preReq),len(tooPre))+1)/2
    
    pos={
        **preReqPos,
        subject: (subMidPos,0),
        **tooPrePos
    }
    # print(pos)

    plotArgs = {
        "with_labels":True,
        # "font_weight":"bold",
        "node_size": 2000,
        "node_color": colour,
        "linewidths": 0,
        "arrowsize": 15
    }

    nx.draw(G, pos=pos, **plotArgs)
    plt.draw()
    plt.savefig(f"test_graphExports\{subjetDict['code']}_path.png")

    plt.clf() # clear so next graphs don't overlap
    return G


if __name__ == "__main__":
    filename="subjects2023.json"
    classJson = readJson(filename)

    # these 5 classes have the highest num of TooPres (all law who's suprised)
    top5TooPre=[33130,70311,70616,70110,70106] 
    
    for i in top5TooPre:
        plotSingleSubject(classJson[findIndex(int(i))])