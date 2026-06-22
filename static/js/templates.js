const templates = {

    experiencia: `
    <div class="experiencia-item">

        <input type="text" name="cargo[]" placeholder="Cargo">
        <input type="text" name="empresa[]" placeholder="Empresa">
        <input type="text" name="periodo[]" placeholder="Período">
        <textarea name="descricao[]" placeholder="Descrição"></textarea>

        <button type="button" class="botao-remover" onclick="removerItem(this)">
            Remover
        </button>

    </div>
    `,

    formacao: `
    <div class="formacao-item">
        <input type="text" name="curso[]" placeholder="Curso">
        <input type="text" name="instituicao[]" placeholder="Instituição">

        <button type="button" class="botao-remover" onclick="removerItem(this)">
            Remover
        </button>
    </div>
    `,

    certificacao: `
    <div class="certificacao-item">
        <input type="text" name="certificacao[]" placeholder="Certificação">

        <button type="button" class="botao-remover" onclick="removerItem(this)">
            Remover
        </button>
    </div>
    `,

    habilidade: `
    <div class="habilidade-item">
        <input type="text" name="habilidade[]" placeholder="Habilidade">

        <button type="button" class="botao-remover" onclick="removerItem(this)">
            Remover
        </button>
    </div>
    `,

    idioma: `
    <div class="idioma-item">
        <input type="text" name="idioma[]" placeholder="Idioma">

        <button type="button" class="botao-remover" onclick="removerItem(this)">
            Remover
        </button>
    </div>
    `
}