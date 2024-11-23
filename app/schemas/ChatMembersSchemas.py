from app.schemas.BaseSchemas import BaseSchema

class ChatsMembersSchema(BaseSchema):

	chat_user_id : int
	chat_id : int