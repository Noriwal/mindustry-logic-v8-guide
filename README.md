# Guia Definitivo de Mindustry Logic (V8)

**Autor:** Manus AI

## 1. Introdução ao Mindustry Logic na V8

Mindustry Logic (MLog) é a linguagem de programação integrada ao jogo Mindustry, permitindo automação complexa e controle preciso de blocos e unidades. Com a chegada da Versão 8 (V8), o MLog recebeu atualizações significativas, especialmente no sistema de comando de unidades e na introdução dos **World Processors**, que abrem novas possibilidades para a interação com o mapa e a criação de cenários dinâmicos.

Este guia visa fornecer uma compreensão abrangente do Mindustry Logic na V8, desde os conceitos fundamentais até as funcionalidades avançadas e as melhores práticas. Seja você um iniciante ou um programador experiente, este documento o ajudará a dominar a automação no Mindustry.

## 2. Conceitos Básicos

O MLog é uma linguagem de baixo nível, inspirada em Assembly, onde cada linha de código corresponde a uma única instrução. Isso exige uma abordagem detalhada e sequencial na programação.

### 2.1. Tipos de Dados

No Mindustry Logic, você trabalhará com os seguintes tipos de dados:

*   **Inteiro (int):** Números inteiros.
*   **Ponto Flutuante (float):** Números com casas decimais.
*   **String:** Texto, como nomes de blocos (`"core"`) ou mensagens (`"Olá Mundo!"`).
*   **Booleano (bool):** Valores `true` (verdadeiro) ou `false` (falso).
*   **null:** Retornado quando uma operação não encontra um resultado (ex: `radar` não encontra um alvo).
*   **Bloco/Unidade (Object):** Referências a entidades do jogo, como uma torre ou uma unidade. Podem ser obtidos via `getlink`, `radar`, `sensor`, etc.
*   **Conteúdo (Content):** Tipos específicos de unidades, blocos, itens ou líquidos (ex: `@copper`, `@flare`).

### 2.2. Variáveis

Variáveis são usadas para armazenar valores. Elas são declaradas implicitamente ao serem usadas pela primeira vez. Exemplo: `set minhaVariavel 10`.

### 2.3. Variáveis Integradas e Constantes (@)

O Mindustry Logic fornece variáveis especiais que começam com `@`. Elas representam estados do processador, do mundo ou de unidades.

| Variável | Tipo | Descrição |
| :--- | :--- | :--- |
| `@this` | Building | O próprio bloco do processador. Útil para sensores. |
| `@thisx`, `@thisy` | Number | Coordenadas X e Y exatas do processador no mapa. |
| `@ipt` | Number | Instruções por Tick (IPT). Indica a velocidade do processador. |
| `@counter` | Number | O "Program Counter". Indica a linha atual. Alterar isso faz o código "pular". |
| `@links` | Number | Número total de blocos linkados ao processador. |
| `@unit` | Unit | A unidade atualmente vinculada via `unit bind`. |
| `@time` | Number | Timestamp UNIX atual em milissegundos. |
| `@tick` | Float | Número de ticks (1/60 seg) desde o início do mapa. |
| `@mapw`, `@maph` | Number | Largura e altura totais do mapa em blocos. |
| `@pi`, `@e` | Number | Constantes matemáticas (3.1415... e 2.7182...). |

### 2.4. Operações Matemáticas e Lógicas (op)

O comando `op` realiza cálculos. A sintaxe é: `op <operação> <resultado> <valor1> <valor2>`.

| Operação | Descrição | Exemplo |
| :--- | :--- | :--- |
| `add`, `sub`, `mul`, `div` | Operações básicas (+, -, *, /). | `op add x x 1` |
| `idiv` | Divisão inteira (descarta o resto). | `op idiv x 10 3` (x = 3) |
| `mod` | Resto da divisão (módulo). | `op mod x 10 3` (x = 1) |
| `pow` | Potenciação (valor1 elevado a valor2). | `op pow x 2 3` (x = 8) |
| `equal`, `notEqual` | Comparação de igualdade (retorna 1 ou 0). | `op equal x a b` |
| `lessThan`, `greaterThan` | Comparações de magnitude. | `op lessThan x a b` |
| `strictEqual` | Igualdade estrita (compara tipo e valor). | `op strictEqual x a b` |
| `and`, `or`, `xor` | Operações lógicas bitwise. | `op and x 1 0` (x = 0) |
| `shl`, `shr` | Bitshift (deslocamento de bits). | `op shl x 1 2` (x = 4) |
| `max`, `min` | Retorna o maior ou menor valor. | `op max x 10 20` (x = 20) |
| `abs` | Valor absoluto (sempre positivo). | `op abs x -5` (x = 5) |
| `sqrt` | Raiz quadrada. | `op sqrt x 16` (x = 4) |
| `sin`, `cos`, `tan` | Funções trigonométricas (em graus). | `op sin x 90` (x = 1) |

### 2.5. Propriedades de Sensor

O comando `sensor` permite ler estados de blocos ou unidades. Abaixo as propriedades mais comuns:

| Propriedade | Descrição | Aplicável a |
| :--- | :--- | :--- |
| `@health` | Vida atual. | Blocos e Unidades |
| `@maxHealth` | Vida máxima. | Blocos e Unidades |
| `@x`, `@y` | Coordenadas no mapa. | Blocos e Unidades |
| `@type` | Tipo do objeto (ex: `@flare`, `@core-shard`). | Blocos e Unidades |
| `@enabled` | Se o bloco está ativado (1 ou 0). | Blocos |
| `@totalItems` | Total de itens armazenados. | Blocos e Unidades |
| `@itemCapacity` | Capacidade total de itens. | Blocos e Unidades |
| `@powerNetStored` | Energia armazenada na rede elétrica. | Blocos de Energia |
| `@heat` | Calor atual (ex: reatores). | Blocos Térmicos |
| `@efficiency` | Eficiência de trabalho (0 a 1). | Fábricas |
| `@rotation` | Rotação atual (0 a 360). | Blocos e Unidades |
| `@dead` | Retorna 1 se o objeto foi destruído. | Blocos e Unidades |

### 2.6. Fluxo de Controle

Os comandos de fluxo de controle determinam a ordem de execução das instruções.

*   **`jump <linha> <condição> <valor1> <valor2>`:** Pula para uma linha específica se a condição for atendida. As condições são as mesmas das operações (ex: `equal`, `lessThan`).
*   **`end`:** Reinicia a execução do código a partir da linha 0.
*   **`stop`:** Pausa o processador.
*   **`wait <segundos>`:** Pausa a execução por um tempo. Usar `wait` em loops é uma boa prática para evitar sobrecarga.

## 3. Comandos Essenciais

Esta seção detalha os comandos mais utilizados para interagir com o ambiente do jogo.

### 3.1. Interação com Blocos e Torres

*   **`getlink <variável> <índice>`:** Obtém uma referência a um bloco linkado ao processador pelo seu índice (0 para o primeiro, 1 para o segundo, etc.).
    *   Exemplo: `getlink minhaTorre 0`
*   **`sensor <variável> <bloco> <propriedade>`:** Lê uma propriedade de um bloco e armazena o valor em uma variável.
    *   Propriedades comuns: `@health`, `@maxHealth`, `@x`, `@y`, `@rotation`, `@ammo`, `@liquid`, `@power`, `@enabled`, `@type`.
    *   Exemplo: `sensor vidaTorre minhaTorre @health`
*   **`control <bloco> <comando> <valor1> <valor2> <valor3> <valor4>`:** Controla um bloco, alterando suas propriedades ou executando ações.
    *   **`shoot <x> <y> <ativar>`:** Faz uma torre atirar nas coordenadas `x`, `y`. `ativar` é 1 para atirar, 0 para parar.
        *   Exemplo: `control minhaTorre shoot 100 200 1 0`
    *   **`shootp <alvo> <ativar>`:** Faz uma torre atirar em um alvo (unidade/bloco) com previsão de movimento.
        *   Exemplo: `control minhaTorre shootp meuAlvo 1 0`
    *   **`enabled <estado>`:** Ativa (1) ou desativa (0) um bloco.
        *   Exemplo: `control meuConveyor enabled 0 0 0 0`
    *   **`config <valor>`:** Configura um bloco (ex: tipo de item para um descarregador).
        *   Exemplo: `control meuDescarregador config @copper 0 0 0`
*   **`radar <filtro1> <filtro2> <filtro3> <ordem> <tipoOrdem> <variável>`:** Detecta unidades ou blocos inimigos/aliados/neutros dentro do alcance de um bloco (geralmente uma torre) e armazena a referência do alvo em uma variável.
    *   Filtros: `enemy`, `ally`, `neutral`, `any`, `attacker`, `flying`, `boss`, `ground`.
    *   Ordem: `distance`, `health`, `shield`, `armor`, `maxHealth`.
    *   Tipo de Ordem: `1` para maior/mais próximo, `0` para menor/mais distante.
    *   Exemplo: `radar enemy any any health 1 meuAlvo` (encontra o inimigo com mais vida).

### 3.2. Saída para Displays e Mensagens

*   **`print <valor>`:** Adiciona texto a um buffer interno do processador.
*   **`printflush <blocoMensagem>`:** Envia o conteúdo do buffer de texto para um bloco de mensagem linkado e limpa o buffer.
    *   Exemplo: `print 
```mlog
print "Recursos: "
print meuRecurso
printflush message1
```

### 3.3. Comandos de Desenho para Displays Gráficos

Os comandos `draw` são usados para criar gráficos em Logic Displays. Lembre-se de que, após uma série de comandos `draw`, você deve usar `drawflush <display>` para renderizar as alterações na tela.

*   **`draw clear <r> <g> <b> <a>`:** Limpa o display com uma cor específica (RGBA, valores de 0 a 255). O `a` (alpha) é opcional.
    *   Exemplo: `draw clear 0 0 0 255` (limpa com preto opaco).
*   **`draw color <r> <g> <b> <a>`:** Define a cor atual para os próximos comandos de desenho.
    *   Exemplo: `draw color 255 0 0 255` (define a cor para vermelho opaco).
*   **`draw stroke <espessura>`:** Define a espessura da linha para os próximos comandos de desenho.
    *   Exemplo: `draw stroke 2`
*   **`draw line <x1> <y1> <x2> <y2>`:** Desenha uma linha entre dois pontos.
    *   Exemplo: `draw line 0 0 80 80`
*   **`draw rect <x> <y> <largura> <altura>`:** Desenha um retângulo preenchido.
    *   Exemplo: `draw rect 10 10 20 20`
*   **`draw poly <x> <y> <lados> <raio> <rotação>`:** Desenha um polígono preenchido.
    *   Exemplo: `draw poly 40 40 3 15 0` (triângulo no centro).
*   **`draw circle <x> <y> <raio>`:** Desenha um círculo preenchido.
    *   Exemplo: `draw circle 40 40 10`
*   **`draw triangle <x1> <y1> <x2> <y2> <x3> <y3>`:** Desenha um triângulo preenchido.
    *   Exemplo: `draw triangle 10 10 20 30 30 10`
*   **`draw image <x> <y> <imagem> <tamanho> <rotação> <opcional>`:** Desenha um ícone ou imagem no display. `<imagem>` é geralmente um `@` seguido do nome do tipo de unidade/bloco (ex: `@flare`, `@core`).
    *   Exemplo: `draw image 40 40 @flare 16 0 0`
*   **`drawflush <display>`:** Renderiza todos os comandos `draw` acumulados no `display` linkado.

## 4. Controle de Unidades (Novidades da V8)

A V8 trouxe um sistema de comando de unidades renovado, oferecendo maior flexibilidade e controle sobre o comportamento das suas unidades.

### 4.1. Comandos Básicos de Unidade

*   **`unit bind <tipoUnidade>`:** Vincula o processador a uma unidade do tipo especificado. A unidade vinculada se torna o alvo para comandos subsequentes. A variável `@unit` referencia a unidade atualmente vinculada.
    *   Exemplo: `unit bind @mono`
*   **`unit control <comando> <parâmetros...>`:** Envia comandos para a unidade vinculada.
    *   **`idle`:** A unidade não faz nada, mantém sua posição.
    *   **`stop`:** A unidade para todas as ações (movimento, construção, mineração).
    *   **`move <x> <y>`:** Move a unidade para as coordenadas `x`, `y`.
    *   **`approach <x> <y> <raio>`:** Move a unidade para as coordenadas `x`, `y` dentro de um `raio` de tolerância.
    *   **`boost <ativar>`:** Ativa (1) ou desativa (0) o boost da unidade (se aplicável).
    *   **`target <x> <y> <ativar>`:** Faz a unidade atirar nas coordenadas `x`, `y`. `ativar` é 1 para atirar, 0 para parar.
    *   **`targetp <alvo> <ativar>`:** Faz a unidade atirar em um `alvo` (unidade/bloco) com previsão de movimento.
    *   **`mine <x> <y>`:** Faz a unidade minerar no bloco em `x`, `y`.
    *   **`build <x> <y> <bloco> <rotação> <config>`:** Faz a unidade construir um `bloco` nas coordenadas `x`, `y` com `rotação` e `config` (opcional).
    *   **`flag <valor>`:** Define uma flag numérica para a unidade, visível na informação da unidade.
    *   **`getblock <variável> <x> <y>`:** Obtém informações sobre o bloco nas coordenadas `x`, `y` e armazena na `variável`.
    *   **`within <x> <y> <raio>`:** Retorna `true` se a unidade estiver dentro do `raio` das coordenadas `x`, `y`.
    *   **`unbind`:** Desvincula a unidade do processador, retornando-a ao controle da IA padrão.
*   **`unit radar <filtro1> <filtro2> <filtro3> <ordem> <tipoOrdem> <variável>`:** Similar ao `radar` de blocos, mas detecta unidades em relação à unidade vinculada.
*   **`unit locate <tipo> <time> <saídaX> <saídaY> <encontrado>`:** Localiza estruturas ou recursos específicos no mapa.
    *   Tipos: `ore`, `building`, `spawn`, `damaged`.
    *   Time: `core`, `storage`, `generator`, `turret`, `factory`, `repair`, `rally`, `reactor`.
    *   Exemplo: `unit locate ore @copper saidaX saidaY encontrado` (encontra o minério de cobre mais próximo).

## 5. World Processors (V8)

Os World Processors são uma das maiores adições da V8, permitindo que você interaja diretamente com o mapa e crie eventos dinâmicos. Eles são indestrutíveis e possuem comandos exclusivos.

### 5.1. Comandos Exclusivos do World Processor

*   **`getblock <variável> <x> <y> <camada>`:** Obtém informações detalhadas sobre um bloco em uma posição específica do mundo, incluindo sua `camada` (ex: `0` para blocos de chão, `1` para construções).
    *   Exemplo: `getblock tipoBloco 100 150 1`
*   **`setblock <x> <y> <bloco> <camada> <rotação> <config>`:** Altera um bloco em uma posição específica do mundo. Permite construir, destruir ou modificar blocos programaticamente.
    *   Exemplo: `setblock 100 150 @thorium-reactor 1 0 0` (constrói um reator de tório).
*   **`spawnunit <tipoUnidade> <equipe> <x> <y> <rotação>`:** Gera uma unidade de um `tipoUnidade` específico para uma `equipe` nas coordenadas `x`, `y` com uma `rotação`.
    *   Exemplo: `spawnunit @dagger @enemy 200 200 0`
*   **`spawnwave <númeroOnda> <intervalo>`:** Força o surgimento de uma onda de inimigos. `númeroOnda` é o índice da onda, `intervalo` é o tempo até a próxima onda.
    *   Exemplo: `spawnwave 5 60`
*   **`applystatus <status> <unidade> <duração>`:** Aplica um `status` (ex: `burning`, `freezing`, `unmoving`) a uma `unidade` por uma `duração`.
    *   Exemplo: `applystatus burning meuAlvo 300`
*   **`explosion <x> <y> <dano> <raio> <incêndio> <push> <ignorarEquipe>`:** Cria uma explosão nas coordenadas `x`, `y` com `dano`, `raio`, `incêndio` (chance de incendiar), `push` (força de empurrão) e `ignorarEquipe` (se a explosão afeta a própria equipe).
    *   Exemplo: `explosion 100 100 50 30 0.5 10 0`
*   **`cutscene <x> <y> <zoom> <duração>`:** Inicia uma cutscene focando nas coordenadas `x`, `y` com um `zoom` e `duração`.
    *   Exemplo: `cutscene 100 100 2 300`

## 6. Lógica Avançada e Boas Práticas

### 6.1. Otimização de Código

*   **Minimizar `jump`s:** Jumps consomem ciclos. Estruture seu código para ter o mínimo de jumps possível.
*   **Reutilizar variáveis:** Evite criar variáveis desnecessárias. Reutilize-as quando possível.
*   **Processadores dedicados:** Para tarefas complexas (ex: controle de unidades, displays gráficos), use processadores dedicados. Isso melhora a performance e a legibilidade.
*   **Comentários:** Use `#` para adicionar comentários e explicar partes complexas do seu código.

### 6.2. Gerenciamento de Múltiplas Unidades

Com a V8, o controle de unidades se tornou mais robusto. Você pode iterar sobre unidades vinculadas ou usar `unit locate` para encontrar unidades específicas e emitir comandos.

### 6.3. Interação com o Ambiente (World Processor)

Os World Processors permitem criar defesas dinâmicas, armadilhas, ou até mesmo alterar o terreno em tempo real. Explore `setblock` para construir barreiras temporárias ou `explosion` para limpar áreas.

## 7. Exemplos Práticos

### 7.1. Torre de Defesa com Display de Alvo

```mlog
# Linkar a torre e o display
getlink minhaTorre 0
getlink meuDisplay 1

loop:
    # Radar para encontrar o inimigo mais próximo com mais vida
    radar enemy any any maxHealth minhaTorre 1 alvo

    # Se houver um alvo, atira e exibe no display
    jump noTarget equal alvo null

    # Atirar no alvo
    sensor alvoX alvo @x
    sensor alvoY alvo @y
    control minhaTorre shoot alvoX alvoY 1 0

    # Exibir tipo de alvo no display
    sensor tipoAlvo alvo @type
    draw clear 0 0 0 255 0 0 # Limpa o display com preto
    draw color 255 255 255 255 # Define a cor para branco
    draw image 40 40 tipoAlvo 32 0 0 # Desenha o ícone do alvo no centro
    drawflush meuDisplay

    jump loop

noTarget:
    # Se não houver alvo, para de atirar e limpa o display
    control minhaTorre shoot 0 0 0 0
    draw clear 0 0 0 255 0 0 # Limpa o display com preto
    drawflush meuDisplay

    jump loop
```

### 7.2. Mineração Automatizada com Unidades

```mlog
# Linkar o core e o ponto de mineração (ex: um bloco de minério)
getlink meuCore 0
set minerioX 100 # Coordenada X do minério
set minerioY 150 # Coordenada Y do minério

loop:
    # Vincular uma unidade de mineração (ex: @mono)
    unit bind @mono

    # Se não houver unidade vinculada, tenta novamente
    jump loop equal @unit null

    # Mover para o ponto de mineração
    unit control move minerioX minerioY

    # Esperar a unidade chegar perto do minério
    set chegouMinerio unit control within minerioX minerioY 5
    jump loop equal chegouMinerio 0

    # Minerar
    unit control mine minerioX minerioY

    # Esperar a unidade encher o inventário (simplificado, na prática precisaria de sensor @itemCapacity)
    wait 5 # Espera 5 segundos para simular a mineração

    # Mover para o core para descarregar
    sensor coreX meuCore @x
    sensor coreY meuCore @y
    unit control move coreX coreY

    # Esperar a unidade chegar perto do core
    set chegouCore unit control within coreX coreY 5
    jump loop equal chegouCore 0

    # Descarregar itens no core
    unit control itemDrop meuCore 0 0 0 # Descarrega todos os itens

    jump loop
```

## 8. Referências

*   [Mindustry Unofficial Wiki - Version 8.0](https://mindustry-unofficial.fandom.com/wiki/Version_8.0)
*   [Mindustry Logic Manual Oficial (Incompleto)](https://mindustrygame.github.io/wiki/logic/0-introduction/)
*   [Mlog Documentation (yrueii.github.io)](https://yrueii.github.io/MlogDocs/)
