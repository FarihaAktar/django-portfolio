
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Skill


class UserUpdateForm(forms.ModelForm):
    # name = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    phone = forms.IntegerField()
    # image = forms.ImageField(upload_to='photos/self')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
            
            # print("instance",self.fields['phone'])
        # jodi user er account thake 
        if self.instance:
            try:
                user_profile = self.instance
                
            except Profile.DoesNotExist:
                user_profile = None
               
            print(user_profile)
            # if user_profile:
            #     self.fields['phone'].initial = user_profile.phone
           

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     if commit:
    #         user.save()

    #         user_profile, created = Profile.objects.get_or_create(user=user) # jodi account thake taile seta jabe user_account ar jodi account na thake taile create hobe ar seta created er moddhe jabe
            

    #         user_profile.phone = self.cleaned_data['phone']
         
         
    #         user_profile.save()

          

        return None