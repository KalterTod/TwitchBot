import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import Message
from app import utils, db


class MessageObject(SQLAlchemyObjectType):
    class Meta:
        model = Message
        interfaces = (graphene.relay.Node, )

class MessageAttribute:
    message = graphene.String(description="Message contents.")
    channel_name = graphene.String(description="Twitch Channel Name")

class CreateMessageInput(graphene.InputObjectType, MessageAttribute):
    """Arguments to create a message."""
    pass

class CreateMessage(graphene.Mutation):
    message = graphene.Field(lambda: MessageObject, description="Message created.")

    class Arguments: 
        input = CreateMessageInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)

        message = Message(**data)
        db.session.add(message)
        db.session.commit()

        return CreateMessage(message=message)


class Query(graphene.ObjectType):
    message = graphene.relay.Node.Field(MessageObject)

class Mutation(graphene.ObjectType):
    createMessage = CreateMessage.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

