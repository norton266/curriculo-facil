const form = document.getElementById("form-chat");

const input = document.getElementById("mensagem");

const chat = document.getElementById("chat");

const botaoEnviar =
    document.getElementById("btn-enviar");


const barraProgresso =
    document.getElementById("barra-progresso");


const numeroProgresso =
    document.getElementById("progresso-numero");


const mensagemProgresso =
    document.getElementById("mensagem-progresso");

const btnGerarCurriculo = document.getElementById(
    "btn-gerar-curriculo"
);

btnGerarCurriculo.addEventListener(
    "click",
    gerarCurriculoPDF
);

async function gerarCurriculoPDF() {

    btnGerarCurriculo.disabled = true;
    btnGerarCurriculo.textContent = "Gerando currículo...";

    try {

        const resposta = await fetch(
            "/api/ia/gerar",
            {
                method: "POST"
            }
        );

        if (!resposta.ok) {

            const erro = await resposta.json();

            console.error(
                "Erro ao gerar currículo:",
                erro
            );

            alert(
                erro.detalhes
                    ? erro.detalhes.join("\n")
                    : "Não foi possível gerar o currículo."
            );

            return;
        }

        const blob = await resposta.blob();

        const url = window.URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;
        link.download = "curriculo.pdf";

        document.body.appendChild(link);

        link.click();

        link.remove();

        window.URL.revokeObjectURL(url);

    } catch (erro) {

        console.error(
            "Erro ao gerar PDF:",
            erro
        );

        alert(
            "Ocorreu um erro ao gerar o currículo."
        );

    } finally {

        btnGerarCurriculo.disabled = false;
        btnGerarCurriculo.textContent =
            "Gerar meu currículo em PDF";
    }
}


/* =========================================
   ETAPAS DO CURRÍCULO
========================================= */

const etapas = [

    "dados_pessoais",

    "experiencias",

    "formacoes",

    "certificacoes",

    "habilidades",

    "idiomas",

    "resumo"

];



/* =========================================
   NOMES DAS ETAPAS
========================================= */

const nomesEtapas = {

    dados_pessoais:
        "dados pessoais",

    experiencias:
        "experiência profissional",

    formacoes:
        "formação",

    certificacoes:
        "cursos e certificações",

    habilidades:
        "habilidades",

    idiomas:
        "idiomas",

    resumo:
        "resumo profissional"

};



/* =========================================
   SESSÃO DA CONVERSA
========================================= */

let sessao =
    localStorage.getItem(
        "curriculo_facil_sessao"
    );


if (!sessao) {

    sessao =
        crypto.randomUUID();

    localStorage.setItem(
        "curriculo_facil_sessao",
        sessao
    );

}



/* =========================================
   ADICIONAR MENSAGEM
========================================= */

function adicionarMensagem(
    texto,
    tipo
) {

    const mensagem =
        document.createElement("div");


    mensagem.classList.add(
        "mensagem",
        `mensagem-${tipo}`
    );


    if (tipo === "ia") {

        const avatar =
            document.createElement("div");

        avatar.classList.add(
            "mensagem-avatar"
        );

        avatar.textContent = "🤖";

        mensagem.appendChild(avatar);

    }


    const conteudo =
        document.createElement("div");


    conteudo.classList.add(
        "mensagem-conteudo"
    );


    conteudo.textContent = texto;


    mensagem.appendChild(conteudo);


    chat.appendChild(mensagem);


    chat.scrollTop =
        chat.scrollHeight;

}



/* =========================================
   MOSTRAR "PENSANDO..."
========================================= */

function mostrarCarregando() {

    const mensagem =
        document.createElement("div");


    mensagem.id =
        "mensagem-carregando";


    mensagem.classList.add(
        "mensagem",
        "mensagem-ia"
    );


    const avatar =
        document.createElement("div");


    avatar.classList.add(
        "mensagem-avatar"
    );


    avatar.textContent = "🤖";


    mensagem.appendChild(avatar);


    const conteudo =
        document.createElement("div");


    conteudo.classList.add(
        "mensagem-conteudo"
    );


    conteudo.textContent =
        "Pensando...";


    mensagem.appendChild(conteudo);


    chat.appendChild(mensagem);


    chat.scrollTop =
        chat.scrollHeight;

}



/* =========================================
   REMOVER "PENSANDO..."
========================================= */

function removerCarregando() {

    const mensagem =
        document.getElementById(
            "mensagem-carregando"
        );


    if (mensagem) {

        mensagem.remove();

    }

}



/* =========================================
   ATUALIZAR PROGRESSO
========================================= */

function atualizarProgresso(
    proximoCampo
) {

    let indiceAtual =
        etapas.indexOf(proximoCampo);


    /*
     * Se a IA não informou um campo
     * conhecido, não alteramos o progresso.
     */

    if (indiceAtual === -1) {

        return;

    }


    /*
     * Tudo que estiver antes do campo
     * atual é considerado concluído.
     */

    const etapasConcluidas =
        indiceAtual;


    const porcentagem =
        Math.round(
            (etapasConcluidas / etapas.length) * 100
        );


    barraProgresso.style.width =
        `${porcentagem}%`;


    numeroProgresso.textContent =
        `${porcentagem}%`;


    /*
     * Atualiza visualmente cada etapa.
     */

    document
        .querySelectorAll(".etapa")
        .forEach((elemento, index) => {

            elemento.classList.remove(
                "etapa-atual",
                "etapa-concluida"
            );


            if (index < indiceAtual) {

                elemento.classList.add(
                    "etapa-concluida"
                );

            }


            else if (index === indiceAtual) {

                elemento.classList.add(
                    "etapa-atual"
                );

            }

        });


    /*
     * Texto abaixo do progresso.
     */

    const nome =
        nomesEtapas[proximoCampo];


    if (nome) {

        mensagemProgresso.textContent =
            `Agora vamos falar sobre ${nome}.`;

    }

}



/* =========================================
   CURRÍCULO CONCLUÍDO
========================================= */


function finalizarProgresso() {

    barraProgresso.style.width = "100%";

    numeroProgresso.textContent = "100%";

    document
        .querySelectorAll(".etapa")
        .forEach((elemento) => {

            elemento.classList.remove(
                "etapa-atual"
            );

            elemento.classList.add(
                "etapa-concluida"
            );

        });

    mensagemProgresso.textContent =
        "Seu currículo está pronto!";

    btnGerarCurriculo.style.display = "block";

    btnGerarCurriculo.disabled = false;
}




/* =========================================
   ENVIAR MENSAGEM
========================================= */

form.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const mensagem =
            input.value.trim();


        /*
         * Não envia mensagem vazia.
         */

        if (!mensagem) {

            return;

        }


        /*
         * Mostra a mensagem do usuário.
         */

        adicionarMensagem(
            mensagem,
            "usuario"
        );


        /*
         * Limpa o campo.
         */

        input.value = "";


        /*
         * Bloqueia os controles enquanto
         * a IA está respondendo.
         */

        input.disabled = true;

        botaoEnviar.disabled = true;


        mostrarCarregando();


        try {

            const resposta =
                await fetch(
                    "/api/ia/conversar",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            mensagem:
                                mensagem,

                            sessao:
                                sessao

                        })
                    }
                );


            /*
             * Verifica se o servidor
             * respondeu com erro HTTP.
             */

            if (!resposta.ok) {

                throw new Error(
                    "Erro ao conversar com a IA."
                );

            }


            const dados =
                await resposta.json();

                console.log("Resposta completa da IA:", dados);
                console.log("Currículo pronto:", dados.curriculo_pronto);
                console.log("Próximo campo:", dados.proximo_campo);


            removerCarregando();


            /*
             * Mostra a resposta da IA.
             */

            if (dados.mensagem) {

                adicionarMensagem(
                    dados.mensagem,
                    "ia"
                );

            }


            /*
             * Atualiza o progresso.
             */

            if (dados.proximo_campo) {

                atualizarProgresso(
                    dados.proximo_campo
                );

            }

            if (dados.curriculo_pronto === true) {

                finalizarProgresso();

            } else {

                btnGerarCurriculo.style.display = "none";

            }


        }

        catch (erro) {

            console.error(erro);


            removerCarregando();


            adicionarMensagem(
                "Desculpe, ocorreu um erro ao conversar com a IA. Tente novamente.",
                "ia"
            );

        }


        finally {

            /*
             * Libera novamente o campo
             * de mensagem.
             */

            input.disabled = false;

            botaoEnviar.disabled = false;


            input.focus();

        }

    }
);