document.addEventListener('DOMContentLoaded', () => {
    const animationWrapper = document.getElementById('animation-wrapper');
    const content = document.getElementById('content');
    const circleExpand = document.querySelector('.circle-expand');
    const micButton = document.getElementById('mic');
    const playback = document.querySelector('.playback');
    
    let can_record = false;
    let is_recording = false;
    let recorder = null;
    let chunks = [];

    // Función para mostrar el contenido después de la animación
    circleExpand.addEventListener('animationend', () => {
        animationWrapper.style.display = 'none';
        content.classList.remove('hidden');
        content.style.opacity = '1';
        content.style.transform = 'scale(1)';
    });

    // Configurar el acceso al micrófono y la grabación
    function SetupAudio() {
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ audio: true })
                .then(SetupStream)
                .catch(err => {
                    console.error(err);
                });
        }
    }

    function SetupStream(stream) {
        recorder = new MediaRecorder(stream);

        recorder.ondataavailable = e => {
            chunks.push(e.data);
        };

        recorder.onstop = e => {
            const blob = new Blob(chunks, { type: "audio/ogg; codecs=opus" });
            chunks = [];
            const formData = new FormData();
            formData.append('audio_file', blob, 'user_audio.ogg');

            // Envía el archivo de audio al servidor
            fetch('/memo/process_audio/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.audio_url) {
                    // Cargar la URL en el reproductor y reproducir
                    playback.src = data.audio_url;
                    playback.play();

                    // Deshabilitar el botón mientras se reproduce el audio
                    micButton.disabled = true;
                } else {
                    console.error('Error: No se recibió la URL del archivo de audio');
                }
            })
            .catch(error => console.error('Error al procesar el audio:', error));
        };

        can_record = true;
    }

    // Alternar la grabación de audio
    function ToggleMic() {
        if (!can_record) return;

        is_recording = !is_recording;

        if (is_recording) {
            recorder.start();
            micButton.textContent = ""; // Mostrar estado de grabación
        } else {
            recorder.stop();
            micButton.textContent = "Tell me more!"; // Mostrar que dejó de grabar
        }
    }

    // Habilitar el botón cuando termina la reproducción del audio
    playback.addEventListener('play', function() {
        micButton.disabled = true; // Deshabilitar el botón
      });

    playback.addEventListener('ended', function() {
        micButton.disabled = false; // Rehabilitar el botón al terminar el audio
    });

    // Habilitar el botón cuando el audio se pausa
    playback.addEventListener('pause', function() {
        micButton.disabled = false; // Rehabilitar el botón si se pausa el audio
    });

    // Alternar la clase 'active' al hacer clic en el botón de micrófono
    micButton.addEventListener('click', ToggleMic);
    micButton.addEventListener('click', () => {
        micButton.classList.toggle('active');
    });

    // Inicializar la configuración de audio
    SetupAudio();
    const mic_btn = document.querySelector('#mic'); 

// Evento para cuando comienza la reproducción del audio
playback.addEventListener('play', () => {
    mic_btn.classList.add('is-playing'); // Añadir la clase para la animación
});

// Evento para cuando el audio se detiene o termina
playback.addEventListener('pause', () => {
    mic_btn.classList.remove('is-playing'); // Quitar la clase para detener la animación
});

playback.addEventListener('ended', () => {
    mic_btn.classList.remove('is-playing'); // Quitar la clase cuando el audio termine
});

});


