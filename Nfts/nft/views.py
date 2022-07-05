from http.client import HTTPResponse
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User, auth
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def homeView(request):
    return render(request,'nft/home.html')

def logInView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'nft/logIn.html',context)

def registerView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method=='POST':
            form = UserCreationForm(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context = {'form':form,}
        
        return render(request,'nft/register.html',context)

def logoutView(request):
    logout(request)
    return redirect('/')

def cryptoView(request):
    return render(request, 'nft/crypto.html')


def bitcoinView(request):
    return render(request, 'nft/bitcoin.html')

def blockchainView(request):
    return render(request, 'nft/blockchain.html')

def correlationView(request):
    return render(request, 'nft/correlation.html')

def etheriumView(request):
    return render(request, 'nft/etherium.html')

def whatView(request):
    return render(request, 'nft/what.html')

def wiseView(request):
    return render(request, 'nft/wise.html')

def addCryptoView(request):
    if request.user.is_staff:
        form=addCryptoQuestionform()
        if(request.method=='POST'):
            form=addCryptoQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'nft/addCrypto.html',context)
    else: 
        return redirect('home')

def cryptoQuizView(request):
    if request.method == 'POST':
        questions=CryptoQuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(q.ans)
            print(request.POST[q.question])
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'nft/result.html',context)
    else:
        questions=CryptoQuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'nft/quizCrypto.html',context)


def addBlockchainView(request):
    if request.user.is_staff:
        form=addBlockchainQuestionform()
        if(request.method=='POST'):
            form=addBlockchainQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'nft/addBlockchain.html',context)
    else: 
        return redirect('home')

def BlockchainQuizView(request):
    if request.method == 'POST':
        questions=BlockchainQuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(q.ans)
            print(request.POST[q.question])
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'nft/result.html',context)
    else:
        questions=BlockchainQuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'nft/quizBlockchain.html',context)

def addBitcoinView(request):
    if request.user.is_staff:
        form=addBitcoinQuestionform()
        if(request.method=='POST'):
            form=addBitcoinQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'nft/addBitcoin.html',context)
    else: 
        return redirect('home')

def BitcoinQuizView(request):
    if request.method == 'POST':
        questions=BitcoinQuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(q.ans)
            print(request.POST[q.question])
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'nft/result.html',context)
    else:
        questions=BitcoinQuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'nft/quizBlockchain.html',context)

def addEtheriumView(request):
    if request.user.is_staff:
        form=addEtheriumQuestionform()
        if(request.method=='POST'):
            form=addEtheriumQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'nft/addEtherium.html',context)
    else: 
        return redirect('home')

def EtheriumQuizView(request):
    if request.method == 'POST':
        questions=EtheriumQuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(q.ans)
            print(request.POST[q.question])
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'nft/result.html',context)
    else:
        questions=EtheriumQuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'nft/quizEtherium.html',context)

def addNftsView(request):
    if request.user.is_staff:
        form=addNFTSQuestionform()
        if(request.method=='POST'):
            form=addNFTSQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'nft/addNfts.html',context)
    else: 
        return redirect('home')


def NftsQuizView(request):
    if request.method == 'POST':
        questions=NFTSQuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(q.ans)
            print(request.POST[q.question])
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'nft/result.html',context)
    else:
        questions=NFTSQuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'nft/quizNfts.html',context)

def addCorrelationView(request):
    if request.user.is_staff:
        form=addCorrelationQuestionform()
        if(request.method=='POST'):
            form=addCorrelationQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'nft/addCorrelation.html',context)
    else: 
        return redirect('home')

def CorrelationQuizView(request):
    if request.method == 'POST':
        questions=CorrelationQuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(q.ans)
            print(request.POST[q.question])
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'nft/result.html',context)
    else:
        questions=CorrelationQuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'nft/quizCorrelation.html',context)


def addWiseView(request):
    if request.user.is_staff:
        form=addWiseQuestionform()
        if(request.method=='POST'):
            form=addWiseQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'nft/addWise.html',context)
    else: 
        return redirect('home')

def WiseQuizView(request):
    if request.method == 'POST':
        questions=WiseQuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(q.ans)
            print(request.POST[q.question])
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'nft/result.html',context)
    else:
        questions=WiseQuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'nft/quizWise.html',context)

def cryptoSecondView(request):
    return render(request,'nft/cryptoSecond.html')

def bitcoinSecondView(request):
    return render(request,'nft/bitcoinSecond.html')

def bitcoinThirdView(request):
    return render(request,'nft/bitcoinThird.html')

def etheriumSecondView(request):
    return render(request,'nft/etheriumSecond.html')

def correlationSecondView(request):
    return render(request,"nft/correlationSecond.html")

def correlationThirdView(request):
    return render(request,'nft/correlationThird.html')

def correlationFourthView(request):
    return render(request,'nft/correlationFourth.html')

def AddCommentsView(request):
    if(request.user.is_authenticated):
        form = CommentForm()
        if(request.method=='POST'):
            form = CommentForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('comments')
        context={'form':form}
        return render(request,'nft/addComments.html',context)
    else:
        return redirect("login")
    
def CommentsView(request):
    komentari = Comments.objects.all()
    for k in komentari:
        print(k.name)

    context = {
            'komentari':komentari
        }
    return render(request,'nft/comments.html',context)
