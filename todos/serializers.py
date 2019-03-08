from shared.serializers import PageSerializer


def get_dto(todo, include_description=False):
    data = {
        'id': todo.id,
        'title': todo.title,
        'completed': todo.completed,
    }

    if include_description:
        data['description'] = todo.description
    data['created_at'] = todo.created_at
    data['updated_at'] = todo.updated_at

    return data


class TodoDetailsSerializer():
    def __init__(self, todo, messages=None):
        self.data = {'success': True}
        if messages is not None:
            if type(messages) == list:
                self.data['full_messages'] = messages
            elif type(messages) == str:
                self.data['full_messages'] = [messages]
        else:
            self.data['full_messages'] = []

        self.data.update(get_dto(todo, include_description=True))


class TodoListSerializer(PageSerializer):
    resource_name = 'todos'

    def __init__(self, todos_pagination, **kwargs):
        super(TodoListSerializer, self).__init__(todos_pagination, **kwargs)

    def get_dto(self, todo, **kwargs):
        return get_dto(todo, **kwargs)
