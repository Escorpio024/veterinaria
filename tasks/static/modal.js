// Ventanas modales
const open = document.getElementById('open');
const modal = document.getElementById('modal1');
const close = document.getElementById('close');

open.addEventListener('click', (e) => {
    e.preventDefault();
    modal.classList.add('show');  
});

close.addEventListener('click', (e) => {
    e.preventDefault();
    modal.classList.remove('show');
});

const open2 = document.getElementById('open2');
const modal2 = document.getElementById('modal2');
const close2 = document.getElementById('close2');

open2.addEventListener('click', (e) => {
    e.preventDefault();
    modal2.classList.add('show');  
});

close2.addEventListener('click', (e) => {
    e.preventDefault();
    modal2.classList.remove('show');
});

const open3 = document.getElementById('open3');
const modal3 = document.getElementById('modal3');
const close3 = document.getElementById('close3');

open3.addEventListener('click', (e) => {
    e.preventDefault();
    modal3.classList.add('show');  
});

close3.addEventListener('click', (e) => {
    e.preventDefault();
    modal3.classList.remove('show');
});

const open4 = document.getElementById('open4');
const modal4 = document.getElementById('modal4');
const close4 = document.getElementById('close4');

open4.addEventListener('click', (e) => {
    e.preventDefault();
    modal4.classList.add('show');  
});

close4.addEventListener('click', (e) => {
    e.preventDefault();
    modal4.classList.remove('show');
});

const open5 = document.getElementById('open5');
const modal5 = document.getElementById('modal5');
const close5 = document.getElementById('close5');

open5.addEventListener('click', (e) => {
    e.preventDefault();
    modal5.classList.add('show');  
});

close5.addEventListener('click', (e) => {
    e.preventDefault();
    modal5.classList.remove('show');
});

const open6 = document.getElementById('open6');
const modal6 = document.getElementById('modal6');
const close6 = document.getElementById('close6');

open6.addEventListener('click', (e) => {
    e.preventDefault();
    modal6.classList.add('show');  
});

close6.addEventListener('click', (e) => {
    e.preventDefault();
    modal6.classList.remove('show');
});

const open7 = document.getElementById('open7');
const modal7 = document.getElementById('modal7');
const close7 = document.getElementById('close7');

open7.addEventListener('click', (e) => {
    e.preventDefault();
    modal7.classList.add('show');  
});

close7.addEventListener('click', (e) => {
    e.preventDefault();
    modal7.classList.remove('show');
});

const open8 = document.getElementById('open8');
const modal8 = document.getElementById('modal8');
const close8 = document.getElementById('close8');

open8.addEventListener('click', (e) => {
    e.preventDefault();
    modal8.classList.add('show');  
});

close8.addEventListener('click', (e) => {
    e.preventDefault();
    modal8.classList.remove('show');
});

const open9 = document.getElementById('open9');
const modal9 = document.getElementById('modal9');
const close9 = document.getElementById('close9');
const consultaGeneralTextarea = document.getElementById('consulta_general');
const enviarConsultaGeneralButton = document.getElementById('enviarConsultaGeneral');
const mensajeConsultaGeneral = document.getElementById('mensajeConsultaGeneral');

open9.addEventListener('click', (e) => {
    e.preventDefault();
    modal9.classList.add('show');  
});

close9.addEventListener('click', (e) => {
    e.preventDefault();
    modal9.classList.remove('show');
    consultaGeneralTextarea.value = ''; 
    mensajeConsultaGeneral.textContent = '';
});

enviarConsultaGeneralButton.addEventListener('click', () => {

    const consultaGeneralTexto = consultaGeneralTextarea.value.trim();

    if (consultaGeneralTexto !== '') {
        mensajeConsultaGeneral.textContent = 'Consulta General Enviada Correctamente';

        consultaGeneralTextarea.value = ''; 
        setTimeout(() => {
            mensajeConsultaGeneral.textContent = '';
        }, 4000);
    } else {
        mensajeConsultaGeneral.textContent = 'Por favor, ingrese su consulta antes de enviar.';
        setTimeout(() => {
            mensajeConsultaGeneral.textContent = '';
        }, 4000);
    }
});



const open10 = document.getElementById('open10');
const modal10 = document.getElementById('modal10');
const close10 = document.getElementById('close10');
const consultaCardiologicaTextarea = document.getElementById('consulta_cardiologica');
const enviarConsultaCardiologicaButton = document.getElementById('enviarConsultaCardiologica');
const mensajeConsultaCardiologica = document.getElementById('mensajeConsultaCardiologica');

open10.addEventListener('click', (e) => {
    e.preventDefault();
    modal10.classList.add('show');  
});

close10.addEventListener('click', (e) => {
    e.preventDefault();
    modal10.classList.remove('show');
    consultaCardiologicaTextarea.value = ''; 
    mensajeConsultaCardiologica.textContent = '';
});

enviarConsultaCardiologicaButton.addEventListener('click', () => {

    const consultaCardiologicaTexto = consultaCardiologicaTextarea.value.trim();

    if (consultaCardiologicaTexto !== '') {
        mensajeConsultaCardiologica.textContent = 'Consulta Cardiológica Enviada Correctamente';

        consultaCardiologicaTextarea.value = ''; 
        setTimeout(() => {
            mensajeConsultaCardiologica.textContent = '';
        }, 4000);
    } else {
        mensajeConsultaCardiologica.textContent = 'Por favor, ingrese su consulta antes de enviar.';
        setTimeout(() => {
            mensajeConsultaCardiologica.textContent = '';
        }, 4000);
    }
});
