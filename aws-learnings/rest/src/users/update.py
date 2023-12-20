import boto3
import json


class CreateUserUsecase:
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
    # user = {
    #   "id": id,
    #   "name": name,
    #   "age": age,
    #   "address": address,
    #   "tel": tel,
    # }
    # self.table.put_item(
    #   Item=user,
    # )

    # todo 実装
    pass


def lambda_handler(event, context):
  body = json.loads(event['body'])

  create_user = CreateUserUsecase()
  create_user.execute(
    id=body["id"],
    name=body["name"],
    age=body["age"],
    address=body["address"],
    tel=body["tel"],
  )
  return
