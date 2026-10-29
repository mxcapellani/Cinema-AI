# Cinema AI™ — Skill
Prompts para animar imagens estáticas com movimentos sutis, naturais e cinematográficos. Interação em português brasileiro; duas opções em inglês, cada uma com tradução fiel PT-BR.

## Comportamento
Pergunta inicial automático/manual uma vez por fluxo. Com câmera já definida, prossegue diretamente. Automático escolhe duas opções adequadas; manual respeita um movimento com duas variações, ou dois movimentos com uma opção para cada. Quantidade explicitamente solicitada prevalece. Analisa profundidade, luz, pose e áreas estáveis; preserva identidade, roupa, materiais e estilo. Não usa os qualificadores epic, masterpiece ou HD.
O pacote inclui todos os prompts A–E fornecidos, os dois catálogos e os exemplos originais, além de três exemplos completos novos. [Fonte integral](docs/SOURCE_SPECIFICATION.md).

## Instalação e uso
Copiar `.agents/skills/cinema-ai` para a mesma estrutura no projeto. Host deve reconhecer Agent Skills ou carregar [SKILL.md](.agents/skills/cinema-ai/SKILL.md) explicitamente. Nenhuma instalação de serviço ou chave é exigida para escrever prompts.
Pedido: “Use câmera automática nesta imagem”. Ou “Faça um tracking suave para a direita e preserve o produto”. Sem imagem acessível, fornecer descrição detalhada; a Skill não alegará inspeção visual. [Instalação e atualização](docs/INSTALLATION.md).

## Dependências e limites
Modelo de linguagem para texto; visão para leitura de imagem. A Skill não gera vídeos nem integra automaticamente Kling, Luma, Runway, Pika ou Higgsfield. São plataformas de referência da fonte; suporte e sintaxe atuais não foram verificados. Movimento pode exigir regiões não visíveis; evitar extrapolação de conteúdo e grandes órbitas sem suporte.
A especificação distingue comportamento atribuído ao agente de implementações propostas. Catálogo privado de movimentos ousados não foi fornecido e não foi reconstruído como se estivesse disponível. [Auditoria](docs/AUDIT.md).

## Testes
```bash
python -m pip install -r tests/requirements.txt
python tests/validate_skill.py
python -m unittest discover -s tests -p 'test_*.py'
```
Validação estrutural verifica YAML, links, integridade dos prompts A–E, formatos dos exemplos e termos proibidos. Não comprova fidelidade semântica EN/PT, visão ou qualidade de vídeo. [Aceitação](tests/acceptance-tests.md), [comparação](tests/comparison-matrix.md), [resultados](tests/RESULTS.md). Actions configurado.

MIT para o pacote produzido. Nome Cinema AI™ preservado da especificação, sem alegação de titularidade da marca, endosso ou acesso a configurações internas. [Histórico](CHANGELOG.md).
