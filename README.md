# Projeto de Observabilidade

## Integrantes
- Antônio Lisarb Cordeiro Saraiva
- Karyna Rodrigues de Sousa

## Descrição
Este projeto tem como objetivo criar uma API simples que expõe métricas para Prometheus e visualizá-las no Grafana.

## Estrutura do Projeto
- **api/**: contém a API desenvolvida.
- **prometheus/**: contém a configuração do Prometheus.
- **docker-compose.yml**: orquestra os serviços.
- **README.md**: informações sobre o projeto.

## Como Executar
1. Navegue até o diretório do projeto.
2. Execute `docker-compose up` para iniciar os serviços.
3. Acesse a API em `http://localhost:5000`.
4. Acesse o Prometheus em `http://localhost:9090`.
5. Acesse o Grafana em `http://localhost:3000` (usuário: admin, senha: admin).

## Observações
- Certifique-se de ter o Docker e o Docker Compose instalados.