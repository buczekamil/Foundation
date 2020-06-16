from django.forms import ModelForm, forms, ModelMultipleChoiceField, ModelChoiceField

from Base_app.models import Donation, Category


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
