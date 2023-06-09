# Table of content

- [Description](#description)
- [NPM start](#npm-start)
- [Usage](#usage)
- [Documentation](#doc)
- [Frameworks](#Frameworks)
- [Clinic Sources](#clinic-sources)
- [Continous Integration](#continous-integration)
- [Docker Image](#docker-image)
- [Assumptions](#assumptions)
- [Decisions](#decisions)

### Description

An application that fetches clinic list from multiple sources and filters them based on user's query.

### NPM Start
Starts the server on port 5000 or any set port in the .env file

Runs node server.js

### Usage
- Clone this repository
- Run npm install
- Run npm start
- After Starting the server in Development mode
- Send a post request to http://localhost:5000/api/v1/search
- The endpoint recieves 4 parameters. Ranges from none to all in all possible combinations


Query Example:
{
  "name": "Scratchpay",
  "state": "California",
  "availableFrom": "01:00",
  "availableTo": "23:00"
}


Response Example:
{
  "data": [
    {
      "name": "Scratchpay",
      "state": "California",
      "availability": {
        "from": "00:00",
        "to": "24:00"
      }
    }
  ]
}

### Framework
This project was bootstrapped with these

- [Expressjs](https://expressjs.com/)
- [Jest](https://jestjs.io/)

### Doc
After NPM start

[Swagger Doc](http://localhost:5000/docs/)

### Clinic Sources
[DENTAL_CLINICS_API_URL](https://storage.googleapis.com/scratchpay-code-challenge/dental-clinics.json)

[VET_CLINICS_API_URL](https://storage.googleapis.com/scratchpay-code-challenge/vet-clinics.json)

### Continous Integration
Continous Integration implemented on [Github Actions](https://github.com/Layoolar/scratch_pay/actions)

### Docker Image
[DockerHub](https://hub.docker.com/repository/docker/layoolar/scratch_pay/general)

### Assumptions
- That the client is looking for any available time within the range and should return any overlap.
- That I am working alone on the project, hence no need to checkout the branch.
- We will eventually scale to source for clinics outside US, hence why I created a key value for state codes instead of using a framework.
- The endpoint is available to everyone. Hence, no need for authorization
- We are interested in keeping logs. 


### Decisions
- The "try me out" in the documentation has been left strictly for grading purposes. In a live environment, this should be removed as it poses a great security risk. 
- Allow customers to search with only one time constraint.
- Returns an error if a customer searches above 23:59 or below 00:00
- Using express as the framework because it is lightweigt and fast
- Using Jest for testing because it is easy to use
- Logging has been loosely coupled to enable easy removal
- Used Winston for logging to help us get more insight 
- A different log each file for each day to make maintainance easy
- Not to use Typescript as it increases required time
- Constant commits after each file to make going back to any point easy 

