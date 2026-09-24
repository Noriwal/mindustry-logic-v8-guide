# Mindustry Tool: referência para o projeto de lógica V8

Consulta em 24/09/2026. Este documento registra o que foi observado no [Mindustry Tool](https://mindustry-tool.com/en/tools/logic) e como aproveitar o site nos controladores do projeto. É um índice comentado, não uma cópia do manual nem uma garantia de compatibilidade com cada build do jogo.

## Logic Editor: teste direto

1. A página pediu criar um *workspace*. Criei um workspace de teste e abri o editor visual.
2. Em **Edit → Import**, há **Copy from clipboard** e **Import sample**. O exemplo importado gerou um fluxo visual numerado de 0 a 44 com `ubind`, `sensor`, `jump`, `ulocate`, `uradar`, `ucontrol`, `set`, `op` e `end`.
3. A paleta oferece também `read`, `write`, `getlink`, `control`, `radar`, `select`, `lookup`, `print`, `printflush`, desenho e outras instruções. Há busca de instruções, operações de desfazer/refazer, alinhamento e menu de workspaces.
4. **Global variables** mostra, entre outras, `@ipt`, `@links`, `@mapw`, `@maph`, `@this`, `@thisx`, `@thisy`, `@tick`, `@time` e `@unit`. A interface também permite adicionar variáveis personalizadas.
5. O exemplo visual não é uma simulação do combate, mineração ou fábrica. O editor ajuda a montar e inspecionar fluxo e saltos; comportamento, vínculos e compatibilidade V8 precisam ser conferidos no jogo. Não testei exportação nem persistência remota.

### Fluxo sugerido para nossos scripts

- Guardar aqui o **código MLog integral**, com linhas numeradas a partir de 0 quando houver revisão de `jump`.
- Colar uma cópia no editor para inspecionar instruções, parâmetros e caminhos visuais. Usar um workspace por controlador (Horizon, Flare, Nova, Quasar, fábricas).
- Testar no Mindustry com os blocos e unidades realmente disponíveis. Registrar build, links, mapa e resultado. Não chamar um script de validado apenas porque foi importado.
- Após cada alteração, entregar novamente **o código completo pronto para colar**.

## Referências úteis do próprio site

| Fonte | Uso no projeto | Cuidado |
| --- | --- | --- |
| [Introdução à lógica](https://mindustry-tool.com/ru/posts/0199080c-bffc-7721-9392-777e6e3a0c20) | Visão geral de MLog, blocos, unidades, memória e mensagens | O texto se descreve como manual incompleto; confirmar detalhes da V8 no jogo. |
| [Blocos de lógica](https://mindustry-tool.com/ua/posts/0199081d-82ca-7962-a367-3f0989ffa5d1) | `print`/`printflush`, switch, displays e memória: célula 64 posições (0–63), banco 512 | Útil para nossa `cell1` e depuração; verificar limites na build usada. |
| [Exemplos simples](https://mindustry-tool.com/cn/posts/01990d1b-da84-7cf2-918c-0eebb1bd50ff) | Exemplo de varredura com `getlink`, `@links`, `sensor @type`, `control enabled` | Adaptar para nossos links e critérios de produção. |
| [World Logic](https://mindustry-tool.com/de/posts/01991289-4bc4-7df2-b437-46077106f508) | `fetch`, flags globais e recursos do **world processor** no editor de mapas | Não presumir que instruções do world processor funcionem em processadores comuns. |
| [Galeria de schematics](https://mindustry-tool.com/en/schematics) | Encontrar montagens e exemplos comunitários de lógica | Um schematic publicado não comprova correção ou versão. |
| [Ferramentas](https://mindustry-tool.com/en/tools) | Calculadora de proporção, gerador de logic display, sorter e mapa | Utilidade distinta do Logic Editor; não validar MLog por inferência. |
| [API pública documentada](https://api.mindustry-tool.com/api/v4/api-docs) | Consultar endpoints de schematics e lógica, caso futuramente seja necessária integração | Endpoints de `@me`/criação podem exigir autenticação; nenhuma integração foi implementada. |

## Pontos aplicáveis aos controladores atuais

- **Horizon:** usar o editor para visualizar seleção de alvo terrestre, estados da onda e saltos da formação; verificar no jogo o timing do bombardeio e a sincronização entre unidades.
- **Flare e Nova:** separar no fluxo visual patrulha/combate/reparo; verificar `uradar`, `ulocate`, `@range`, flags e `ucontrol` na unidade real.
- **Quasar:** inspecionar a transição entre mineração, retorno, descarga e troca de item; observar no jogo `@totalItems`, `@itemCapacity` e a distância necessária para descarregar.
- **Fábricas/desmontadores:** acompanhar `getlink` e `@links`, índice inicial 0, seleção de item, `mcap = 90%` da capacidade do núcleo e condições de matéria-prima. Confirmar no jogo sensores e receitas.

## Qual fonte prevalece

Para sintaxe e semântica de MLog, consultar também o [manual de lógica do Mindustry](https://mindustrygame.github.io/wiki/logic/0-introduction/), especialmente [edição visual e manual](https://mindustrygame.github.io/wiki/logic/2-editing/), [variáveis](https://mindustrygame.github.io/wiki/logic/3-variables/) e [glossário](https://mindustrygame.github.io/wiki/logic/1-glossary/). A fonte decisiva para o nosso trabalho é a **build V8 instalada e o teste dentro do jogo**.

**Atenção ao README atual deste repositório:** ele contém pseudocódigo com rótulos como `loop:`, chamadas escritas como `unit bind`/`unit control`, exemplos de `radar` e `jump` que precisam de revisão de ordem/argumentos, e comentários embutidos. Portanto, não colar seus exemplos diretamente no processador sem converter e conferir instrução por instrução. O Logic Editor é uma ferramenta de apoio para essa revisão, não um certificado automático de execução.
