import json
import requests
import time
import random
from faker import Faker

faker = Faker()
#read json file
path = "/home/furkanbk/SDM/P1/SDM-P1-GRAPH/data" # change the absolute path of data to your own path
raw_paper_data = None
start_time = time.time()
with open(path + '/matched_papers_on_topics.json', 'r') as json_file:
    raw_paper_data = json.load(json_file)


#extract paperId from raw_paper_data
paper_ids = [paper['paperId'] for paper in raw_paper_data]

#create 10 mock citations for each paper in the paper_ids list to another paper in the paper_ids list
reference_details = []
paper_references= []
paper_limits = []
#fill paper_references with key value pairs. keys are paper_ids and values are 0
for paper in paper_ids:
    rand = random.randint(5, 12)
    paper_limits.append({paper: rand})

for paper in paper_ids:
    paper_references.append({paper: 0})
    
for paper in paper_ids:
    for i in range(1, 9):
        paper_new = paper + "-" + str(i)

        #create random number between 20 and 50
        rand= random.randint(1, 3)
        for i in range(rand):
            referenceId = random.choice(paper_ids)
            if paper_new != referenceId:
                if paper_references[paper_ids.index(paper)][paper] >= paper_limits[paper_ids.index(paper)][paper]:
                    break
                #create fake year between 2017 and 2021
                year = faker.date_time_between(start_date='-5y', end_date='now').year
            
                reference_details.append({'paperId': paper_new, 'referenceId': referenceId, 'year': year})
                paper_references[paper_ids.index(paper)][paper] += 1
               

            #paper cannot be a reference to itself


import csv
import pandas as pd
df = pd.DataFrame(reference_details)
print(df.head(15))

path = "/home/furkanbk/SDM/P1/SDM-P1-GRAPH/data" # change the absolute path of data to your own path
df.to_csv(path + '/citations.csv', index=False)

print("Completed in: ", time.time()-start_time, " seconds")

