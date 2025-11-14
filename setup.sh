#!/usr/bin/env bash
set -e
CMD=${1:-up}
if [ "$CMD" = "up" ]; then
  docker-compose up -d
  echo "Aguarde 30-60s para SonarQube e Jenkins inicializarem."
  echo "Jenkins: http://localhost:8080"
  echo "SonarQube: http://localhost:9000"
elif [ "$CMD" = "down" ]; then
  docker-compose down
else
  echo "Uso: ./setup.sh [up|down]"
fi
