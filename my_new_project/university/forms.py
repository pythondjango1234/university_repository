from django import forms
from multiselectfield import MultiSelectFormField
class FeedBackFrom(forms.Form):
    name= forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )

    )
    feedback = forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Give Your Feedback'
            }
        )
    )
class ContactForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Name'

            }
        )

    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email'
                }
        )
    )
    mobile = forms.IntegerField(
        label="Enter your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Number'
            }
        )
    )
    COURSES_CHOICES = (
        ('py', 'Python'),
        ('dj', 'Django'),
        ('ui', 'UI'),
        ('rest', 'REST API')
    )
    courses=MultiSelectFormField(max_length=200,choices=COURSES_CHOICES)

    SHIFTS_CHOICES=(
        ('mrg','Morning'),
        ('aftrn','Afternoon'),
        ('evng','Evening'),
        ('night','Night')
    )
    shifts=MultiSelectFormField(max_length=200,choices=SHIFTS_CHOICES)

    LOCATIONS_CHOICES = (
        ('hyd','Hyderbad'),
        ('bang','Banglore'),
        ('pune','pune'),
        ('chn','Chennai')
    )
    locations=MultiSelectFormField(max_length=200,choices=LOCATIONS_CHOICES)

    GENDER_CHOICE=(
        ('m','Male'),
        ('f','Female')

    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(), choices=GENDER_CHOICE
    )

    start_date=forms.DateField(
        widget=forms.SelectDateWidget()
    )




