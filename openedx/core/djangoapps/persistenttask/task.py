from celery.tasks import Task

from .models import FailedTask

def serialize_value(value):
    pass

def serialize_args(args):
    """
    Combine args into a single string
    """



def serialize_kwargs(kwargs):
    """
    Combine args into a single string
    """


class PersistentTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if not kwargs.pop('_persistent_task_retried', False):
            FailedTask.objects.create(
                task_name=self.name,
                task_id=task_id,
                args=serialize_args(args),
                kwargs=serialize_kwargs(kwargs),
                exc=exc,
                einfo=einfo,
            )
