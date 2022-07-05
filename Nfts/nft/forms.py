from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import * 

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
 
class addCryptoQuestionform(ModelForm):
    class Meta:
        model=CryptoQuesModel
        fields="__all__"

class addBlockchainQuestionform(ModelForm):
    class Meta:
        model = BlockchainQuesModel
        fields="__all__"

class addBitcoinQuestionform(ModelForm):
    class Meta:
        model = BitcoinQuesModel
        fields="__all__"

class addEtheriumQuestionform(ModelForm):
    class Meta:
        model = EtheriumQuesModel
        fields="__all__"

class addNFTSQuestionform(ModelForm):
    class Meta:
        model = NFTSQuesModel
        fields="__all__"

class addCorrelationQuestionform(ModelForm):
    class Meta:
        model = CorrelationQuesModel
        fields="__all__"

class addWiseQuestionform(ModelForm):
    class Meta:
        model = WiseQuesModel
        fields="__all__"

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = "__all__"