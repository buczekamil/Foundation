from django.forms import ModelForm, ModelMultipleChoiceField, ModelChoiceField
from django.template.defaultfilters import register
from Base_app.models import Donation


class DonationForm(ModelForm):
    # category = ModelMultipleChoiceField(queryset=Category.objects.all())


    class Meta:
        model = Donation
        fields = [
            'quantity',
            'category',
            'institution',
            'address',
            'phone',
            'city',
            'zip_code',
            'pick_up_date',
            'pick_up_time',
            'pick_up_comment']

    widget = {'category': ModelMultipleChoiceField,
              'institution': ModelChoiceField

              }


@register.filter
def selected_category(form, field):
    return [label for value, label in form.fields[field].choices if value in form[field].value()]
