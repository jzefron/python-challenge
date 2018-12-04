import csv
import os

csvpath = os.path.join('source','Instructions','PyBank','Resources','budget_data.csv')
count = 0
bigLoss = 9999
bigGain = -9999
tot = 0
lString = ""
gString = ""
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)
   
    for row in csvreader:
        count += 1
        monData = int(row[1])
        tot += monData
        if bigLoss > monData:
            bigLoss = monData
            lString = row[0]
        if bigGain < monData:
            bigGain = monData
            gString = row[0]
outputpath =os.path.join("PyBank","output.txt")
with open(outputpath, 'w', newline='\n') as fileW:
    fileW.write("FInancial Analysis \n")
    fileW.write("----------------------------\n")
    fileW.write("Total Monthes: " + str(count)+"\n")
    fileW.write("Total: "+str(tot)+"\n")
    fileW.write("Average Gain: " + str(round(float(tot)/count,2))+"\n")
    fileW.write("Biggest montly gain: " +gString +" ("+str(bigGain)+")\n")
    fileW.write("Biggest montly loss:" + lString+" ("+str(bigLoss)+")\n")
with open(outputpath) as readback:
    for row in readback:
        print(row)
