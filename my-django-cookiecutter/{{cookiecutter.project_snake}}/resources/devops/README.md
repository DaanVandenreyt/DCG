# OSN Platform - Cloudformation templates

## Serverless devops policy
In order for you to deploy an application via `sls deploy`to AWS, you require an IAM user with sufficient permissions.

1. Make sure there is an IAM user for which you have the access id and secret access key
2. If it is the first time, you're going to apply the policy document to the given user, you'll be "creating a Cloudformation stack":

```
$ aws cloudformation create-stack --stack-name osn-platform-devops-policy --template-body file://$(pwd)/devops-policy.yaml --capabilities CAPABILITY_IAM 
```

If something had changed in the template, you'd replace `create-stack` with `update-stack`.

If you want to detach the policy, you can simply delete the stack by calling
```
$ aws cloudformation delete-stack --stack-name osn-platform-devops-policy
```
