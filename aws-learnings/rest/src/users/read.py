import json
import boto3
from typing import Any

class LambdaException(Exception):
    def __init__(self, status_code: int, error_msg: str):
        self.status_code = status_code
        self.error_msg = error_msg

    def __str__(self):
        obj = {
            "statusCode": self.status_code,
            "errorMessage": self.error_msg
        }
        return json.dumps(obj)


class NotFoundException(LambdaException):
    def __init__(self, error_msg: str):
        super().__init__(404, error_msg)


class GetUserUsecase:
  def __init__(self) -> None:
    self.dynamodb = boto3.resource("dynamodb")
    self.table = self.dynamodb.Table("users")

  def execute(self, id: str) -> None:
    user = self.table.get_item(
      Key={
        'id': id,
      }
    )

    if "Item" not in user:
      raise NotFoundException('user not found.')
    return user["Item"]


class GetAllUsersUsecase:
  def __init__(self) -> None:
    self.dynamodb = boto3.resource("dynamodb")
    self.table = self.dynamodb.Table("users")

  def execute(self) -> Any:
    return self.table.scan()["Items"]


def lambda_handler(event, context):
  if "id" not in event or not event["id"]:
    get_all = GetAllUsersUsecase()
    return get_all.execute()


  id = event["id"]
  get_user = GetUserUsecase()
  return get_user.execute(id=id)
