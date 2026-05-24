#!/usr/bin/env bash
# Fetch LFS-tracked model (bash)
MODEL_PATH=${1:-injex/transformer/model/model.safetensors}

command -v git >/dev/null 2>&1 || { echo "git is not installed or not on PATH." >&2; exit 1; }

echo "Initializing Git LFS..."
git lfs install --local

echo "Fetching refs and switching to main..."
git fetch --all
git checkout main

echo "Pulling LFS object: $MODEL_PATH"
git lfs pull --include="$MODEL_PATH"

if [ -f "$MODEL_PATH" ]; then
  echo "Model downloaded: $MODEL_PATH"
  ls -lh "$MODEL_PATH"
  exit 0
else
  echo "Model not found after git lfs pull. Check remote LFS availability and quota." >&2
  exit 2
fi
