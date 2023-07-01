import boto3

client = boto3.client('lambda', region_name='ap-south-1')
def lambda_handler(marker = None):
  response = None
  if(marker is None):
    response = client.list_functions(
      FunctionVersion='ALL',
      MaxItems=500,
    )
  else:
    response = client.list_functions(
      FunctionVersion='ALL',
      MaxItems=500,
      Marker=marker
    )
    
  if marker is None:
    print('Function Name,Runtime,Function Size,Timeout,Memory Size,Last Modified')
  for function in response['Functions']:
    print('{},{},{} MB,{},{},{}'.format(function['FunctionName'], function['Runtime'], function['CodeSize']/(1024 * 1024), function['Timeout'], function['MemorySize'], function['LastModified']))
  if(response.get('NextMarker', None) is not None):
    lambda_handler(response['NextMarker'])

lambda_handler()