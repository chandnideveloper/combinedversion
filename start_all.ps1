# start_all.ps1
# Script to clone missing microservices and start them in separate terminal windows.

$repos = @(
    @{ Name = "az-qlikengine-api-repo"; Path = "az-qlikengine-api-repo"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/Qlik-base-engine.git"; StartCommand = "uvicorn main:app --port 8001 --reload" },
    @{ Name = "unified-parsing"; Path = "unified-parsing"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/Parsing.git"; StartCommand = "uvicorn main:app --port 8002 --reload" },
    @{ Name = "mapping"; Path = "mapping (2)\mapping"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/mapping.git"; StartCommand = "uvicorn main:app --port 8003 --reload" },
    @{ Name = "az-wa-repo-generationagent"; Path = "az-wa-repo-generationagent"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/generation.git"; StartCommand = "uvicorn main:app --port 8004 --reload" },
    @{ Name = "unified-semantic-kernel"; Path = "unified-semantic-kernel"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/semantickernel.git"; StartCommand = "uvicorn main:app --port 8000 --reload" },
    @{ Name = "az-repo-mongodb-vl"; Path = "az-repo-mongodb-vl"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/mongo_db.git"; StartCommand = "uvicorn main:app --port 8005 --reload" },
    @{ Name = "vl-t2f-tableu-base-api"; Path = "vl-t2f-tableu-base-api"; Branch = "main"; Url = "https://github.com/krishnau2097-byte/Tableaue-base-api.git"; StartCommand = "uvicorn main:app --port 8006 --reload" },
    @{ Name = "vl-t2f-mongo-db"; Path = "vl-t2f-mongo-db"; Branch = "master"; Url = "https://github.com/krishnau2097-byte/tableaue-mongo-db.git"; StartCommand = "uvicorn main:app --port 8007 --reload" }
)

Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host " Starting QT2F Microservices" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

# 1. Clone missing repositories
foreach ($repo in $repos) {
    # Check if directory exists and has files (e.g., .git)
    $repoPath = Join-Path $PWD $repo.Path
    $isEmpty = $true
    
    if (Test-Path $repoPath) {
        $files = Get-ChildItem -Path $repoPath -Force
        if ($files.Count -gt 0) {
            $isEmpty = $false
        }
    } else {
        New-Item -ItemType Directory -Path $repoPath | Out-Null
    }

    if ($isEmpty) {
        Write-Host "-> Directory '$($repo.Path)' is empty. Cloning from $($repo.Url)..." -ForegroundColor Yellow
        git clone -b $repo.Branch $repo.Url $repoPath
        if ($LASTEXITCODE -ne 0) {
            Write-Host "   ERROR: Failed to clone $($repo.Name)!" -ForegroundColor Red
        } else {
            Write-Host "   SUCCESS: Cloned $($repo.Name)." -ForegroundColor Green
        }
    } else {
        Write-Host "-> Repository '$($repo.Path)' already exists and is not empty. Skipping clone." -ForegroundColor Green
    }
}

Write-Host "`n==================================================================" -ForegroundColor Cyan
Write-Host " Starting Services..." -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

# 2. Start services
# Note: These startup commands are templates. Modify them according to each service's actual entry point.
foreach ($repo in $repos) {
    Write-Host "-> Starting $($repo.Name)..." -ForegroundColor Yellow
    $repoPath = Join-Path $PWD $repo.Path
    
    # We will launch a new PowerShell window for each service
    $scriptBlock = @"
    Set-Location -Path '$repoPath'
    Write-Host 'Starting service: $($repo.Name)' -ForegroundColor Cyan
    Write-Host 'Running: $($repo.StartCommand)' -ForegroundColor Yellow
    # If there is a requirements.txt, install it (optional)
    if (Test-Path 'requirements.txt') {
        Write-Host 'Installing requirements...'
        pip install -r requirements.txt
    }
    $($repo.StartCommand)
    Write-Host 'Service stopped. Press any key to close...'
    `$null = `$Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
"@
    
    # Save the script block to a temporary file
    $tempScript = Join-Path $env:TEMP "start_$($repo.Name).ps1"
    Set-Content -Path $tempScript -Value $scriptBlock
    
    # Start the process in a new window
    Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy", "Bypass", "-File", "`"$tempScript`""
}

# Also start vl-t2f-report-generation which already has code
$reportGenPath = Join-Path $PWD "vl-t2f-report-generation"
Write-Host "-> Starting vl-t2f-report-generation..." -ForegroundColor Yellow
$reportGenScriptBlock = @"
Set-Location -Path '$reportGenPath'
Write-Host 'Starting service: vl-t2f-report-generation' -ForegroundColor Cyan
if (Test-Path 'requirements.txt') {
    pip install -r requirements.txt
}
uvicorn main:app --port 8008 --reload
`$null = `$Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
"@
$tempReportGenScript = Join-Path $env:TEMP "start_report_generation.ps1"
Set-Content -Path $tempReportGenScript -Value $reportGenScriptBlock
Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy", "Bypass", "-File", "`"$tempReportGenScript`""

Write-Host "`n==================================================================" -ForegroundColor Cyan
Write-Host " All services started in separate windows." -ForegroundColor Cyan
Write-Host " Please verify their startup logs in their respective windows." -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
