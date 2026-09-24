# Como validar um controlador

O status de cada código começa como **experimental**. Só marque **testado na V8** depois de observar a execução no jogo. O [Mindustry Tool Logic Editor](https://mindustry-tool.com/en/tools/logic) é a referência visual para importar e inspecionar o fluxo; o [manual de lógica do Mindustry](https://mindustrygame.github.io/wiki/logic/0-introduction/) ajuda a conferir sintaxe. Importar no editor não simula unidades nem confirma o resultado em combate.

1. Guarde o programa integral em `controllers/<nome>/<nome>.mlog`, sem números de linha impressos, marcadores Markdown nem trechos omitidos. Cada linha de instrução corresponde ao índice de salto iniciado em zero.
2. Execute `python3 tools/check_mlog.py controllers/<nome>/<nome>.mlog`. O verificador confere destinos numéricos de `jump`, formato de alguns comandos e sinais de pseudocódigo. Avisos de salto dinâmico requerem revisão manual.
3. Importe uma cópia no **Mindustry Tool Logic Editor**. Confira o grafo de saltos, a ordem dos parâmetros e a leitura de variáveis. Não publique conteúdo pessoal nem presuma que o workspace do navegador é backup do GitHub.
4. Cole o programa inteiro num processador da build V8 usada, com os links e o mapa descritos na ficha. Observe cada estado, inclusive quando não há alvo, quando o alvo morre, quando o núcleo muda e quando uma unidade é destruída.
5. Anote o resultado real em `controllers/<nome>/README.md`: build, links em ordem, mapa, número de unidades, casos testados, falhas conhecidas e data. Se houver schematic reproduzível, inclua o arquivo e seu modo de importação; não apresente apenas uma imagem como teste.

O script estático **não interpreta a semântica de MLog**, não verifica tipo de alvo, tempo de instruções por tick, alcance do radar, receitas, física do voo ou limites específicos da build. O teste dentro do jogo decide se o código funciona.

## Critérios para aceitar a próxima versão do Horizon

- Uma única Horizon encontra uma unidade terrestre; as demais recebem o mesmo objetivo.
- Um alvo aéreo isolado não inicia o bombardeio.
- As unidades aproximam-se numa linha estreita, mantêm espaçamento e passam sobre o alvo para soltar bombas.
- Após alvo morto, fora do radar ou sem alvo, a formação não gira indefinidamente nem mantém disparo em coordenadas antigas.
- O comportamento se recupera da destruição de uma Horizon e de uma reinicialização do processador.

Até que o código integral utilizado em jogo esteja no repositório e passe por esses cenários, o controlador Horizon permanece **pendente de validação**.
