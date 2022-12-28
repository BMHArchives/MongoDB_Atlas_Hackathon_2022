##########################################################################
# Author: Brandon M Hunter                                               #
# Date: 12.28.22                                                         #
# Description: This powershell script will create a new app service plan #
# and create a new web app based on the app service plan that was        #
# recently created.connect the user to azure,                            #
##########################################################################
$RESOURCE_GROUP_NAME = "MongoDBDemo_rg"
$APP_SERVICE_PLAN_NAME = "mongodbdemo_asp"
$WEB_APP_NAME = "mongodbdemoapp"
$appServicePlan = 
$webApp= "mongodbdemoapp"
New-AzAppServicePlan -Name $APP_SERVICE_PLAN_NAME -Location eastus -ResourceGroupName $RESOURCE_GROUP_NAME-Tier Free
New-AzWebApp -Name $WEB_APP_NAME  -Location eastus -AppServicePlan $APP_SERVICE_PLAN_NAME -ResourceGroupName $RESOURCE_GROUP_NAME

# C
