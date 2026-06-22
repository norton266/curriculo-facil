function removerItem(botao) {
    botao.parentElement.remove();
}


function adicionarItem(idContainer, html) {

    const container = document.getElementById(idContainer);

    container.insertAdjacentHTML("beforeend", html);
}


// função genérica, todos os formulários que adicionam itens em lista usam
function adicionar(tipo, container) {

    adicionarItem(
        container,
        templates[tipo]
    );

}