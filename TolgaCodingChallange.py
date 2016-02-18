import re
import sys

## CODING CHALLANGE


def cleanme(s):
    sClean = re.sub(r'[\W_]+', '', s)
    return sClean


def sortedlist(lst, outputfile):
    
    cleanlst =  [cleanme(term) for term in lst]

    letterDict = {}
    numberDict = {}

    for i in range(len(cleanlst)):
        if cleanlst[i][0].isdigit():
            numberDict[cleanlst[i]] = i
        else:
            letterDict[cleanlst[i]] = i

    lettertuples = zip(sorted(letterDict.keys(), key=lambda v: v.lower()),
    	               sorted(letterDict.values()))
    numbertuples = zip(sorted(numberDict.keys(), key=lambda v: v.lower()),
    	               sorted(numberDict.values()))

    mergedAndsorted = sorted(lettertuples + numbertuples,key=lambda x: x[1])
   
    cleanedlst = [item[0] for item in mergedAndsorted]

    with open(outputfile, 'w') as out_file:
    	out_file.write(' '.join(cleanedlst))
    out_file.close()

    return cleanedlst


def challangeaccepted(inputfile,outputfile):
	
	f = open(inputfile, 'r')
	line = f.readline()
	f.close()

	if line == []:
		print "The file is empty!"
	else:
		wordList = line.split(' ')
		sortedlist(wordList, outputfile)



def main():
    if len(sys.argv) != 3:
		print "Not enough arguments. Please enter an input file and an output file name to write the results in"
    else:
		inputfile = sys.argv[1]
		outputfile = sys.argv[2]
		challangeaccepted(inputfile,outputfile)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()