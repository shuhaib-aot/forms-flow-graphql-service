from src.models.formio.form import FormModel
from src.graphql.types.formio_form import Form


async def get_forms_from_formio():
    """Fetch all users from MongoDB"""
    forms = await FormModel.find_all().to_list()
    return [
        Form(
            id=str(form.id),
            name=form.name,
            path=form.path,
            type=form.type,
            display=str(form.display),
        )
        for form in forms
    ]
