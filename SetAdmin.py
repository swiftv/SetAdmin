#SetAdmin
#---------------------------------------------------------------------
#A utility to present pupil score data by set for setting discusssions
#---------------------------------------------------------------------
#AAV 17/11/23
#Version 1.0
#---------------------------------------------------------------------

#imports
#---------------------------------------------------------------------
import csv

#Subroutines
#---------------------------------------------------------------------

#returns a datalist
def openfile():
    data = []
    with open("test2.csv") as csvfile:
        content = csv.reader(csvfile, delimiter=',')
        for row in content:
            data.append(row)
    return data
    
#identifies the class sets in the data, returns a list of them
def sets(data):
    setList = []
    for row in data:
        if row[1] not in setList:
            setList.append(row[1])

    return setList

#returns a blank scores list, one list for each score out of 100
def score_list():
    score_list = []
    for i in range(0,100):
        currentScore = 100-i
        score_list.append([currentScore])
    return score_list

def writefile(headers, data):
    with open('processed.csv','w',newline='') as csvfile:
        datawriter = csv.writer(csvfile)
        datawriter.writerow(headers)
        datawriter.writerows(data)

def main():
    #dataimport
    data = openfile()

    #analyse the data for classes, assuming they are in column 2
    sets_in_data = sets(data)

    #starter list of 100 scores
    scores_list = score_list()
    
    #for each set
    for classset in sets_in_data:
        #print(classset)
        #loop through the scores.
        for score in scores_list:
            #find the pupils in the data in the set with that school. 
            pupils = ""
            for pupil in data:
                 #if the pupil score and their set matches the list score and the current set, add it to the list at the position, else append a gap
                if int(pupil[2]) == score[0] and pupil[1] == classset:
                    print(pupil)
                    pupils = pupils + pupil[0]
            score.append(pupils)
            
    #set up the header row
    headers = ["score"]
    for set_name in sets_in_data:
        headers.append(set_name)
        
    writefile(headers, scores_list)

if __name__ == "__main__":
    main()
