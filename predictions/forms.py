from django.forms import ModelForm
from .models import Prediction

class PredictionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PredictionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Prediction
        fields = ['result']
