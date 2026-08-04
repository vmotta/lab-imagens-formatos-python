# Guia do professor

## Preparação anterior à aula

1. Abra o notebook pelo botão do Colab no `README.md`.
2. Execute todas as células para confirmar que o acesso ao GitHub está funcionando.
3. Defina se a entrega será por Pull Request ou por Issue.
4. Compartilhe o repositório antes da aula.
5. Recomende aos estudantes que façam login no Google e no GitHub.

O notebook gera imagens sintéticas reproduzíveis. Portanto, não é necessário distribuir fotografias separadamente.

## Cronograma de 50 minutos

| Tempo | Atividade | Mediação sugerida |
|---:|---|---|
| 0–5 min | Abertura, cópia do notebook e configuração | Reforce que tamanho do arquivo, dimensões e qualidade são conceitos diferentes. |
| 5–10 min | Geração e inspeção das imagens | Peça que localizem o modo `RGB` e o modo `RGBA`. |
| 10–25 min | Conversão e medição de formatos | Compare fotografia e captura de tela; o comportamento pode mudar conforme o conteúdo. |
| 25–35 min | JPEG, recortes, MSE e PSNR | Destaque artefatos em blocos e o compromisso entre tamanho e fidelidade. |
| 35–42 min | Canal alpha e conversão para JPEG | Mostre que o JPEG exige composição sobre um fundo. |
| 42–47 min | SVG em dois tamanhos | Relacione formas geométricas com escalabilidade. |
| 47–50 min | Matriz de decisão e conclusão | Solicite justificativas baseadas nos resultados produzidos. |

## Evidências esperadas

Sem impor um resultado numérico único, espera-se que os estudantes observem:

- JPEG com qualidade menor produz arquivo menor e tende a reduzir PSNR;
- fotografias podem ficar menores em JPEG ou WebP com perda;
- PNG preserva detalhes e costuma funcionar bem em telas com texto;
- PNG e WebP podem preservar canal alpha;
- JPEG não armazena transparência;
- TIFF com LZW preserva os pixels, mas pode ocupar mais espaço;
- SVG mantém bordas nítidas em ampliações porque descreve formas, não uma grade fixa;
- uma imagem de dimensões maiores não é automaticamente melhor.

Os tamanhos exatos variam conforme a versão das bibliotecas e o conteúdo da imagem. Avalie a interpretação, não a coincidência de números.

## Intervenções para dificuldades comuns

### O notebook não consegue baixar os arquivos do GitHub

Peça que o estudante execute novamente a célula de configuração. Como alternativa, faça upload manual dos arquivos `src/image_utils.py` e `src/gerar_imagens_exemplo.py`.

### WebP não é reconhecido

No Colab, o Pillow normalmente inclui suporte a WebP. Em ambiente local, atualize o Pillow ou instale uma compilação com suporte à biblioteca WebP.

### O JPEG apresenta fundo preto

A conversão direta de RGBA para RGB pode descartar a interpretação visual do alpha. O laboratório usa `ensure_rgb`, que compõe a imagem sobre fundo branco.

### O PSNR é infinito

Isso ocorre quando as duas imagens comparadas são idênticas e o erro quadrático médio é zero.

## Fechamento recomendado

Solicite que duas duplas defendam escolhas diferentes para fotografia web. A discussão deve considerar qualidade, peso, compatibilidade e finalidade, em vez de buscar um formato universal.
