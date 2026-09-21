# PowerShell script to push all updated repositories to their GitHub remotes

$repos = @(
    @{ Path = "az-qlikengine-api-repo"; Remote = "origin"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/Qlik-base-engine.git" },
    @{ Path = "unified-parsing"; Remote = "origin"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/Parsing.git" },
    @{ Path = "mapping (2)\mapping"; Remote = "origin"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/mapping.git" },
    @{ Path = "az-wa-repo-generationagent"; Remote = "origin"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/generation.git" },
    @{ Path = "unified-semantic-kernel"; Remote = "origin"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/semantickernel.git" },
    @{ Path = "az-repo-mongodb-vl"; Remote = "origin"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/mongo_db.git" },
    @{ Path = "vl-t2f-tableu-base-api"; Remote = "origin"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/Tableaue-base-api.git" },
    @{ Path = "vl-t2f-mongo-db"; Remote = "origin"; Branch = "master"; Url = "https://github.com/krishnau2097-byte/tableaue-mongo-db.git" }
)

Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host " Pushing all updated code to GitHub remotes" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

$token = $env:GITHUB_TOKEN

foreach ($repo in $repos) {
    Write-Host "`n--> Pushing $($repo.Path) ($($repo.Branch)) to $($repo.Url)..." -ForegroundColor Yellow
    Push-Location $repo.Path
    try {
        $pushUrl = $repo.Url -replace "https://github.com/", "https://$token@github.com/"
        git push $pushUrl $repo.Branch
        if ($LASTEXITCODE -eq 0) {
            Write-Host " SUCCESS: $($repo.Path) pushed successfully!" -ForegroundColor Green
        } else {
            Write-Host " FAILED to push $($repo.Path) (Exit Code: $LASTEXITCODE)" -ForegroundColor Red
        }
    } finally {
        Pop-Location
    }
}

Write-Host "`n==================================================================" -ForegroundColor Cyan
Write-Host " Push process completed!" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
