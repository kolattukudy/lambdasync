**Install instructions**

**cd rearcproj**

Install the libraries to empty folder using requirements file

    pip3 install -r requirements.txt -t .

  
Package the folder for upload

    zip -r9 ../rearcrepo/lambda.zip * -x "bin/*" requirements.txt

  

**cd rearcrepo**

    zip -g lambda.zip lambda_function.py

  
**Upload lambda file to s3**

    aws s3api put-object --bucket kkudylambdazips --key PullACTListings --region us-west-2 --body ./lambda.zip

  

**run cloudformation**

    aws cloudformation create-stack --stack-name lamdapull2 --template-body file://datasync.yml --capabilities CAPABILITY_NAMED_IAM

  
**Invoke lambda's** 

    aws lambda invoke --function-name PullListings --invocation-type Event response.json

Login to AWS Console choose the Cloudwatch service and look for the logs to see the lambdas and invoked.

If there was no error on the CloudWatch logs you should see the files uploaded to S3 bucket.






