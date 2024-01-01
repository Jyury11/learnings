import boto3
import json


class UpdateUserUsecase:
  def __init__(self) -> None:
    self.dynamodb = boto3.resource("dynamodb")
    self.table = self.dynamodb.Table("users")

  def execute(
    self,
    id: str,
    name: str,
    age: int,
    address: str,
    tel: str,
  ) -> None:
    expression_values = {
      ':newName': name,
      ':newAge': age,
      ':newAddress': address,
      ':newTel': tel,
    }

    self.table.update_item(
        Key={
            'id': id
        },
        UpdateExpression="SET #name = :newName, age = :newAge, address = :newAddress, tel = :newTel",
        ExpressionAttributeNames= {
          '#name' : 'name'
        },
        ExpressionAttributeValues=expression_values
    )


def lambda_handler(event, context):
  body = json.loads(event['body'])

  update_user = UpdateUserUsecase()
  update_user.execute(
    id=body["id"],
    name=body["name"],
    age=body["age"],
    address=body["address"],
    tel=body["tel"],
  )
  return
