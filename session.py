import requests
from bs4 import BeautifulSoup

bs = BeautifulSoup(markup , 'lxml')
pageCounter = 0 
pages = []
buttons = bs.find_all('button', {"class":"css-1dtj1k4 ezfki8j0"})

for button in buttons:
    pages.append(button.text)
    pageCounter = pages  
    print(pageCounter)
#urlResult = requests.get("https://wuzzuf.net/search/jobs/?q=php&a=hpb")
urlResult = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=php&start={pageCounter}")
# save html content

markup = urlResult.content

# take object from beautiful soup


# find h2 from markup
jobHeadings = bs.find_all('h2' , {"class" : "css-m604qf"})
jobAnchors = bs.find_all('a' , {"class" : "css-o171kl"})
jobLocation = bs.find_all('span' , {"class" : "css-5wys0k"})

#experienceYears = bs.find_all('span' , {"class" : '' })

#print(experienceYears)
# print(jobAnchors)
# create list to append all jobs 
jobs = []


for i in range(len(jobHeadings)):
    jobs.append(jobHeadings[i].text)
    jobs.append(jobLocation[i].text)

#print(jobs)
# Write into file 
with open('jobs.txt' , 'w') as jobsFile:
     for job in jobs:
         jobsFile.write(job)
     print('Jobs Added Successfully ')

# Read Jobs
with open('jobs.txt' , 'r') as jobsFile:
     print(jobsFile.read())