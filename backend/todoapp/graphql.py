import graphene
from graphene_django import DjangoObjectType

from todoapp.models import Project, ToDo
from userapp.models import CustomUser


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = "__all__"


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = "__all__"


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "first_name", "last_name", "is_superuser", "is_staff", "date_joined"]


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, pk=graphene.Int(required=True))

    all_todos = graphene.List(ToDoType)
    todos_by_author_name = graphene.List(ToDoType, username=graphene.String(required=False))

    all_projects = graphene.List(ProjectType)
    project_by_title = graphene.List(ProjectType, title=graphene.String(required=False))

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    def resolve_user_by_id(self, info, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return None

    def resolve_all_todos(root, info):
        return ToDo.objects.all()

    def resolve_todos_by_author_name(self, info, username=None):
        todos = ToDo.objects.all()
        if username:
            todos = todos.filter(author__username__contains=username)
        return todos

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_project_by_title(root, info, title):
        if title:
            return Project.objects.filter(title__contains=title)
        return Project.objects.all()


class ToDoCreateMutation(graphene.Mutation):
    todo = graphene.Field(ToDoType)

    class Arguments:
        text = graphene.String(required=True)
        author_pk = graphene.Int(required=True)
        project_pk = graphene.Int(required=True)
        is_completed = graphene.Boolean(required=False)

    @classmethod
    def mutate(cls, root, info, text, project_pk, author_pk, is_completed=False):
        author: CustomUser = CustomUser.objects.get(pk=author_pk)
        project: Project = Project.objects.get(pk=project_pk)
        todo: ToDo = ToDo.objects.create(text=text, project=project, is_completed=is_completed, author=author)
        todo.save()
        return cls(todo=todo)


class ToDoUpdateMutation(graphene.Mutation):
    todo = graphene.Field(ToDoType)

    class Arguments:
        pk = graphene.ID()
        text = graphene.String(required=False)
        author_pk = graphene.Int(required=False)
        project_pk = graphene.Int(required=False)
        is_completed = graphene.Boolean(required=False)

    @classmethod
    def mutate(cls, root, info, pk, text=None, project_pk=None, author_pk=None, is_completed=False):
        todo: ToDo = ToDo.objects.get(pk=pk)
        if text:
            todo.text = text
        if project_pk:
            project: Project = Project.objects.get(pk=project_pk)
            todo.project = project
        if author_pk:
            author: CustomUser = CustomUser.objects.get(pk=author_pk)
            todo.author = author
        if is_completed:
            todo.is_completed = is_completed
        todo.save()
        return cls(todo=todo)


class Mutation(graphene.ObjectType):
    create_todo = ToDoCreateMutation.Field()
    update_todo = ToDoUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


"""
Примеры запросов:
{
	allProjects {
    id
    title
    repo
    todoSet {
      text
      isCompleted
      author {
        id
        isSuperuser
        username
        firstName
        lastName
      }
    }
  }
}

{
  allTodos{
    id
    created
    updated
    isActive
    text
    isCompleted
    project {
      id
      title
      repo
      users {
        id
        username
      }
    }
    author {
      id
      isSuperuser
      username
      firstName
      lastName
    }
  }
}

Пример сложного запроса:
{
  todosByAuthorName (username: "admin") {
    id
    text
    author {
      dateJoined
      username
    }
    project {
      title
      users {
        username
        isSuperuser
      }
      todoSet {
        id
        text
        isCompleted
      }
    }
  }
}


Примеры запросов на изменение данных:

mutation {
  createTodo (
    authorPk:1,
    projectPk: 2,
    text: "Some new ToDo."
  ) {
    todo {
      id
      created
      text
      project {
        id
        title
        repo
      }
      author {
        id
        username
        isSuperuser
      }
    }
  }
}

mutation {
  updateTodo (
		pk: 14,
    text: "Some CHANGED new ToDo."
  ) {
    todo {
      id
      created
      text
      project {
        id
        title
        repo
      }
      author {
        id
        username
        isSuperuser
      }
    }
  }
}
"""
