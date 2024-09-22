# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
import os
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from .models import Profile
import re
from openai import OpenAI
from twilio.rest import Client

client = OpenAI()


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect("/memo/login")

    context = {'form': form}
    return render(request, "Accounts/register.html", context)


def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/memo/chat")
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, "Accounts/login.html",context)

def logoutUser(request):
    logout(request)
    return redirect("/memo/login")

@csrf_exempt
def process_audio(request):
    if request.method == 'POST' and request.FILES['audio_file']:
        audio_file = request.FILES['audio_file']
    
        # Guardar el archivo temporalmente
        audio_path = f'temp/{audio_file.name}'
        with open(audio_path, 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)
        
        text = audio_to_text(audio_path)
        response_text = response(text)
        status, response_text = separate_string(response_text)
        
        print(status)
        output_audio_path = response_to_speech(response_text)
        
        
        if status == "S":
            
            profile = Profile.objects.get(user=request.user)
            emergency_phone = profile.emergency_phone
            name = profile.full_name
            account_sid = "ACac918f742f70d937efed69dc27b344d2"
            auth_token = "06b9c952cc1b5c46a2248d21e580ffc0"
            client = Client(account_sid, auth_token)
            print(emergency_phone)
            call = client.calls.create(
                twiml='<Response><Say>Hello! We are contacting you from memo (a mental health advisor) we noticed that {name} who registered you as an emergency contact is at risk, please contact him or her as fast as posible</Say></Response>',
                to= emergency_phone,
                from_="+12065392866"
            )

            print(call.sid)
        return JsonResponse({'audio_url': f'/memo/media/output.mp3'})

    return JsonResponse({'error': 'Invalid request'}, status=400)


from django.shortcuts import render

def index(request):
    return render(request, 'chat.html')

def realindex (request):
    return render(request, "index.html")




def audio_to_text(path):
  audio_file= open(path, "rb")
  transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
  )
  audio_to_text=transcription.text
  print(audio_to_text)
  return audio_to_text

def response_to_speech(response_text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=response_text,  
    )

    output_path = "../memo/media/output.mp3"
    response.stream_to_file(output_path)
    return output_path


def response (prompt):
  completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role": "system", "content": "You are a mental health counselor. Your role is to advise people on their daily life problems, as well as identify potential individuals at risk of suicide. Your responses must follow the format: [status], response. The status can be either S or N, representing whether the individual is a potential suicide risk or not. It is important that you use brackets around the status."},
          {
              "role": "user",
                "content": f"{prompt}"
            }
        ]
    )
  print(completion.choices[0].message.content)
  return completion.choices[0].message.content



def separate_string(cadena):
    match = re.match(r"\[(.*?)\](.*)", cadena)
    
    if match:
        brackets = match.group(1).strip()  
        response = match.group(2).strip()  
        return brackets, response
    else:
        return None, cadena  
