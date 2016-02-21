import re
import sys

## CODING CHALLANGE


def cleanme(s):
    # Gets rid of characters that are not letters or numbers
    sClean = re.sub(r'[\W_]+', '', s)
    return sClean


def sortedlist(lst, outputfile):
    #given a list of strings first cleans them then sorts them as desired.
    cleanlst =  [term[0] + cleanme(term[1:]) if term[0] == '-' and 
                 term[1].isdigit() else cleanme(term) for term in lst]

    letterDict = {}
    numberDict = {}
    #first, we store letters and numbers in separate dictionaries
    for i in range(len(cleanlst)):

        if cleanlst[i][0].isdigit():
            numberDict[cleanlst[i]] = i

        elif cleanlst[i][0] == '-' and cleanlst[i][1].isdigit():
            numberDict[cleanlst[i]] = i
            
        else:
            letterDict[cleanlst[i]] = i
    #We create letter tuples and number tuples from the dictionaries
    #and sort them individually
    lettertuples = zip(sorted(letterDict.keys(), key=lambda v: v.lower()),
    	               sorted(letterDict.values()))
    numbertuples = zip(sorted(numberDict.keys(), key=lambda v: v.lower()),
    	               sorted(numberDict.values()))

    #We merge the two tuples and sort again to get the final tuple
    mergedAndsorted = sorted(lettertuples + numbertuples,key=lambda x: x[1])
   
    #We get rid of the indices in the tuple and create a final list
    cleanedlst = [item[0] for item in mergedAndsorted]

    #Write the list to a file
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