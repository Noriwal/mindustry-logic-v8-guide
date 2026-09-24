# Catálogo de esquemas comunitários úteis

Levantamento em 24/09/2026 no [Mindustry Schematics](https://mindustryschematics.com/), catálogo **não oficial** de esquemas enviados por usuários. O catálogo apresentava busca por nome e tags e cerca de 2.995 esquemas na consulta. As descrições abaixo são as alegações dos autores nas respectivas páginas; **não** extraí código dos processadores nem confirmei funcionamento na V8. A referência a um esquema não transfere autoria para este repositório.

| Projeto nosso | Esquema e autor, quando indicado | Ideia a examinar | Limite conhecido |
| --- | --- | --- | --- |
| Horizon | [Xenith v34.5](https://mindustryschematics.com/schematics/662677c574d219bb2055ca58), Ricochet_Master | Modos de ataque e defesa, padrão de bombardeio distribuído e convergência das unidades para um ponto; flags que evitam tomar unidades de outro controlador | Usa Zenith, vários modos e controles por arc/sorter; adaptar apenas o conceito de formação, sem presumir que serve para Horizon. |
| Horizon | [L-UnitSquadControl](https://mindustryschematics.com/schematics/62ed2c62d53a9d7c4771f98e) | Quantidade configurável de unidades, comando de agrupar e ataque em esquadrão | Descrição curta; verificar como distribui posições e se todas obedecem ao mesmo alvo. |
| Horizon/Flare | [Better unit control v2](https://mindustryschematics.com/schematics/667b139e73cec42f11bef6af) | Diz controlar Flare, Horizon, Zenith e Quad | A [versão anterior](https://mindustryschematics.com/schematics/666c53cffe14c8c776075b99) declara Flare e Horizon quebrados. Tratar v2 como hipótese até inspeção e teste. |
| Quasar | [mono miner v1.3](https://mindustryschematics.com/schematics/64dbe5b98b129e2a66e78ae5), Hyperion | Tipo e número de unidades configuráveis, sorter para recurso, depósito extra ou núcleo, busca de areia e outros minérios, descarte de carga incompatível | Autor informa que **não verifica limites do armazenamento**; nosso bloqueio aos 95% e transição de estados exigem lógica própria. |
| Quasar | [MiningMega](https://mindustryschematics.com/schematics/6823476f4d1b558558aecacd) | Sorter escolhe recurso; usa Mega e aceita areia, carvão e titânio segundo a descrição | A descrição não estabelece seleção automática do material menos estocado nem descarte aos 95%. |
| Nova | [L-DamageControlNova](https://mindustryschematics.com/schematics/62ed2750d53a9d7c4771f59d) | Procura construções danificadas e ataca inimigos próximos usando a linha Nova | A página informa exigência de cinco Polys; não descreve pouso, evasão ou reparo próprio. |
| Flare/Quasar | [Courier v6.1](https://mindustryschematics.com/schematics/65903bd7f76a2f634dcc0459) | Alterna evasão de torres/inimigos, agressão e retorno de itens errados ao núcleo | É um transportador; usar apenas como pista para desvio e tratamento de carga. |
| Controle de estoque | [upg coreMD Sender V1.4.1](https://mindustryschematics.com/schematics/62e59210d0b3785f5486cb38), lorD | Busca dados do núcleo com uma unidade, depois a libera; reserva mínima de itens e diagnóstico por mensagem | O limiar descrito é 8%, distinto do nosso alvo de 90% da capacidade. |
| Fábrica | [Silicon on Sand](https://mindustryschematics.com/schematics/65bd93b73995a05415bc99b1) | Broca e cadinho param ao encher; fábrica modular | Receita e layout não substituem nossa condição areia + carvão + piratita e limite `mcap`. |

## Como aproveitar sem perder rastreabilidade

1. Abrir o esquema, observar a imagem e importar uma cópia no Mindustry para inspecionar links, processadores e conteúdo real. A página pública fornece título, descrição e opção de copiar/baixar, mas a descrição isolada não demonstra a implementação.
2. Comparar o programa integral com o [Mindustry Tool Logic Editor](https://mindustry-tool.com/en/tools/logic) e registrar qual trecho ou estratégia inspirou a mudança. Creditar título, autor e URL do esquema original.
3. Escrever **nosso código completo** em `controllers/<nome>/`, passar no verificador estático e testar na build V8, conforme [procedimento de validação](validation.md).
4. Registrar diferenças de unidade, versão, links, mapa e comportamento observado. Não classificar como validado um esquema que só tenha sido visto na galeria.

**Prioridade prática:** examinar primeiro `L-UnitSquadControl` e o modo de bombardeio de `Xenith v34.5` para o paredão Horizon; depois comparar o fluxo do `mono miner v1.3` com o estado de descarga do Quasar. O Mindustry Tool continua sendo nossa ferramenta de revisão do fluxo MLog; este catálogo fornece casos comunitários para estudar.


## Inspeção dos arquivos de 24/09/2026

Baixei os dois arquivos `.msch` diretamente das páginas acima e extraí **somente para análise** os códigos de seus processadores e os nomes dos links. A extração de texto e a verificação estática abaixo não equivalem a executar os esquemas no Mindustry. Os códigos integrais dos autores não foram republicados aqui.

### L-UnitSquadControl, Sphynx

- O arquivo contém **dois processadores**: o principal tem **113 instruções**, o outro escreve instruções no bloco de mensagem. O principal usa os links `arc1` e `message1`.
- Apesar da descrição genérica, a unidade configurada no código é **`@fortress`**, com `unitMax = 10`. Essa linha teria de ser modificada para outro tipo; o funcionamento com Horizon não foi demonstrado.
- A reserva de unidades usa `@flag` com um identificador calculado a partir das coordenadas do processador, evita unidades já controladas e mostra quantas foram aceitas. Essa é uma ideia útil para não disputar unidades com outro controlador.
- Quando a saúde cai abaixo de **70%**, tenta localizar reparo. Usa a mira e o disparo de `arc1` para movimentação e ataque; quando o jogador atira, as unidades se agrupam perto do ponto indicado. Não encontrei atribuição explícita de posições laterais para um paredão nem seleção automática de alvo terrestre.
- O nosso verificador estático contou as 113 instruções sem apontar salto numérico fora do programa. Isso não valida a sintaxe integral ou o comportamento.

### Xenith v34.5, Ricochet_Master

- O arquivo contém **13 códigos de processadores extraídos**, com coordenação por `cell1`, sorter, arc, switches e displays. O processador de comportamento com o modo de bombardeio tem **317 instruções**.
- O modo indicado pelo sorter com `@titanium` corresponde ao comando **7**. Nele, o código vincula **`@zenith`**, consulta a carga e tenta recolher o item escolhido no sorter do núcleo.
- Para dispersar unidades, calcula **linhas e ângulos**, aplica `sin`/`cos` e soma deslocamentos ao ponto do arc ou ao ponto de tiro. A geometria produz uma distribuição radial por fileiras; **não é o paredão alinhado** que queremos para as Horizons.
- Nesse modo há `uradar enemy any any distance ...` e `targetp` para inimigos próximos, sem filtro `ground`. Portanto, não copiar a aquisição de alvo para nossa regra de ignorar unidades aéreas. Há também localização de torre inimiga quando o arc é controlado.
- O verificador estático aceitou os 317 saltos do processador de comportamento. Em **outro** processador, o seletor de modo contém três `jump -1` associados a itens adicionais (`@thorium`, `@scrap`, `@silicon`), que nosso verificador sinaliza como fora do intervalo 0..59. Isso exige inspeção no editor do jogo antes de configurar esses itens; não interpretei o comportamento especial de `-1`.
- Não há teste nesta análise de importação no jogo, disparo de bombas, limites de distância ou compatibilidade com a build V8 da usuária.

**Aplicação ao Horizon:** estudar a reserva por flag e a contagem de unidades do primeiro esquema; usar a geometria do segundo apenas como comparação. Para atender nosso objetivo, ainda é necessário construir uma linha perpendicular ao vetor de ataque, compartilhar um alvo **terrestre** e confirmar no jogo que a Horizon cruza o ponto e solta bombas. O [Mindustry Tool Logic Editor](https://mindustry-tool.com/en/tools/logic) permanece a ferramenta de revisão visual do código que nós viermos a escrever.
