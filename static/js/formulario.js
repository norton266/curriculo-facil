// ==========================
// FUNÇÃO GENÉRICA DE CLONE
// ==========================

function adicionarCampo(containerId, className) {

    const container = document.getElementById(containerId);

    const template = container.querySelector("." + className);

    const clone = template.cloneNode(true);

    // limpa inputs do clone
    const inputs = clone.querySelectorAll("input, textarea");

    inputs.forEach(input => input.value = "");

    container.appendChild(clone);
}

function adicionarExperiencia() {
    adicionarCampo("experiencias", "experiencia");
}

function adicionarFormacao() {
    adicionarCampo("formacoes", "formacao");
}

function adicionarCertificacao() {
    adicionarCampo("certificacoes", "certificacao");
}

function adicionarHabilidade() {
    adicionarCampo("habilidades", "habilidade");
}

function adicionarIdioma() {
    adicionarCampo("idiomas", "idioma");
}