cd rearcproj
package
pip3 install -r requirements.txt -t .

zip -r9 ../rearcrepo/lambda.zip * -x "bin/*" requirements.txt

cd rearcrepo
zip -g lambda.zip lambda_function.py

aws s3api put-object --bucket kkudylambdazips --key PullACTListings --region us-west-2 --body ./lambda.zip

run cloudformation
aws cloudformation create-stack --stack-name lamdapull2 --template-body file://datasync.yml --capabilities CAPABILITY_NAMED_IAM

aws lambda invoke  --function-name PullListings --invocation-type Event response.json
