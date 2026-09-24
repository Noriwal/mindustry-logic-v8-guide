# Biblioteca Mindustry Logic V8

Repositório para organizar os controladores MLog, registrar como foram testados e manter o **código integral pronto para colar** no Mindustry. O projeto começou como um guia de conceitos; o texto original permanece em [Guia histórico](docs/legacy-guide.md) para consulta e revisão. Seus exemplos são pseudocódigo e não têm status de programas testados.

## Comece por aqui

- [Controladores e estado de cada programa](controllers/README.md)
- [Procedimento de validação](docs/validation.md)
- [Mindustry Tool Logic Editor e outras referências do site](docs/mindustry-tool.md)
- [Guia histórico, ainda não auditado](docs/legacy-guide.md)

O [Mindustry Tool Logic Editor](https://mindustry-tool.com/en/tools/logic) é parte do nosso fluxo: importar uma cópia do código, visualizar os saltos e conferir parâmetros. Agradecemos ao **Mindustry Tool** por disponibilizar o editor e o conteúdo de referência. A importação não substitui o teste no jogo; as referências do site e o [manual de lógica do Mindustry](https://mindustrygame.github.io/wiki/logic/0-introduction/) devem ser conferidos contra a build V8 utilizada.

## Verificação rápida

```bash
python3 tools/check_mlog.py controllers/horizon/horizon.mlog
python3 -m unittest discover -s tests
```

O primeiro comando passa a valer quando o programa Horizon completo for incluído. Ele detecta alguns erros estruturais, como `jump` para linha inexistente; não afirma que o código executa corretamente no Mindustry. A numeração de `jump` começa em **zero**. Qualquer correção deve entregar novamente o arquivo `.mlog` completo.

## Próxima versão

O [Horizon](controllers/horizon/README.md) é o primeiro caso: uma onda coordenada que ignora alvos aéreos e passa sobre um alvo terrestre em formação. A ficha registra os requisitos e casos de teste. O código integral da última versão que rodou no jogo ainda não está neste repositório; não atribuí status de testado a um programa reconstruído a partir de um trecho de conversa.
