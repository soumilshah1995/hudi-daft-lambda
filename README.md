![Untitled Diagram drawio](https://github.com/soumilshah1995/hudi-daft-lambda/assets/39345855/7f86b35a-c5e9-4488-92eb-3ec50ec7d1d9)


### Steps 


### Step 1: EDIT env File 
```

DEV_AWS_ACCESS_KEY_ID="XX"
DEV_AWS_SECRET_ACCESS_KEY="XX"
DEV_AWS_REGION="X"
DEV_S3_PATH="XXX"
```
### Step 2:Deploy Stack
```
serverless config credentials --provider aws --key <XX>  --secret <XX> -o
serverless plugin install -n serverless-python-requirements

serverless deploy

```
### Step 3: Create Functional URL 

![image](https://github.com/soumilshah1995/hudi-daft-lambda/assets/39345855/69bf363e-3d54-45cf-ab46-2eeceb9a3454)


#### Make HTTP request now 
