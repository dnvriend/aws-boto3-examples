# aws-boto3-examples
Some boto3 examples


## How to build/run
Use the Makefile:

```
$ make
env                            creates a virtual python environment  for this project
info                           shows current python environment
clobber                        remove virtual python environment
fmt                            runs code formatter
type_check                     type checks the code
lint                           run python code analysis on rules
lint_test                      run python code analysis on test


# for example
$ make run
$ make test
$ make fmt
$ make info
```

## Cost Explorer
Determine your cost:

```
$ aws ce get-cost-and-usage \
   --time-period Start=$START_DATE,End=$END_DATE \
   --granularity DAILY \
   --group-by '[{"Type": "DIMENSION", "Key": "SERVICE"}, {"Type": "DIMENSION", "Key": "REGION"}]' \
   --metrics AmortizedCost \
   --query 'ResultsByTime[*].Groups[?(Metrics.AmortizedCost.Amount != `"0"`)].{Service:Keys[0],Region:Keys[1],Amount:Metrics.AmortizedCost.Amount}' \
   --output text
```

## Resource
- [Boto3 docs](https://boto3.readthedocs.io/en/latest/)


Have fun!