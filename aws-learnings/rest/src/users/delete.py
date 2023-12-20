import boto3

class DeleteUserUsecase:
  def __init__(self) -> None:
    self.dynamodb = boto3.resource("dynamodb")
    self.table = self.dynamodb.Table("users")

  def execute(self, id: str) -> None:
    self.table.delete_item(
      key={
        "id": id,
      },
    )


class DropTableUsecase:
  def __init__(self) -> None:
    self.dynamodb = boto3.resource("dynamodb")
    self.table = self.dynamodb.Table("users")

  def execute(self) -> None:
    self.table.delete()


def lambda_handler(event, context):
  if "id" not in event or not event["id"]:
    drop_table = DropTableUsecase()
    drop_table.execute()
    return


  id = event["id"]
  delete_user = DeleteUserUsecase()
  delete_user.execute(id=id)
  return
