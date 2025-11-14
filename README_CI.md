# CI adjustments added automatically

Arquivos adicionados:
- Jenkinsfile
- sonar-project.properties
- docker-compose.ci.yml
- tests/ (com testes básicos)
- requirements.txt (atualizado com pytest & pytest-cov)

Como usar localmente (Docker):
1. Copie este projeto para um repositório (Git) e configure no Jenkins.
2. Suba os serviços de CI (opcionalmente):
   docker-compose -f docker-compose.ci.yml up -d
3. Configure no Jenkins:
   - Instale plugins: Pipeline, SonarQube Scanner, JUnit, etc.
   - Adicione uma credencial "Secret text" com id 'sonar-token' contendo seu token Sonar.
   - Crie um Pipeline (multibranch ou simples) apontando para este repositório.
4. O Jenkins rodará as etapas:
   - Instalar dependências
   - Executar pytest e gerar coverage.xml
   - Executar SonarScanner CLI (baixa automaticamente durante o job)
   - Esperar Quality Gate
