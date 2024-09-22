from openai import OpenAI

client = OpenAI()

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
        voice="alloy",
        input=response_text,  # Asegúrate de pasar el texto generado
    )

    output_path = "output.mp3"
    response.stream_to_file(output_path)
    return output_path


def response (prompt):
  completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role": "system", "content": "You are a mental health advisor. Your job is to prevent people from commiting suicide."},
          {
              "role": "user",
                "content": f"{prompt}"
            }
        ]
    )
  return completion.choices[0].message.content
