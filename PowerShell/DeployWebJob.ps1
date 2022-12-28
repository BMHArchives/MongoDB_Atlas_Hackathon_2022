###########################################################################
# Author: Brandon M Hunter                                                #
# Date: 12.28.22                                                          #
# Description: This script will zip all python scripts under the          #
# StockTwitterFeeder folder and deploy them out to the StockTwitterFeeder #
# web job.                                                                #
# Assumption: This script assumes that you have previously created a      #
# web job name 'StockTwitterFeeder'                                       #
###########################################################################

$literalPath       = "..\StockTwitterFeeder"
$newFileName       = "StockTwitterFeeder"
$destinationPath   = "..\WebJobArtifacts\StockTwitterFeeder"
$WEB_APP_NAME           = "mongodbdemoapp"
$RESOURCE_GROUP_NAME = "MongoDBDemo_rg"
$WEB_JOB_NAME = "StockTwitterFeeder" # Change this to the web job you created in Azure.
$fileNameAndPath = "$($destinationPath).zip"

Write-Host $destinationPath
Write-Host $fileNameAndPath
Write-Host "Starting - Zipping files from $($literalPath) to $($destinationPath)"
Compress-Archive -LiteralPath $literalPath -DestinationPath $destinationPath

#$files = Get-ChildItem -Path "$($destinationPath).zip"  #$(build.artifactstagingdirectory)\*.zip -Recurse
$files = Get-ChildItem -Path "..\WebJobArtifacts\*.zip" #-Recurse
Test-Path -Path $files[0]
Write-Host $files[0]
#Test-Path -Path $files[0]
Write-Host "Completed - Zipping files from $($literalPath) to $($destinationPath)"

Write-Host "Retreiving publishing credentials"
$app = Get-AzWebApp -ResourceGroupName $RESOURCE_GROUP_NAME -Name $WEB_APP_NAME
$publishingCredentials = Invoke-AzResourceAction `
    -ResourceGroupName $app.ResourceGroup `
    -ResourceType "Microsoft.Web/sites/config" `
    -ResourceName "$($app.Name)/publishingcredentials" `
    -Action list `
    -Force
$user = $publishingCredentials.Properties.PublishingUserName
$pass = $publishingCredentials.Properties.PublishingPassword
$creds = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(("${user}:${pass}")))

# # PUT file
$endpoint = "https://mongodbdemoapp.scm.azurewebsites.net/api/triggeredwebjobs/$($WEB_JOB_NAME)"
# #$endpoint = "https://$($appName).scm.azurewebsites.net/api/$($jobType)webjobs/$($webJobName)"
try{
    Write-Host "Uploading file to $endpoint"
    Write-Host "Trying to update the Web Jobs"
    $ZipHeaders = @{
        "Authorization"     = "Basic $creds" 
        "Content-Disposition" = "attachment; filename=$($files[0].Name)"
    }
    $response = Invoke-WebRequest -Uri $endpoint -Headers $ZipHeaders -InFile $files[0] -ContentType "application/zip" -Method Put
    Write-Host $response    
    Write-Host "Successfully uploaded file"
    Move-Item -Path "$($destinationPath).zip" -Destination "..\WebJobArtifacts\Archive\$($newFileName).zip"
}
catch {
    Move-Item -Path "$($destinationPath).zip" -Destination "..\WebJobArtifacts\Archive\$($newFileName).zip"

    Write-Error "Failed to PUT a file with status $($_.Exception.Response.StatusCode.value__): $($_.ErrorDetails.Message)"
    throw [System.InvalidOperationException] "Failed to deploy file"
}
Remove-Item "..\WebJobArtifacts\Archive\*" -Recurse -Force
