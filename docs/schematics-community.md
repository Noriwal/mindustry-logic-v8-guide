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
