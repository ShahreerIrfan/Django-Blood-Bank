from django import forms
from .models import Support
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        exclude = ['who_need_support']

    def __init__(self, *args, **kwargs):
        super(SupportForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit', css_class='w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded'))
