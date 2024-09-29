from django.db.models import UniqueConstraint


def unique_together_constraint(*fields: str, **kwargs) -> UniqueConstraint:
    """Generate a UniqueConstraint with a sensible name"""
    name = f"%(app_label)s_%(class)s_{'_'.join(sorted(fields))}_uniq"
    return UniqueConstraint(fields=tuple(fields), name=name, **kwargs)
