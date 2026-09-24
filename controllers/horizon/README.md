# Horizon: onda de bombardeiros

**Estado:** especificação registrada; código integral em uso ainda não foi recuperado para o GitHub. Não há `.mlog` testado nesta pasta.

## Requisitos observados na conversa

- Um processador coordena todas as Horizons. Quando qualquer uma detecta um alvo terrestre válido, as demais devem avançar.
- Ignorar alvos aéreos. Evitar alterações de rota por detecções isoladas ou alvos inválidos.
- Aproximar em um paredão alinhado e fechado, mantendo separação suficiente para não atrapalhar o bombardeio.
- Passar por cima do alvo, porque a Horizon lança bombas sobre a área abaixo dela.

Trecho inicial fornecido pelo usuário, apenas como histórico (incompleto; **não colar como programa final**):

```mlog
ubind @horizon
ucontrol approach ux uy 25 0 0
uradar enemy any any distance 0 1 alvo
sensor ax alvo @x
sensor ay alvo @y
sensor ux @unit @x
sensor uy @unit @y
sensor rng @unit @range
ucontrol target ax ay 1 0 0
```

## Plano de implementação

1. Resolver alvo terrestre, tempo de validade e atualização partilhada. Documentar como uma unidade transmite o alvo às outras, por exemplo via `cell1`; confirmar que todos os leitores e escritores usam os mesmos índices.
2. Atribuir uma posição estável por unidade e calcular deslocamentos laterais em relação ao vetor de aproximação. Prever reatribuição se alguma unidade morrer.
3. Definir fases de reunião, aproximação, passagem sobre o alvo e saída; confirmar no jogo o raio e os comandos de ataque que realmente disparam as bombas.
4. Tratar alvo ausente, aéreo ou morto. Não usar `sensor` em alvo nulo sem uma verificação prévia.
5. Versionar o **programa inteiro** e executar os cenários de [validação](../../docs/validation.md). Registrar build V8, processador, ordem de links, número de Horizons e resultados nesta ficha.

O [Mindustry Tool Logic Editor](https://mindustry-tool.com/en/tools/logic) ajuda a desenhar e revisar essas transições. O comportamento aéreo e o bombardeio dependem de teste no jogo.
