from app.schemas.BaseSchemas import BaseSchema

class ChatMessagesSchema(BaseSchema):

	message : str
	chat_user_id : int
	chat_id : int