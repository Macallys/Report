# Merge feature/assets and feature/chapter-00..09 into develop.
# Optional: -StartFrom feature/chapter-02 to resume after a resolved conflict.
# Script made by AI agent. Make sure to check before running and manual review.
param(
    [string]$StartFrom = ""
)

$ErrorActionPreference = "Stop"

$branches = @("feature/assets") + (0..9 | ForEach-Object { "feature/chapter-{0:D2}" -f $_ })
if ($StartFrom) {
    $idx = $branches.IndexOf($StartFrom)
    if ($idx -lt 0) { throw "Unknown branch: $StartFrom" }
    $branches = $branches[$idx..($branches.Count - 1)]
}

git fetch origin --prune
if ($LASTEXITCODE -ne 0) { throw "git fetch failed" }

git checkout develop
if ($LASTEXITCODE -ne 0) { throw "git checkout develop failed" }

git pull origin develop
if ($LASTEXITCODE -ne 0) { throw "git pull origin develop failed" }

foreach ($branch in $branches) {
    Write-Host "`n=== Merging $branch into develop ===" -ForegroundColor Cyan
    git merge --no-edit "origin/$branch"
    if ($LASTEXITCODE -ne 0) {
        throw "Merge failed for $branch. Resolve conflicts, then continue."
    }
}

Write-Host "`nAll listed feature branches merged into develop." -ForegroundColor Green
git status
git log --oneline -15
