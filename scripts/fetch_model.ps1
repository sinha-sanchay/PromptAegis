param(
    [string]$ModelPath = "injex/transformer/model/model.safetensors"
)

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "git is not installed or not on PATH. Install Git first."
    exit 1
}

Write-Host "Ensuring Git LFS is installed and initialized..."
git lfs install --local

Write-Host "Fetching latest refs and switching to 'main'..."
git fetch --all
git checkout main

Write-Host "Pulling LFS object: $ModelPath"
git lfs pull --include="$ModelPath"

if (Test-Path $ModelPath) {
    $f = Get-Item $ModelPath
    Write-Host "Model downloaded:" $f.FullName "(" ($f.Length) "bytes)"
    exit 0
} else {
    Write-Error "Model not found after git lfs pull. Check remote LFS availability and quota."
    exit 2
}
