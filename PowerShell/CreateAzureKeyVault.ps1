#########################################################################
# Author: Brandon M Hunter                                              #
# Date: 12.28.22                                                        #
# Description: This powershell script will connect the user to azure,   #
# create a new key vault and set the access policy on the new key value.#
#########################################################################
Connect-AzAccount
$KEY_VALUE_NAME = "MongoDBDemo-kv"
$RESOURCE_GROUP_NAME = "MongoDBDemo_rg"
$USER_PRINCIPAL_NAME = "<AZURE ACTIVE AD USER EMAIL ADDRESS>"
New-AzResourceGroup -Name $RESOURCE_GROUP_NAME -Location eastus
New-AzKeyVault -Name $KEY_VAULT_NAME  -ResourceGroupName $RESOURCE_GROUP_NAME -Location eastus
Set-AzKeyVaultAccessPolicy -VaultName $KEY_VAULT_NAME -UserPrincipalName $USER_PRINCIPAL_NAME -PermissionsToSecrets delete,get,list,set