#!/bin/bash
set -e

# Retry loop
until flyway -url=jdbc:postgresql://postgres:5432/mm_db -user=postgres -password=password -locations=filesystem:/flyway/sql migrate; do
  echo "Waiting for PostgreSQL to be ready..."
  sleep 5
done