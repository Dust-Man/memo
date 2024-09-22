# memo
## Virtual Psychologist Asisted by AI

### General description
memo Ai is a virtual psychologist that uses artificial inteligence to process user's voice and develop answers in audio format as if it was a real interaction, providing a really fluid experience that's accessible and affordable for everyone. Its main objective is to prevent suicides and give some company to those who are in need because of a stressful, sad, or hard situation. If the AI detects possibilities that the user could harm himself by analizing their voice and words, it will immediatly call its emergency contact for it to help the user as soon as possible. This call has a personalized message depending on the user in risk, which can help the people answering to identify the person in risk.

### Main characteristics
- memo is free and adaptive to mobile devices, regardless of screen size or operating software. Therefore, a wide range of audiences can be reached.
- Use of OpenAI Whisper API to convert from voice (audio) to text for it to be analized.
- Processing of text with GPT-4 model from OpenAI to personaliza each conversation and help from the best way.
- Responses with audio generated using OpenAI TTS (Text-to-Speech) API.
- Web interface was constructed with Django, which led us easily record audio and easily implement AI.
- Twilio API was integrated to make automatic calls if a user is in risk of suicide with the objective of preventing any harmful action.

### Technologies
- **Backend**: [Django](https://www.djangoproject.com/) - Framework web en Python.
- **Frontend**: HTML5, CSS3, JavaScript.
- **API de Inteligencia Artificial**: [OpenAI API](https://beta.openai.com/docs/)
- **Audio a Texto**: [Whisper API de OpenAI](https://openai.com/research/whisper).
- **Text-to-Speech (TTS)**: [OpenAI TTS API](https://beta.openai.com/docs/guides/speech-to-text).
- **Automatic calls**: [Twilio API](https://www.twilio.com/docs/usage/api).

### Recursos Externos / Open Source Utilizados
- [OpenAI API Documentation](https://beta.openai.com/docs/)
- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Twilio API Documentation](https://www.twilio.com/docs/usage/api)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

### Contributors
Josué Iram Tijerina de León (josue.tijerina@outlook.com)<\b>
Emilio Puga Ascencio (emilio.puga@live.com)<\b>
Carlos Gael Hernández Parrilla (carlosgaelhp@gmail.com)<\b>
Sohit Patro (sohitpatro25@solonschools.net)<\b>

