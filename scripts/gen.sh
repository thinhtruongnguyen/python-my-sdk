#!/bin/bash
set -e

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
JAR="$BASE_DIR/scripts/openapi-generator-cli.jar"

SPEC_DIR="$BASE_DIR/specs"
RAW="$SPEC_DIR/doc.json"
FILTERED="$SPEC_DIR/doc_filtered.json"

OUT="$BASE_DIR"
LANGS=("go")

# 1. Download spec
bash "$BASE_DIR/scripts/download_spec.sh" || exit 1

# 2. Filter schema
python3 "$BASE_DIR/scripts/extract_schemas.py" "$RAW" "$FILTERED" || exit 1

# 3. Generate python client
rm -rf "$BASE_DIR/python-client"

java -jar "$JAR" generate \
  -i "$FILTERED" \
  -g python \
  -o "$BASE_DIR/python-openapi-generator-cli" \
  --package-name aioz_api_client \
  --additional-properties=packageVersion=1.0.0,projectName=AIOZApiClient,generateSourceCodeOnly=true

# 4. Create setup.py for pip install
cat > "$BASE_DIR/python-openapi-generator-cli/setup.py" << 'EOF'
from setuptools import setup, find_packages

setup(
    name="aioz_api_client",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
)
EOF

echo "✅ setup.py created in python-openapi-generator-cli"

# 5. (Optional) Install in editable mode
pip install -e "$BASE_DIR/python-openapi-generator-cli"
echo "✅ Installed aioz_api_client in editable mode"
