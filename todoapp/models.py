from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class ToDoAppModelManager(models.Manager):
    # def get_queryset(self):
    #     return super().get_queryset().filter(is_active=True)
    pass


class ToDoAppBaseModel(models.Model):
    objects = ToDoAppModelManager()

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"), editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name=_("updated"), editable=False)
    is_active = models.BooleanField(default=True, verbose_name=_("is_active"))

    def delete(self, *args):
        self.is_active = True
        self.save()

    def restore(self, *args):
        self.is_active = True
        self.save()

    class Meta:
        abstract = True


class Project(ToDoAppBaseModel):
    title = models.CharField(_("title"), max_length=150, blank=False)
    repo = models.CharField(_("repo"), max_length=255, blank=False)
    users = models.ManyToManyField(get_user_model())

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ("-created",)


class ToDo(ToDoAppBaseModel):
    text = models.CharField(_("title"), max_length=1000, blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_("project"))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("author"))
    is_completed = models.BooleanField(default=False, verbose_name=_("is_completed"))

    def __str__(self) -> str:
        return f"{self.text}"

    class Meta:
        verbose_name = _("ToDo")
        verbose_name_plural = _("ToDos")
        ordering = ("-created",)
