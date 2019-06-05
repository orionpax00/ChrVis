from django import forms
from .models import Document
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'matrix_file','annotation_file','email','password' )

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.layout = Layout(
            'email',
            'password',
            'title',
            'matrix_file',
            'annotation_file'
        )
