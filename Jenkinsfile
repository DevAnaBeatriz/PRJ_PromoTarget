pipeline {
  agent { docker { image 'python:3.10' } }

  environment {
    SONAR_TOKEN = credentials('sonar-token')
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install') {
      steps {
        sh 'python -m pip install --upgrade pip'
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Test & Coverage') {
      steps {
        sh 'pytest --junitxml=reports/junit.xml --cov=src --cov-report=xml:coverage.xml || true'
      }
      post {
        always {
          junit 'reports/junit.xml'
          archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
        }
      }
    }

    stage('SonarQube Analysis') {
      steps {
        // Baixa e executa SonarScanner CLI (versão especificada)
        sh '''
        set -e
        SCANNER_VERSION=4.8.0.2856
        if [ ! -d sonar-scanner-$SCANNER_VERSION ] ; then
          wget -q https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-$SCANNER_VERSION-linux.zip -O /tmp/sonar-scanner.zip
          apt-get update -y && apt-get install -y unzip
          unzip -q /tmp/sonar-scanner.zip -d /
          mv /sonar-scanner-$SCANNER_VERSION /opt/sonar-scanner
        fi
        export PATH=/opt/sonar-scanner/bin:$PATH
        sonar-scanner -Dsonar.projectKey=PRJ_PromoTarget -Dsonar.sources=src -Dsonar.python.coverage.reportPaths=coverage.xml -Dsonar.host.url=http://sonarqube:9000 -Dsonar.login=$SONAR_TOKEN || true
        '''
      }
    }

    stage('Quality Gate') {
      steps {
        timeout(time: 2, unit: 'MINUTES') {
          waitForQualityGate abortPipeline: true
        }
      }
    }

    stage('Package/Archive') {
      steps {
        sh 'tar -czf artifact.tar.gz src requirements.txt README.md || true'
        archiveArtifacts artifacts: 'artifact.tar.gz', allowEmptyArchive: true
      }
    }
  }

  post {
    success { echo 'Pipeline concluída com sucesso.' }
    failure { echo 'Pipeline falhou.' }
  }
}
