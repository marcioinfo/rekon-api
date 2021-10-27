# Staircase Demo API


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#Deploy">Deploy</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
This API implement the recognition of images using AWS Rekognition on the back-end, dynamodb as persist layer and s3 bucket to store images. The API stores an image in S3, does image recognition on it and returns results to the user in two ways, with a callback and a GET endpoint


![diagram](diagram.png?raw=true "Diagram")

### Built With
* [Serverless Framework](https://www.serverless.com/)
* [Python3](https://www.python.org/downloads/)
* [AWS](https://aws.amazon.com/)
* [Swagger](https://swagger.io/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
To deploy the API you need AWS account and appropriate permission, python3, nodejs, npm and Serverless framework


### Prerequisites

* npm
  ```shell script
  npm install -g serverless
  npm install serverless-aws-documentation --save-dev
  npm install serverless-api-gateway-xray --save-dev
  ```
  
* pip
  ```shell script
  # Local Tests
  virtualenv rekon --python=python3.6
  source rekon/bin/activate
  pip install -r requirements.txt
  ```

### Deploy
In order to deploy the demo api, you need to run the following command:
 
```shell script
$ serverless package
$ serverless deploy
```

After running deploy, you should see output similar to:

```shell script
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
........
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service aws-python.zip file to S3 (711.23 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.................................
Serverless: Stack update finished...
Service Information
service: aws-python
stage: dev
region: us-east-1
stack: aws-python-dev
resources: 6
functions:
  api: aws-python-dev-hello
layers:
  None
```

<!-- USAGE EXAMPLES -->
## Usage

In order to test callback_url on the post Request you can user [webhook-site](https://webhook.site/)

* curl
 ```shell script
# Post Request
curl --location --request POST 'https://mbr4a662j6.execute-api.us-east-1.amazonaws.com/dev/blobs' \
--header 'Content-Type: application/json' \
--data-raw '{"callback_url": "https://webhook.site/5f735c59-2fb3-472e-bba3-ac1664f2bb2d"}'
  ```

 ```shell script
# Put Request
curl --location --request PUT 'https://blob-presigned.s3.amazonaws.com/...' \
--header 'Content-Type: text/plain' \
--data-binary '/TestCases/test2.png'
  ```

 ```shell script
# Get Request
curl --location --request GET 'https://mbr4a662j6.execute-api.us-east-1.amazonaws.com/dev/blobs/189b51c2-7b97-471d-a5c7-9ebceeb9db64'
  ```

As a quick start import Postman requests, [collections](docs/postman/RekonAPI.postman_collection.json) and [environments](docs/postman/RekonAPI%20Dev.postman_environment.json) to Testfully. 
To do so, import the colletion and update the base_url in the environment variables of postman.

_For more examples, please refer to the swagger [Documentation](docs/swagger.yml)_

<p align="right">(<a href="#top">back to top</a>)</p> 


<!-- CONTACT -->
## Contact

Elison Márcio Correa - [Linkedin](https://www.linkedin.com/in/elison-correa/) - marcioinfo.correa@gmail.com

Project Link: [Demo AWS Rekognition](https://github.com/your_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>

