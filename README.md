Lost Minds | Decentralised BaaS 

Let’s say you want to develop yet another CRUD application in the traditional way. You will struggle to provision servers, develop repetitive APIs, configure databases, handle scaling, etc,. Instead, you may opt to use a BaaS, which will handle all that for you. These services have grown in popularity in the past decade, and a lot of applications nowadays use popular BaaS like firebase and supabase. How Lost Minds differentiate from other is, it is build on top of IPFS which makes it decentralised and affordable. 


---
# Backend as a Service using Decentralised Storage [IPFS]

Follow the below instructions to set up Lost Minds in your machine and build on Web3. The minimum requirements to run Lost minds are as little as 4 CPU core and 2GB of RAM, and an operating system that supports Python.


## Flask Backend for the main application

Setup and Run

### Fork, Clone and Remote

    (venv) $ cd flask
    (venv) $ pip install -r requirements.txt

## Running the Flask Server

Step 1: Change the current directory to Flask-backend
```sh
(venv) $ cd flask
```

Step 2: Set up FLASK_APP
(For Linux or Mac)
```sh
(venv) $ `export FLASK_APP=run.py`
```

(For Windows)
```sh
(venv) $ `set FLASK_APP=run.py`
```


Step 4:Start the backend server
To run the server use the following command:
```sh
(venv) $ flask run --host=0.0.0.0 --port=5000
```

# Analytics | Sepearte Solution

Separate app using streamlit | We have used data from our testing phase to create a dashboard using streamlit.

```
(venv) $ cd streamlit
(venv) $ streamlit run ml.py
```

## Node Backend APIs for the main application

# IPFS
start IPFS works in linux and mac only or use windows subsystem for linux (WSL - IPFS does not work natively on windows)

```
(venv) $ ipfs init
(venv) $ ipfs daemon --enable-pubsub-experiment
```
# Prism
Install prism and generate

```
(venv) $ npm i prism
(venv) $ ./node_modules/.bin/prisma2 generate
```
# API Endpoints List

```

base API -- /api/projects

    Methods         Endpoint                                Rule
    --------        --------                                ----
    get             - "/"                                   allProjects
    post            - "/"                                   -->  projectValidator -->  createProject
    get             - "/:project_id"                        -->  readProject
    put             - "/:project_id"                        -->  projectValidator -->  updateProject
    delete          - "/:project_id"                        -->  deleteProject
    get             - "/:project_id/buckets"                -->  allBuckets
    post            - "/:project_id/buckets"                -->  createBucket
    get             - "/:project_id/buckets/:bucket_id"     -->  readBucket
    put             - "/:project_id/buckets/:bucket_id"     -->  updateBucket
    delete          - "/:project_id/buckets/:bucket_id"     -->  deleteBucket
    post            - "/:project_id/kv/create"              -->  createKvStore
    get             - "/:project_id/kv"                     -->  getKvStores
    get             - "/:project_id/kv/:database_id/all"    -->  databaseInstanceValidator -->  kvGetAll
    get             - "/:project_id/kv/:database_id"        -->  databaseInstanceValidator -->  kvGet
    post            - "/:project_id/kv/:database_id"        -->  databaseInstanceValidator -->  kvPut
    delete          - "/:project_id/kv/:database_id"        -->  databaseInstanceValidator -->  kvDel
    post            - "/:project_id/log/create"             -->  createLogStore
    get             - "/:project_id/log"                    -->  databaseInstanceValidator -->  getLogStores
    get             - "/:project_id/log/:database_id"       -->  databaseInstanceValidator -->  logGet
    get             - "/:project_id/log/:database_id/all"   -->  databaseInstanceValidator -->  logGetAll
    post            - "/:project_id/log/:database_id"       -->  databaseInstanceValidator -->  logAdd
    post            - "/:project_id/analytics/init"         -->  createAnalyticsStore
    get             - "/:project_id/analytics/status"       -->  analyticsStatus
    get             - "/:project_id/analytics"              -->  getAnalytics
    post            - "/:project_id/analytics"              -->  postAnalytics;
```

**Note** : You can find the updated list of API endpoints using the following command
```sh
(venv) $ flask routes
```
